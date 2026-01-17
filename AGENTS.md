## AGENTS.md
## Build & Run

This repo starts as “empty”. Use this as a generic Python scaffold.

### Setup (first time)
- Create venv: `python -m venv .venv`
- Activate (Windows PowerShell): `.venv\Scripts\Activate.ps1`
- Activate (Git Bash): `source .venv/Scripts/activate`
- Activate (macOS/Linux): `source .venv/bin/activate`
- Upgrade pip: `python -m pip install -U pip`

### Install dependencies
- If present: `python -m pip install -r requirements.txt`
- If present (dev): `python -m pip install -r requirements-dev.txt`

## Validation

Run these after implementing to get immediate feedback:

- Tests (pytest): `python -m pytest -q`
- Typecheck (mypy): `python -m mypy .`
- Lint (ruff): `python -m ruff check .`
- Format check (black): `python -m black --check .`

### If tools are missing
Install the standard dev toolchain:
`python -m pip install pytest ruff black mypy`

## Operational Notes

- Always run commands from repo root.
- Prefer adding a minimal `pyproject.toml` to pin tool configs when repo grows.
- Keep tests small and fast; one task per loop iteration.

### Codebase Patterns

- New code goes in a package folder (e.g. `src/<name>/` or `<name>/`), tests in `tests/`.
- Each feature should have at least one test and a clear entrypoint (function or CLI).
