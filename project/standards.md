# 03 Standards

## Naming Conventions

### `metrics/`
- **Required prefix for new APIs**: `calc_` or `fit_`.
- Examples: `calc_sharpe_ratio`, `calc_drawdown_series`, `fit_student_t_distribution`.

### `formulas/`
- **Required prefix for new APIs**: `compute_`, `summarize_`, or `build_`.
- Examples: `compute_grouped_ic`, `summarize_long_short`, `build_trend_vol_regime_mapping`.

### `pipeline/`
- **Required prefix for orchestration entry points**: `run_`, `generate_`, or `evaluate_`.
- Examples: `run_factor_batch`, `generate_predictions`, `evaluate_factor_stability`.
- Analysis helpers that operate on an already prepared in-memory context may use `analyze_*`.

### `interface/`
- Use protocol/config nouns, not workflow verbs.
- Key contracts/files: `calendar.py`, `loader.py`, `model.py`, `config.py` (`IndexSpec`, `ColumnSpec`, `DatasetSpec`, `ParallelSpec`).

## Directory Do/Don't Rules

### `core/metrics`
- **Do**
  - Accept `np.ndarray` / `pd.Series` / simple 1D structures.
  - Return scalar/array/stat tables without index business semantics.
  - Validate shapes and finite values.
- **Don't**
  - Depend on MultiIndex structure, ticker/date levels, or OHLCV column names.
  - Implement groupby-by-date/ticker orchestration.
  - Mix loading/config/backend concerns.

### `core/formulas`
- **Do**
  - Operate on panel-like `pd.Series`/`pd.DataFrame` with explicit column/index assumptions.
  - Use `metrics` as computation building blocks.
  - Keep reusable research logic here, not in pipelines.
- **Don't**
  - Open files or call backend-specific loaders directly.
  - Own full runtime orchestration/stateful workflow concerns.

### `pipeline/analysis`
- **Do**
  - Load inputs via `Interface` contracts.
  - Wire configs, execution sequence, and result dataclasses.
  - Call formulas to compute outputs.
- **Don't**
  - Re-implement low-level statistics already available in `metrics`/`formulas`.
  - Hardcode backend-specific paths inside pipeline logic.

### `core/interface`
- **Do**
  - Keep contracts strict and backend-agnostic.
  - Keep schema defaults (`IndexSpec`, `ColumnSpec`, etc.) explicit.
- **Don't**
  - Include business logic, filesystem I/O, or orchestration.

## Fence Rule (Metrics vs Formulas)
When a function could fit either layer:
- Put it in **metrics** if it is purely mathematical and structure-agnostic.
- Put it in **formulas** if it requires financial/panel semantics (e.g., OHLCV fields, date/ticker index structure, grouped cross-sectional logic).W

## PR Quality Gate
Before merge, verify:
1. New functions are placed in the correct layer.
2. Naming follows the required prefix for that layer.
3. No upward dependency violations (e.g., `metrics` importing `pipeline`).
4. `docs/04_registry.md` is updated for any public function add/remove/rename.
