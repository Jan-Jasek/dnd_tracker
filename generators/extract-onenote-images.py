#!/usr/bin/env python3
"""
Extract images and structured text from OneNote .one backup files.

Strategy:
- Text: scan for UTF-16LE encoded strings (how OneNote stores text),
  which is far more faithful than the prior ASCII `strings` approach.
- Images: carve JPEG and PNG blobs by their magic bytes.

Usage:
    python3 generators/extract-onenote-images.py \
        <source.one> \
        --out-dir imports/onenote/extracted \
        [--images-dir imports/onenote/images]
"""

import argparse
import os
import re
import struct
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Image carving
# ---------------------------------------------------------------------------

JPEG_SOI = b"\xff\xd8\xff"
JPEG_EOI = b"\xff\xd9"
PNG_SIG  = b"\x89PNG\r\n\x1a\n"
PNG_IEND = b"IEND\xae\x42\x60\x82"


def carve_images(data: bytes, out_dir: Path, stem: str) -> list[str]:
    """Carve JPEG and PNG images from raw bytes; return list of saved filenames."""
    saved = []
    idx = 0
    img_num = 0

    while idx < len(data):
        # --- JPEG ---
        j = data.find(JPEG_SOI, idx)
        p = data.find(PNG_SIG, idx)

        next_hit = min(
            j if j != -1 else len(data),
            p if p != -1 else len(data),
        )
        if next_hit == len(data):
            break

        if next_hit == j:
            end = data.find(JPEG_EOI, j + 3)
            if end == -1:
                idx = j + 3
                continue
            end += 2  # include the EOI marker
            blob = data[j:end]
            if len(blob) > 500:  # skip tiny blobs (thumbnails / artefacts)
                img_num += 1
                fname = f"{stem}-img{img_num:03d}.jpg"
                (out_dir / fname).write_bytes(blob)
                saved.append(fname)
            idx = end

        else:  # PNG
            end = data.find(PNG_IEND, p + 8)
            if end == -1:
                idx = p + 8
                continue
            end += len(PNG_IEND)
            blob = data[p:end]
            if len(blob) > 500:
                img_num += 1
                fname = f"{stem}-img{img_num:03d}.png"
                (out_dir / fname).write_bytes(blob)
                saved.append(fname)
            idx = end

    return saved


# ---------------------------------------------------------------------------
# UTF-16LE text extraction
# ---------------------------------------------------------------------------

# Minimum run length (in characters) to be considered a real string
MIN_CHARS = 6

# Allowed Unicode ranges for Latin/Czech/Slovak/English text
# Basic Latin, Latin-1 Supplement, Latin Extended-A/B cover Czech/Slovak
def _is_text_char(cp: int) -> bool:
    return (
        0x0020 <= cp <= 0x007E  # Basic ASCII printable
        or 0x00A0 <= cp <= 0x024F  # Latin-1 + Latin Extended A/B (Czech, Slovak, etc.)
        or cp in (0x0009, 0x000A, 0x000D)  # tab, LF, CR
        or 0x2013 <= cp <= 0x2026  # common typographic chars (en-dash, em-dash, ellipsis)
        or cp in (0x201C, 0x201D, 0x2018, 0x2019)  # curly quotes
    )


def extract_utf16_strings(data: bytes) -> list[str]:
    """
    Scan for UTF-16LE encoded text runs restricted to Latin/Czech character
    ranges.  This avoids picking up binary data that happens to form valid
    high-plane Unicode codepoints.
    """
    results = []
    i = 0

    while i < len(data) - 1:
        run_chars = []
        j = i
        while j + 1 < len(data):
            cp = data[j] | (data[j + 1] << 8)
            if _is_text_char(cp):
                run_chars.append(chr(cp))
                j += 2
            else:
                break

        if len(run_chars) >= MIN_CHARS:
            text = "".join(run_chars).strip()
            if text:
                results.append(text)
            i = j
        else:
            i += 1

    return results


def deduplicate_strings(strings: list[str]) -> list[str]:
    """Remove duplicates while preserving order."""
    seen = set()
    out = []
    for s in strings:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def looks_like_noise(s: str) -> bool:
    """Filter out strings that are unlikely to be real campaign text."""
    if len(s) < MIN_CHARS:
        return True
    # Need some alphanumeric content
    alnum = sum(1 for c in s if c.isalnum())
    if alnum < 2:
        return True
    # Reject if it looks like a path, URL, or XML/HTML tag with no prose
    if s.startswith(("<", "{", "[") ) and ">" in s:
        return True
    return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process(source: Path, out_dir: Path, images_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    stem = source.stem  # e.g. "Dračí nezavislost.one (On 26.04.2026)"
    # Build a slug for filenames
    slug = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
    notebook = source.parent.name

    data = source.read_bytes()
    print(f"[{notebook}/{source.name}] {len(data):,} bytes", file=sys.stderr)

    # --- Images ---
    images = carve_images(data, images_dir, slug)
    print(f"  Carved {len(images)} image(s)", file=sys.stderr)

    # --- Text ---
    strings = extract_utf16_strings(data)
    strings = deduplicate_strings(strings)
    strings = [s for s in strings if not looks_like_noise(s)]
    print(f"  Extracted {len(strings)} text strings", file=sys.stderr)

    # --- Write markdown ---
    out_path = out_dir / f"{slug}.md"
    with out_path.open("w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"id: import.onenote.{slug}\n")
        f.write(f"type: onenote-extract\n")
        f.write(f"status: draft\n")
        f.write(f"source_format: one\n")
        f.write(f'source_path: "{source}"\n')
        f.write(f'notebook: "{notebook}"\n')
        f.write(f'section: "{stem}"\n')
        f.write("---\n\n")
        f.write(f"# {stem}\n\n")
        f.write("> Extracted from OneNote backup via UTF-16LE string scan. Review before promoting to canon.\n\n")

        if images:
            f.write("## Images\n\n")
            for img in images:
                f.write(f"![{img}](../images/{img})\n\n")

        f.write("## Content\n\n")
        for s in strings:
            # Heuristic: lines shorter than 80 chars are likely headings/labels
            if "\n" not in s and len(s) < 80:
                f.write(f"- {s}\n")
            else:
                f.write(f"{s}\n\n")

    print(f"  Written: {out_path}", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser(description="Extract text and images from OneNote .one files")
    ap.add_argument("source", nargs="+", help=".one file(s) to process")
    ap.add_argument("--out-dir", default="imports/onenote/extracted",
                    help="Directory for extracted markdown files")
    ap.add_argument("--images-dir", default="imports/onenote/images",
                    help="Directory for carved image files")
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    images_dir = Path(args.images_dir)

    for src in args.source:
        process(Path(src), out_dir, images_dir)


if __name__ == "__main__":
    main()
