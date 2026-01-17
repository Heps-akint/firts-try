## PRD.md

# PRD: Ralph Loop Smoke Test (Python)

Goal: Create the smallest possible Python “feature” with real backpressure so the Ralph loop can plan, implement, run tests, and mark done.

## PRD-01: Minimal greeter module + tests (smoke test)

User story:
As a developer, I want a tiny Python module with a function that returns a greeting string so I can verify the Ralph loop end-to-end (plan → implement → test → commit).

Acceptance criteria:
- A function `greet(name: str) -> str` exists.
- If `name` is `"Heps"`, it returns exactly `"Hello, Heps!"`.
- If `name` is `""` or only whitespace, it returns exactly `"Hello, world!"`.
- Unit tests exist and pass via: `python -m pytest -q`.
- A minimal `pyproject.toml` exists so the repo has a clear Python/tooling baseline.
