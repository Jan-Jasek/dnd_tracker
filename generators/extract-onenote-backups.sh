#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 OUTPUT_DIR SOURCE_DIR [SOURCE_DIR ...]" >&2
  exit 2
fi

output_dir="$1"
shift

mkdir -p "$output_dir"

slugify() {
  printf "%s" "$1" \
    | iconv -c -t ascii//TRANSLIT 2>/dev/null \
    | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//'
}

extract_one() {
  local source_path="$1"
  local notebook
  local section
  local slug
  local target

  notebook="$(basename "$(dirname "$source_path")")"
  if [ "$notebook" = "OneNote_RecycleBin" ]; then
    notebook="$(basename "$(dirname "$(dirname "$source_path")")")/OneNote_RecycleBin"
  fi

  section="$(basename "$source_path" .one)"
  slug="$(slugify "$notebook--$section")"
  target="$output_dir/$slug.md"

  {
    echo "---"
    echo "id: import.onenote.$slug"
    echo "type: onenote-extract"
    echo "status: draft"
    echo "source_format: one"
    echo "source_path: \"$source_path\""
    echo "notebook: \"$notebook\""
    echo "section: \"$section\""
    echo "---"
    echo
    echo "# $section"
    echo
    echo "> Extracted from OneNote backup via printable strings. Review before promoting to canon."
    echo
    strings -a -n 5 "$source_path" \
      | sed -E 's/[[:cntrl:]]+/ /g; s/[[:space:]]+$//' \
      | awk '
          length($0) < 3 { next }
          /^[[:space:]]*$/ { next }
          /^[[:punct:][:space:]]+$/ { next }
          /^(AUUQA|\?VU&A|W<qq\*|QK|;@|Aff|BUUU|V6Z|I6&|n1zur|[A-Za-z0-9+\/]{20,}=*)$/ { next }
          { print }
        '
  } > "$target"
}

for source_dir in "$@"; do
  find "$source_dir" -type f -name "*.one" -print0 | while IFS= read -r -d '' file_path; do
    extract_one "$file_path"
  done || true
done
