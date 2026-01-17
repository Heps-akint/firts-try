# AGENTS.md (Codex “operational contract”)

## Goal
Make it cheap for any fresh Codex session to:
1) understand how to validate changes
2) run the correct commands
3) avoid repo-specific footguns

Keep this file short. No status updates here.

## Build & Run (edit these once per project)
- Install:
  - (fill in) e.g. `pnpm i` OR `pip install -r requirements.txt` OR `poetry install`
- Dev run:
  - (fill in) e.g. `pnpm dev` OR `python -m app`

## Validation (the backpressure)
Run these after every change. Prefer fast + deterministic.
- Unit tests (fast): (fill in) e.g. `pnpm test -r` / `pytest -q`
- Full tests (CI-like): (fill in)
- Typecheck: (fill in) e.g. `pnpm typecheck` / `mypy .`
- Lint/format: (fill in) e.g. `pnpm lint` / `ruff check .`

If unsure which commands exist, discover them (package.json, Makefile, README) then update this file.

## Git workflow (default)
- One Ralph iteration = one focused commit.
- Commit message format:
  - `feat(prd-XX): …` or `fix(prd-XX): …` or `chore: …`
- Always include updates to: PRD.md / IMPLEMENTATION_PLAN.md / progress.md when relevant.

## Safety rails
- Do NOT touch secrets, tokens, SSH keys, or any `.env` not required.
- Do NOT run destructive commands (`rm -rf`, `git reset --hard`, mass deletes) unless explicitly asked.
- Prefer minimal diffs. No drive-by refactors unless required to pass validation.
