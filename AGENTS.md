# AGENTS.md

## Working Rules

- `CURRENT_PLAN.md` is the only current execution entry point; `MASTER_PLAN.md` is the roadmap; `TODO_BACKLOG.md` holds candidates.
- `data/entries.json` is the single source of truth. Never hand-edit `README.md`, `README.zh-CN.md` or `docs/image-prompts.md`; run `python3 tools/render_readme.py`.
- Only English and Chinese. Every entry needs URL, verified license (with the page it was verified on), and use in both languages.
- Verify licenses for real: GitHub API `license` field for repos, the official license page for websites. Unclear license = do not add. No pirated, cracked or star-farmed repos. Never make up data.
- Images: prefer the project's own preview, hotlinked from its original address with credit. Only for covers or entries without an original image, add an original generated image to `docs/images/` (WebP/PNG, < 300 KB) and its prompt to `data/image-prompts.json`. Never copy third-party images into the repo.
- Zero telemetry: no analytics, trackers, counters or visitor badges.
- Always run `python3 tools/verify.py` (offline) and `python3 tools/check_links.py` (network) before claiming completion.
- Changes go through a PR; do not push content to `main` directly. When the current plan is done, run `python3 tools/next_plan.py`.

## Owner-required presentation

- Keep all 297 resources in genuine category-grouped comparison tables in both READMEs and catalogs. Do not replace tables with cards or vertical entry lists to claim mobile responsiveness.
- For narrow screens, reduce column count and use GitHub's native table scrolling. Keep project/source, preview attribution, license evidence and description. Test actual GitHub rendering and disclose horizontal table scrolling.
- Keep an original, project-specific game-themed hero in both README languages. Record the real generation prompt/tool; do not relabel third-party art as original.

## Original previews and compact tables

- Asset rows prefer hotlinked original project screenshots/samples with source credit. A code license is not a media reuse grant; do not describe hotlinking as permission to redistribute. Verify real image bytes, visual content and the source reference.
- No synthetic stand-ins in asset rows when an original can be found. Missing/blocked sources are labelled, not faked; the generated project hero remains separate.
- Default to 15 visible entries per category, the rest in native details/summary containing real tables. Keep all entries and test expansion on GitHub.
- State practical use conditions first, followed by the linked license in parentheses on a new line. Preserve noncommercial, attribution, share-alike and per-asset boundaries.
- Sort comparable GitHub entries using dated total-star evidence; never invent missing website popularity or call total stars recent growth.
