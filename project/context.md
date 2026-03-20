# 01 Context

## Project Purpose
`alpha` is a quantitative investment research framework focused on factor and model evaluation.
Its core goal is to make cross-sectional alpha research repeatable by separating:
- pure statistical math (`core/metrics`),
- research logic (`core/formulas`),
- orchestration pipelines (`pipeline/analysis`),
- backend contracts (`core/interface`) and concrete data/model adapters (`integration/*`).

## What This Repository Does
The codebase supports an end-to-end research loop:
1. Load panel features/targets for `(dt, ticker)` from a backend.
2. Compute factor/model diagnostics (IC, IR, quantile spreads, drift, regime behavior, drawdown).
3. Aggregate analysis into pipeline-level result objects.
4. Render report figures for single-factor and batch-factor workflows.

## Core Research Workloads Implemented
- **Factor analysis pipeline**: `load_factor_batch_inputs` + `prepare_factor_context` + modular `analyze_factor_*` + `run_factor_batch`.
- **Model comparison workflow**: `load_analysis_inputs` + `prepare_context` + modular `analyze_*` functions (pairwise corr, top-k overlap, IC decay, contribution, incremental, regime, rolling OOS, cost/capacity).
- **Distribution/heteroscedasticity pipeline**: univariate distribution diagnostics and grouped variance analysis.
- **Regime analytics**: trend/volatility/liquidity regime detection and tagging.

## Canonical Data Shape
Most analysis code assumes panel data with:
- MultiIndex: `(dt, ticker)`
- `dt`: date or intraday timestamp string (often `YYYYMMDDHHMMSS`)
- one or more numeric columns (`factor`, `target`, `target_{h}`, feature terms, predictions)

## Backend Strategy
- **Interface-first** design in `core/interface` (Protocol contracts).
- **AIXI backend** in `integration/aixi` provides production adapters.
- **Mock and test utilities** in `core/data/mock.py` allow local deterministic tests.

## Scope Boundaries (High Level)
- `metrics`: structure-agnostic math functions.
- `formulas`: research logic that understands panel structure and domain columns.
- `pipeline`: execution orchestration and result assembly.
- `interface`: contracts/config schemas for backend decoupling.

This document is the conceptual entry point; use:
- `docs/02_architecture.md` for dependency and folder boundaries,
- `docs/03_standards.md` for naming/Do-Don't rules,
- `docs/04_registry.md` for function lookup.
