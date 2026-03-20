## Build, Test, and Development Commands
- `python -m pip install -e .` installs the package in editable mode.
- `python -m pytest -q` runs the full test suite.
- `python -m pytest tests/test_factor_report.py -q` runs a focused test file.
- `python -m build` creates source/wheel distributions using `setuptools`.

## Testing Guidelines
- Framework: `pytest` with files named `test_*.py` and functions named `test_*`.
- Add regression tests for bug fixes and edge cases (NaN handling, index alignment, empty inputs).
- No fixed coverage gate is configured; changed behavior must include targeted tests.
