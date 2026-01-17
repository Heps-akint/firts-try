# IMPLEMENTATION_PLAN

Purpose: the “how-next”. Disposable. Rewritten by planning mode whenever it drifts.

Rules:
- Each task references one PRD ID.
- One build iteration completes ONE task.
- Tasks must be small enough to fit in a single Codex session.

---

## Now (highest priority first)

1) [x] TASK-PRD-01-A: Add minimal greeter module and pyproject baseline
   - PRD: PRD-01
   - What to change: add `greeter/` package with `greet(name: str) -> str`, add minimal `pyproject.toml`
   - Required validation: `python -m ruff check .`, `python -m black --check .`, `python -m mypy .`
   - Completion definition: `greeter/__init__.py` (or `greeter/core.py` + `__init__.py`) implements `greet`, `pyproject.toml` pins tool config

2) [x] TASK-PRD-01-B: Add tests for greet behavior
   - PRD: PRD-01
   - What to change: add `tests/test_greeter.py`
   - Required validation: `python -m pytest -q`
   - Completion definition: tests cover `"Heps"` and blank/whitespace cases and pass

---

## Later / parking lot
- [ ] <stuff discovered but not urgent>
