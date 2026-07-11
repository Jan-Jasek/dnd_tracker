ROOT_DIR := $(CURDIR)
AI_GENERATED_PATHS := AGENTS.md CLAUDE.md .claude .codex .cursor

.PHONY: ai_generate ai_check format lint static

static: lint ai_check

lint:
	npm run format:check

format:
	npm run format

ai_generate:
	npm run ai:generate

ai_check:
	@set -e; \
	tmp="$$(mktemp -d)"; \
	trap 'rm -rf "$$tmp"' EXIT; \
	cp -R .rulesync rulesync.jsonc "$$tmp"/; \
	(cd "$$tmp" && "$(ROOT_DIR)/node_modules/.bin/rulesync" generate --config rulesync.jsonc >/dev/null); \
	for path in $(AI_GENERATED_PATHS); do \
		if [ -e "$$tmp/$$path" ] || [ -e "$$path" ]; then \
			diff -ru "$$path" "$$tmp/$$path"; \
		fi; \
	done
