# 05 Pipeline Design Principles

This document captures the architectural patterns that every `pipeline/analysis/` module
must follow.  The goal is to prevent recurring design pitfalls (monolithic runners,
coupled I/O + analysis, missing composite-level evaluation) and keep the codebase
simple, practical, and easy to extend.


## 1  Three-Layer Architecture

Every analysis pipeline is split into exactly three layers.
Each layer has a single responsibility and a clear data boundary.

```
Layer 1  ──  Inputs        load data from Interface (slow, run once)
                │
Layer 2  ──  Context       pre-compute derived objects: predictions, IC series,
                │          composite aggregations, etc. (medium, run once)
                │
Layer 3  ──  Analyzers     stateless analyze_*() functions (fast, run many times
                           with different parameters)
```

### Layer 1: Inputs

- **Responsibility**: Load raw data via `Interface` contracts (calendar, loader, model).
- **Output**: A frozen `*Inputs` dataclass holding sessions, features, targets, models, etc.
- **Rules**:
  - Must be the *only* layer that touches I/O or network.
  - Returns immutable, backend-agnostic data structures.
  - Called once per analysis session; downstream layers never re-load data.

### Layer 2: Context

- **Responsibility**: Transform raw inputs into everything the analyzers need.
- **Output**: A `*Context` dataclass holding derived objects (e.g., predictions,
  IC series, composite/block/ensemble aggregations).
- **Rules**:
  - No I/O.  Operates purely on the `*Inputs` object.
  - All expensive one-time computations live here (e.g., running model.predict,
    computing IC series for every name).
  - Must expose a **uniform namespace** for individual items *and* composite
    items (see Section 3 below).
  - Called once; all `analyze_*` functions receive the same context.

### Layer 3: Analyzers

- **Responsibility**: Compute a specific analysis slice (quality, stability,
  incremental contribution, regime breakdown, etc.).
- **Signature**: `analyze_*(ctx, names, **params) -> DataFrame | dict`
- **Rules**:
  - Stateless — no side effects, no I/O, no mutation of `ctx`.
  - Accepts a list of `names` to analyze; works identically regardless of
    whether those names refer to individual items, blocks, or the ensemble.
  - Internally delegates to `core/formulas/*` for the actual math.
  - Fast enough to call interactively in a notebook cell.


## 2  No Monolithic Runner

A top-level `run_*_analysis()` convenience function *may* exist, but it must be
a thin composition of the three layers above.  It must never be the only way to
run the analysis.

### Anti-pattern (do not repeat)

```python
def run_analysis(config, interface):
    # loads data
    # computes predictions
    # runs ALL analyses
    # returns one giant Result dataclass
```

Problems with this pattern:
- Changing baseline/candidate requires re-loading data and re-computing predictions.
- Cannot run a subset of analyses.
- Cannot add a new analysis dimension without touching the monolith.

### Required pattern

```python
inputs = load_inputs(config, interface)      # Layer 1
ctx    = prepare_context(config, inputs)      # Layer 2
quality   = analyze_quality(ctx, names)       # Layer 3
stability = analyze_stability(ctx, names)     # Layer 3
incremental = analyze_incremental(ctx, ...)   # Layer 3
```


## 3  Uniform Namespace for Composites

When a domain has a natural hierarchy (e.g., models -> blocks -> ensemble,
or factors -> factor groups -> composite), the Context must store all levels
in a single flat dict keyed by name.

### Example (model analysis)

```
ctx.preds = {
    "lgb_1d_0": Series,    # individual model
    "block_1":  Series,    # block = mean(models in block)
    "ensemble": Series,    # ensemble = mean(blocks)
}
```

This way, every `analyze_*` function works at any granularity without special
case logic:

```python
analyze_quality(ctx, ["lgb_1d_0", "lgb_1d_1"])           # individual
analyze_quality(ctx, ["block_1", "block_2"])              # block
analyze_quality(ctx, ["ensemble"])                        # ensemble
analyze_incremental(ctx, baseline=["block_1"], ...)       # block-level delta
```

### Guidelines

- Composite keys must not collide with individual keys.
- The `prepare_context` function is responsible for computing and inserting
  composites into the dict.
- Analyzers must never assume or check whether a name is individual or composite.


## 4  Incremental Analysis Must Be a Separate Analyzer

Baseline-vs-candidate comparisons (delta IC/IR, leave-one-in/out, significance
tests) must live in their own `analyze_incremental()` function, not be baked
into config or the context.

- `baseline` and `candidates` are *parameters of the analyzer*, not global config
  fields.
- This allows calling `analyze_incremental` in a loop with different
  baseline/candidate combinations without re-loading or re-predicting.


## 5  Regime and Conditional Analysis

Regime analysis (market-state-dependent performance) follows the same analyzer
pattern:

```python
analyze_regime(ctx, names, market_df, ...)
```

- `market_df` is passed to the analyzer, not to config or context.
- The analyzer internally computes the dt-to-regime mapping and delegates to
  formulas for grouped statistics.
- This keeps the context free of external data dependencies and makes regime
  analysis fully optional.


## 6  Extending to New Domains

When creating a new `pipeline/analysis/<domain>.py` module:

1. Define `<Domain>Config`, `<Domain>Inputs`, `<Domain>Context` dataclasses.
2. Implement `load_<domain>_inputs(config, interface)`.
3. Implement `prepare_<domain>_context(config, inputs)`.
4. Add `analyze_*` functions as needed — each one small, stateless, and
   independently callable.
5. If a convenience runner is desired, implement it as a thin wrapper that
   calls the three layers and collects results.

### Checklist before merging a new pipeline module

- [ ] No I/O outside of `load_*_inputs`.
- [ ] `prepare_*_context` produces a uniform namespace (individual + composite).
- [ ] Every `analyze_*` function works on arbitrary name subsets.
- [ ] Incremental / regime analysis is not hardcoded into config or context.
- [ ] All math delegated to `core/formulas/*` or `core/metrics/*`.
