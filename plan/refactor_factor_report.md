# 92 Plan: Refactor `report/factor.py`

## Goal
Refactor `src/alpha/report/factor.py` into a simple, practical, low-coupling reporting layer that:
- fully covers the reportable functionality exposed by `src/alpha/pipeline/analysis/factor.py`
- presents outputs through figures and structured report tables
- contains no duplicated business logic from `pipeline`, `formulas`, or `metrics`
- remains extensible for future stage additions without rewriting core report flow
- degrades gracefully when funnel stages are disabled, empty, or not implemented

This plan follows the engineering standards:
- simple and practical
- low coupling, high cohesion
- extensible and flexible
- orthogonal
- robust and resilient
- evolutionary
- testable
- SOLID / DRY / KISS / YAGNI / MVP

## Current State

### What exists now
- `src/alpha/report/factor.py` supports:
  - single-factor overview
  - single-factor IC decay
  - batch factor summary
  - partial funnel report helpers
- `src/alpha/pipeline/analysis/factor.py` exposes funnel-stage analyzers:
  - `analyze_funnel_screening`
  - `analyze_funnel_orthogonal`
  - `analyze_funnel_redundancy`
  - `analyze_funnel_multiplicity`
  - `analyze_funnel_selection_bias`
  - `analyze_funnel_bootstrap_null`
  - `analyze_funnel_threshold`
  - `analyze_funnel_oos`
  - `analyze_funnel_capacity`
  - `analyze_funnel_incremental`
  - `analyze_funnel_bayesian`
  - `analyze_funnel_review`
  - `analyze_funnel_tiers`

### Current problems
- report responsibilities are mixed:
  - some presentation-only logic
  - some data assembly logic
  - some direct compute calls bypassing analyzer layer
- report coverage is not yet organized as a complete, explicit mapping from funnel stages to report artifacts
- report API shape is inconsistent:
  - old factor report path
  - newer funnel report path
- stage outputs are not normalized into one stable report contract
- unimplemented funnel stages need controlled visibility in reports, not implicit failure paths
- figure set is still MVP-level; table/report bundle contract needs to become the primary artifact

## Scope and Blast Radius
- In scope:
  - `src/alpha/report/factor.py`
  - `src/alpha/report/__init__.py`
  - `tests/test_factor_report.py`
  - `docs/04_registry.md`
  - this plan doc
- Out of scope:
  - `src/alpha/pipeline/analysis/factor.py` business logic changes
  - `core/formulas/*` and `core/metrics/*`
  - notebooks
  - model report

## Design Principles for This Refactor

### Hard rules
- Report layer is presentation-only plus thin orchestration of analyzer calls.
- No business-stat logic duplicated in `report`.
- No direct fallback into `formulas` or `metrics` when an analyzer already exists.
- One canonical report bundle contract:
  - tables first
  - figures derived from tables/context
- Each stage is independent:
  - add/remove one stage without breaking unrelated report modules
- Disabled or unimplemented stages must produce explicit report status, not silent omission.
- Empty/insufficient data must render safely.

### Dependency rule
- Allowed:
  - `report -> pipeline.analysis.factor`
  - `report -> pipeline.analysis.univariate`
  - `report -> matplotlib/pandas/numpy`
- Avoid:
  - `report -> core.formulas.*` direct business compute
  - `report -> integration/*`
  - `report -> backend/interface`

## Design Target

### Primary report contract
- `generate_factor_funnel_report_tables(ctx, *, respect_config=True) -> dict[str, pd.DataFrame]`
- `generate_factor_funnel_report_figures(ctx, *, tables=None) -> dict[str, Figure]`
- `generate_factor_funnel_report(ctx, *, respect_config=True) -> dict[str, dict]`

### Stable output structure
- `tables["stage_status"]`
- `tables["card_summary"]`
- `tables["screening"]`
- `tables["orthogonal"]`
- `tables["redundancy"]`
- `tables["multiplicity"]`
- `tables["selection_bias"]`
- `tables["bootstrap_null"]`
- `tables["threshold"]`
- `tables["oos"]`
- `tables["capacity"]`
- `tables["incremental"]`
- `tables["bayesian"]`
- `tables["review"]`
- `tables["tiers"]`

### Figure families
- health / execution:
  - stage status
  - disabled / unimplemented / error visibility
- ranking:
  - confidence ranking
  - tier distribution
- screening:
  - IC mean vs IC IR
- redundancy:
  - correlation heatmap
- stage-specific visuals:
  - add later only when stage data semantics are stable

### Extension rule
New stage reporting must require only:
1. add analyzer to stage spec map
2. add optional table normalizer if needed
3. add optional stage figure

No core control-flow rewrite.

## Functional Coverage Matrix

### Mandatory coverage
- `analyze_funnel_screening`
  - table
  - ranking/scatter figure inputs
- `analyze_funnel_orthogonal`
  - table
- `analyze_funnel_redundancy`
  - table
  - corr heatmap when matrix available
- `analyze_funnel_multiplicity`
  - table
- `analyze_funnel_selection_bias`
  - explicit status even if unimplemented
- `analyze_funnel_bootstrap_null`
  - explicit status even if unimplemented
- `analyze_funnel_threshold`
  - explicit status even if unimplemented
- `analyze_funnel_oos`
  - explicit status even if unimplemented
- `analyze_funnel_capacity`
  - explicit status even if unimplemented
- `analyze_funnel_incremental`
  - explicit status even if unimplemented
- `analyze_funnel_bayesian`
  - explicit status even if unimplemented
- `analyze_funnel_review`
  - table
- `analyze_funnel_tiers`
  - table
  - tier/confidence visuals

### Secondary coverage
- Existing single-factor report functions stay supported:
  - `plot_factor_analysis_overview`
  - `plot_factor_ic_decay`
  - `plot_factor_batch_summary`
  - `generate_factor_report_figures`

These remain legacy-compatible surfaces, but funnel report becomes the structured primary path.

## Refactor Phases

---

## Phase 1: Freeze Desired Architecture
1. Write plan doc.
2. Define canonical report responsibilities:
   - gather analyzer outputs
   - normalize tables
   - render figures
3. Define explicit non-goals:
   - no new factor research logic
   - no report-driven analyzer rewrites

Exit criteria:
- one approved plan doc exists
- future edits follow this file

---

## Phase 2: Normalize Report Control Flow
1. Introduce or refine a single stage registry:
   - stage name
   - analyzer function
   - config gating
2. Ensure all funnel stages run through one common execution path.
3. Standardize per-stage result handling:
   - `ok`
   - `skipped_disabled`
   - `unimplemented`
   - `error`
4. Keep exceptions visible in `stage_status`, not hidden.

Exit criteria:
- all funnel stages use one shared execution model
- no per-stage ad hoc runner logic

---

## Phase 3: Remove Report-Layer Logic Duplication
1. Audit `report/factor.py` for direct calls into `core.formulas` and `core.metrics`.
2. Replace direct business computations with analyzer/context consumption where possible.
3. Keep only presentation-local helpers in `report`:
   - plotting helpers
   - empty-state rendering
   - simple table alignment/formatting

Exit criteria:
- report contains zero duplicated research logic
- dependency direction remains clean

---

## Phase 4: Make Tables the Source of Truth
1. Ensure every reportable funnel stage has a normalized table slot.
2. Build `card_summary` as the compact summary table for downstream use.
3. Make figures consume normalized tables whenever possible.
4. Keep `ctx.batch` access limited to artifacts not yet materialized into tables:
   - example: redundancy corr matrix

Exit criteria:
- figures are downstream of tables, not hidden recomputation paths
- report bundle is notebook-friendly and test-friendly

---

## Phase 5: Rationalize Figure Surface
1. Keep the initial figure set small and high-signal.
2. Avoid one chart per metric unless it materially improves interpretation.
3. Organize figures by report purpose:
   - status
   - screening
   - ranking
   - redundancy
4. Add stage-specific charts only when they do not create coupling or special-case code explosion.

Exit criteria:
- figure surface is practical, not bloated
- adding a new figure does not require changing core report orchestration

---

## Phase 6: Testing
1. Add/maintain tests for:
   - stage-status generation
   - disabled-stage skipping
   - unimplemented-stage downgrade
   - card summary generation
   - figure bundle key stability
   - empty-data rendering
2. Keep tests unit-level and deterministic.
3. Do not require backend access.

Exit criteria:
- report tests fully cover control flow and output contracts

---

## Phase 7: Docs Sync
1. Update `docs/04_registry.md` for public report API changes.
2. Keep doc edits minimal and scoped.
3. If report architecture meaningfully changes public guidance later, update `docs/02_architecture.md` or `docs/03_standards.md` only if needed.

Exit criteria:
- public report APIs are documented
- no noisy unrelated doc churn

## Acceptance Criteria
- `report/factor.py` covers all reportable functionality exposed by `pipeline/analysis/factor.py`
- all funnel stages have explicit visibility in report outputs
- report layer contains no duplicated quantitative business logic
- report degrades safely on empty / disabled / unimplemented stages
- figure and table APIs are stable and easy to compose in notebooks/tests
- adding one new funnel stage requires local change only
- tests protect the contract

## Risk Controls
- Prefer additive cleanup before deleting legacy helpers.
- Keep old single-factor report APIs working.
- Do not change analyzer semantics from report refactor.
- Avoid creating a giant "universal report class"; use small functions and flat data contracts.
- If a stage is unimplemented in pipeline, represent that as report state, not fake data.

## Implementation Sequence
1. freeze plan
2. normalize stage registry and status handling
3. remove report-layer duplicated logic
4. standardize tables bundle
5. rationalize figure bundle
6. strengthen tests
7. refresh registry

## Definition of Done
- plan doc committed
- factor report refactor completed against this plan
- tests pass
- registry updated
- unrelated notebook/user files untouched
