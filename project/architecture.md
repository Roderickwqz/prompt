# 02 Architecture

## Layered Architecture (Required)
The project is organized as a strict layered system.

| Layer | Primary Paths | Responsibility | Allowed Downstream Dependencies |
|---|---|---|---|
| `metrics` | `src/alpha/core/metrics` | Pure numerical/statistical primitives | `numpy/pandas/scipy` and internal metric utils only |
| `formulas` | `src/alpha/core/formulas` | Research formulas over panel structures; combines metrics | `core/metrics`, `core/formulas/shared`, `numpy/pandas` |
| `pipeline` | `src/alpha/pipeline/analysis` | End-to-end task orchestration and result packaging | `core/formulas`, `core/interface`, `integration/utils` |
| `interface` | `src/alpha/core/interface` | Protocol contracts + schema/config specs | typing/dataclasses only (no business logic) |

Supporting modules:
- `src/alpha/integration/*`: concrete backend adapters implementing interface contracts.
- `src/alpha/core/data/*`: preprocessing, CV strategy, mock-data utilities.
- `src/alpha/models/*`: model inference wrappers (`BaseFactorModel`, `LightGBMFactorModel`).
- `src/alpha/report/*`: visualization/reporting over pipeline outputs.

## Dependency Direction
Strict conceptual flow:

`metrics` -> `formulas` -> `pipeline`

Operational runtime flow for production jobs:

`integration backend` -> `interface` -> `pipeline` -> `formulas` -> `metrics` -> `pipeline results` -> `report`

## Folder Map (Current Repository)

```text
src/alpha/
  core/
    metrics/      # pure math/statistics (calc_*/fit_* expected)
    formulas/     # research formula layer (compute_*/summarize_*/build_ expected)
    interface/    # contracts/config: Calendar/Loader/Model + IndexSpec/ColumnSpec/...
    data/         # preprocessing, CV strategies, mock data generation
  pipeline/
    analysis/     # run_* / generate_* orchestration entry points
  integration/
    aixi/         # concrete production backend
    local/        # local backend placeholders (currently empty files)
    utils.py      # backend-neutral utility helpers
  models/         # inference wrappers and base model protocol
  report/         # plotting/report figure assembly
```

## Boundary Rules to Enforce

### `metrics` boundary
- Must remain structure-agnostic.
- No business-domain assumptions about columns like OHLCV/date/ticker.
- No grouping/index orchestration.

### `formulas` boundary
- Can require panel index semantics and named columns.
- Can orchestrate grouping and call multiple `metrics` functions.
- Should not orchestrate full run lifecycle across loading/config/reporting.

### `pipeline` boundary
- Owns run order, parameter wiring, backend calls, and result DTO assembly.
- Should avoid re-implementing quantitative formulas internally.

### `interface` boundary
- Defines contracts only; no backend filesystem logic.
- Concrete behavior belongs in `integration/*` implementations.

## Practical Review Checklist
When reviewing a new function:
1. If it only transforms numeric arrays/Series and is context-free -> `metrics`.
2. If it needs panel/group/date/ticker semantics -> `formulas`.
3. If it loads data/models and orchestrates multi-step analysis -> `pipeline`.
4. If it defines schemas/protocols/contracts -> `interface`.
