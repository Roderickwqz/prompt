# Coding Standards

## 1. Clean Code & Readability
- **Naming:** Descriptive variable names. Use `snake_case` for Python, `PascalCase` for classes.
- **Type Hinting:** Mandatory for all function signatures (e.g., `def run(data: pd.DataFrame) -> bool:`).
- **KISS:** No "clever" one-liners. Prioritize clarity over brevity.

## 2. Robustness (Error Handling)
- **Fail Fast:** Validate inputs at the start of functions.
- **Graceful Degradation:** Use `try-except` blocks for external I/O (API calls, DB access).
- **Logging:** Use structured logging instead of `print()`. Include context.

## 3. Testing Standard
- **Unit First:** Every logic change must have a corresponding test case in `/tests/`.
- **Mocking:** Mock external dependencies (APIs, network) to ensure tests are fast and isolated.
- **Assertion:** Tests must assert both "Happy Path" and "Edge Cases" (errors/empty inputs).

## 4. Documentation
- **Docstrings:** Required for all public classes and methods (Google or NumPy style).
- **Comments:** Explain "Why," not "What." Code should tell "What" by itself.

## 5. Performance (Quant-Specific)
- **Vectorization:** Prefer NumPy/Pandas vectorized operations over `for` loops.
- **Memory:** Be mindful of large dataset copies; use in-place operations where safe.