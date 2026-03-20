# 04 Registry

Public callable registry for the current codebase.

Index criteria: public top-level functions + public class methods (private helpers with leading `_` are excluded).

## Summary

- Total indexed callables: **319**
- `metrics`: 76
- `formulas`: 94
- `pipeline`: 45
- `interface`: 12
- `data`: 29
- `integration`: 48
- `models`: 3
- `report`: 12

## Metrics

### `src/alpha/core/metrics/_utils.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `clean_1d_finite` | `src/alpha/core/metrics/_utils.py:30` | Convert input data to a 1D float NumPy array and remove non-finite values. | Input: (data: ArrayLike1D, clean: bool = True) -> np.ndarray |
| `clean_1d_finite_pair` | `src/alpha/core/metrics/_utils.py:46` | Convert two inputs to aligned 1D float NumPy arrays and remove positions | Input: (x: ArrayLike1D, y: ArrayLike1D,) -> Tuple[np.ndarray, np.ndarray] |

### `src/alpha/core/metrics/bayesian.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_bayes_factor` | `src/alpha/core/metrics/bayesian.py:8` | Approximate Bayes factor in favor of signal from t-statistics. | Input: (t_stat: ArrayLike1D | float, *, scale: float = 0.5,) -> float | np.ndarray |
| `calc_posterior_probability` | `src/alpha/core/metrics/bayesian.py:34` | Posterior P(signal|data) from Bayes factor and prior. | Input: (bayes_factor: ArrayLike1D | float, *, prior_prob: float = 0.5,) -> float | np.ndarray |

### `src/alpha/core/metrics/capacity.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_market_impact` | `src/alpha/core/metrics/capacity.py:8` | Parametric impact model: impact(q) = c * (q / V) ** alpha. | Input: (q: ArrayLike1D | float, V: ArrayLike1D | float, *, c: float = 0.01, alpha: float = 0.5,) -> float | np.ndarray |
| `calc_capacity_breakeven` | `src/alpha/core/metrics/capacity.py:43` | Solve AUM* where gross_alpha - impact(turnover * AUM) = alpha_min. | Input: (gross_alpha: float, alpha_min: float, turnover: float, adv: float, *, c: float = 0.01, impact_alpha: float = 0.5,) -> float |

### `src/alpha/core/metrics/correlation.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_ic` | `src/alpha/core/metrics/correlation.py:42` | Calculate correlation-based IC between two 1D arrays. | Input: (y_true: ArrayLike1D, y_pred: ArrayLike1D, method: Literal["pearson", "spearman"] = "spearman", dropna: bool = True,) -> float |
| `calc_ic_stats` | `src/alpha/core/metrics/correlation.py:70` | Summarize an IC series into mean/std/IR statistics. | Input: (ics: ArrayLike1D, periods: int = 252, *, periods_per_year: Optional[int] = None,) -> Dict[str, float] |
| `calc_ir` | `src/alpha/core/metrics/correlation.py:115` | Calculate Information Ratio from an IC series. | Input: (ics: ArrayLike1D, dropna: bool = True,) -> float |
| `calc_annualized_ir` | `src/alpha/core/metrics/correlation.py:142` | No docstring; see implementation. | Input: (ir: float, periods_per_year: int = 252,) -> float |
| `calc_grouped_ic` | `src/alpha/core/metrics/correlation.py:149` | Calculate per-group IC values with contiguous-slice iteration. | Input: (y_true: np.ndarray, y_pred: np.ndarray, groups: np.ndarray, method: Literal["pearson", "spearman"] = "spearman",) -> pd.Series |
| `calc_corr_pvalue` | `src/alpha/core/metrics/correlation.py:202` | Compute the p-value associated with a correlation coefficient. | Input: (x: ArrayLike1D, y: ArrayLike1D, method: Literal["pearson", "spearman"] = "spearman", dropna: bool = True,) -> float |
| `calc_corr_matrix` | `src/alpha/core/metrics/correlation.py:245` | Compute a correlation matrix for a 2D dataset. | Input: (X: Union[np.ndarray, pd.DataFrame], method: str = "pearson",) -> np.ndarray |
| `calc_auto_corr` | `src/alpha/core/metrics/correlation.py:284` | Compute the autocorrelation of a time series at a specified lag. | Input: (x: ArrayLike1D, lag: int = 1, dropna: bool = True,) -> float |

### `src/alpha/core/metrics/drift.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_psi` | `src/alpha/core/metrics/drift.py:98` | Compute the Population Stability Index (PSI) between two samples. | Input: (expected: ArrayLike1D, actual: ArrayLike1D, bins: Union[int, ArrayLike1D] = 10, epsilon: float = 1e-10,) -> float |
| `calc_kl_divergence` | `src/alpha/core/metrics/drift.py:132` | Compute histogram-based Kullback-Leibler divergence KL(p || q). | Input: (p: ArrayLike1D, q: ArrayLike1D, bins: Union[int, ArrayLike1D] = 10, epsilon: float = 1e-10,) -> float |
| `calc_js_distance` | `src/alpha/core/metrics/drift.py:166` | Compute histogram-based Jensen-Shannon distance between two samples. | Input: (p: ArrayLike1D, q: ArrayLike1D, bins: Union[int, ArrayLike1D] = 10, epsilon: float = 1e-10, base: float = 2.0,) -> float |
| `calc_wasserstein_distance` | `src/alpha/core/metrics/drift.py:204` | Compute the first Wasserstein distance between two samples. | Input: (p: ArrayLike1D, q: ArrayLike1D,) -> float |
| `calc_ks_statistic` | `src/alpha/core/metrics/drift.py:228` | Compute the two-sample Kolmogorov-Smirnov statistic and p-value. | Input: (p: ArrayLike1D, q: ArrayLike1D, alternative: str = "two-sided", method: str = "auto",) -> Tuple[float, float] |

### `src/alpha/core/metrics/error.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_mse` | `src/alpha/core/metrics/error.py:24` | Compute the mean squared error (MSE) between two 1D arrays. | Input: (y_true: ArrayLike1D, y_pred: ArrayLike1D, dropna: bool = True,) -> float |
| `calc_rmse` | `src/alpha/core/metrics/error.py:38` | Compute the root mean squared error (RMSE) between two 1D arrays. | Input: (y_true: ArrayLike1D, y_pred: ArrayLike1D, dropna: bool = True,) -> float |
| `calc_mae` | `src/alpha/core/metrics/error.py:67` | Compute the mean absolute error (MAE) between two 1D arrays. | Input: (y_true: ArrayLike1D, y_pred: ArrayLike1D, dropna: bool = True,) -> float |
| `calc_smape` | `src/alpha/core/metrics/error.py:81` | Compute the symmetric mean absolute percentage error (sMAPE) | Input: (y_true: ArrayLike1D, y_pred: ArrayLike1D, dropna: bool = True, epsilon: float = 1e-12,) -> float |
| `calc_median_ae` | `src/alpha/core/metrics/error.py:124` | Compute the median absolute error between two 1D arrays. | Input: (y_true: ArrayLike1D, y_pred: ArrayLike1D, dropna: bool = True,) -> float |
| `calc_r2` | `src/alpha/core/metrics/error.py:138` | Compute the coefficient of determination (R-squared) between two 1D arrays. | Input: (y_true: ArrayLike1D, y_pred: ArrayLike1D, dropna: bool = True,) -> float |
| `calc_explained_variance` | `src/alpha/core/metrics/error.py:164` | Compute the explained variance score between two 1D arrays. | Input: (y_true: ArrayLike1D, y_pred: ArrayLike1D, dropna: bool = True,) -> float |

### `src/alpha/core/metrics/hypothesis.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_bonferroni_pvalue` | `src/alpha/core/metrics/hypothesis.py:90` | No docstring; see implementation. | Input: (pvalues: ArrayLike1D, n_tests: int | None = None,) -> float | np.ndarray |
| `calc_holm_pvalue` | `src/alpha/core/metrics/hypothesis.py:101` | No docstring; see implementation. | Input: (pvalues: ArrayLike1D, n_tests: int | None = None,) -> float | np.ndarray |
| `calc_bh_fdr` | `src/alpha/core/metrics/hypothesis.py:113` | No docstring; see implementation. | Input: (pvalues: ArrayLike1D, n_tests: int | None = None,) -> float | np.ndarray |
| `calc_by_fdr` | `src/alpha/core/metrics/hypothesis.py:125` | No docstring; see implementation. | Input: (pvalues: ArrayLike1D, n_tests: int | None = None,) -> float | np.ndarray |
| `calc_local_fdr` | `src/alpha/core/metrics/hypothesis.py:139` | Empirical Bayes-style local FDR estimate on p-values. | Input: (pvalues: ArrayLike1D, *, lambda_: float = 0.5, bins: int = 20, epsilon: float = 1e-12,) -> float | np.ndarray |
| `calc_fdr_miss_curve` | `src/alpha/core/metrics/hypothesis.py:175` | Compute FDR(tau) and MISS(tau) along thresholds. | Input: (scores: ArrayLike1D, labels: ArrayLike1D, *, thresholds: ArrayLike1D | None = None, higher_score_better: bool = True,) -> pd.DataFrame |
| `calc_optimal_threshold` | `src/alpha/core/metrics/hypothesis.py:236` | Choose threshold that minimizes lambda_fdr * FDR + lambda_miss * MISS. | Input: (thresholds: ArrayLike1D, fdr: ArrayLike1D, miss: ArrayLike1D, *, lambda_fdr: float = 1.0, lambda_miss: float = 1.0,) -> float |

### `src/alpha/core/metrics/portfolio.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_quantile_return` | `src/alpha/core/metrics/portfolio.py:6` | Calculate returns by prediction quantile | Input: (predictions: np.ndarray, returns: np.ndarray, n_quantiles: int = 5) -> Dict[str, np.ndarray] |
| `calc_long_short_return` | `src/alpha/core/metrics/portfolio.py:38` | Calculate long-short portfolio return | Input: (predictions: np.ndarray, returns: np.ndarray, long_pct: float = 0.2, short_pct: float = 0.2) -> float |
| `calc_top_turnover` | `src/alpha/core/metrics/portfolio.py:73` | Calculate portfolio turnover between two periods | Input: (predictions_t: np.ndarray, predictions_t1: np.ndarray, top_pct: float = 0.2) -> float |
| `calc_set_turnover` | `src/alpha/core/metrics/portfolio.py:97` | Calculate turnover between two holdings sets. | Input: (previous: set, current: set,) -> float |
| `calc_turnover_stats` | `src/alpha/core/metrics/portfolio.py:113` | Summarize turnover series statistics. | Input: (turnover: np.ndarray) -> Dict[str, float] |
| `calc_net_turnover` | `src/alpha/core/metrics/portfolio.py:138` | Combine long/short leg turnover into a net one-way turnover series. | Input: (long_turnover: np.ndarray, short_turnover: np.ndarray, *, long_weight: float = 0.5, short_weight: float = 0.5, crossing_rate: float = 0.0,) -> np.ndarray |
| `calc_cost_adjusted_ir` | `src/alpha/core/metrics/portfolio.py:185` | Compute gross/net IR after linear turnover-based trading costs. | Input: (gross_returns: np.ndarray, turnover: np.ndarray | float, *, cost_per_turnover: float, periods_per_year: int = 252,) -> Dict[str, float] |

### `src/alpha/core/metrics/risk.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_rolling_volatility` | `src/alpha/core/metrics/risk.py:8` | Calculate rolling volatility from a return series. | Input: (returns: pd.Series, window: int = 20, min_periods: Optional[int] = None, method: str = "realized_vol", annualize: bool = False, periods_per_year: int = 252, ddof: int = 1,) -> pd.Series |
| `calc_sharpe_ratio` | `src/alpha/core/metrics/risk.py:74` | Calculate annualized Sharpe ratio. | Input: (returns: ArrayLike1D, risk_free_rate: float = 0.0, periods: int = 252,) -> float |
| `calc_beta` | `src/alpha/core/metrics/risk.py:105` | Calculate beta relative to market returns. | Input: (returns: ArrayLike1D, market_returns: ArrayLike1D,) -> float |
| `calc_tracking_error` | `src/alpha/core/metrics/risk.py:137` | Calculate annualized tracking error. | Input: (returns: ArrayLike1D, benchmark_returns: ArrayLike1D, periods: int = 252,) -> float |
| `calc_equity_curve` | `src/alpha/core/metrics/risk.py:164` | Build equity curve from periodic returns. | Input: (returns: ArrayLike1D, initial_value: float = 1.0,) -> np.ndarray |
| `calc_drawdown_series` | `src/alpha/core/metrics/risk.py:186` | Calculate drawdown series from an equity curve. | Input: (equity_curve: ArrayLike1D,) -> np.ndarray |
| `calc_max_drawdown` | `src/alpha/core/metrics/risk.py:213` | Calculate maximum drawdown from an equity curve. | Input: (equity_curve: ArrayLike1D,) -> float |
| `calc_average_drawdown` | `src/alpha/core/metrics/risk.py:233` | Calculate average drawdown over underwater periods. | Input: (equity_curve: ArrayLike1D,) -> float |
| `calc_drawdown_duration_series` | `src/alpha/core/metrics/risk.py:257` | Calculate drawdown duration at each time step. | Input: (equity_curve: ArrayLike1D,) -> np.ndarray |
| `calc_max_drawdown_duration` | `src/alpha/core/metrics/risk.py:290` | Calculate maximum drawdown duration. | Input: (equity_curve: ArrayLike1D,) -> int |

### `src/alpha/core/metrics/selection.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_deflated_sharpe_ratio` | `src/alpha/core/metrics/selection.py:19` | Approximate deflated Sharpe ratio (DSR) as a posterior probability-like score in [0, 1]. | Input: (sharpe: float, n_trials: int, T: int, skew: float = 0.0, kurt: float = 3.0,) -> float |
| `calc_haircut_sharpe` | `src/alpha/core/metrics/selection.py:56` | Apply a multiplicity haircut to Sharpe using a log-trials penalty. | Input: (sharpe: float, n_trials: int, *, penalty_scale: float = 0.1, penalty_power: float = 0.5, min_factor: float = 0.0,) -> float |
| `calc_max_statistic_pvalue` | `src/alpha/core/metrics/selection.py:84` | Two-sided p-value for max(|Z_1|,...,|Z_n|) under iid standard normal null. | Input: (observed_stat: float, n_trials: int, *, clip_z: float = 12.0,) -> float |

### `src/alpha/core/metrics/similarity.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_jaccard_index` | `src/alpha/core/metrics/similarity.py:5` | Calculate the Jaccard index between two collections. | Input: (a: Iterable[Hashable], b: Iterable[Hashable],) -> float |
| `calc_overlap_ratio` | `src/alpha/core/metrics/similarity.py:50` | Calculate an overlap ratio between two collections. | Input: (a: Iterable[Hashable], b: Iterable[Hashable], *, denominator: str = "union",) -> float |
| `calc_topk_overlap_count` | `src/alpha/core/metrics/similarity.py:124` | Count the overlap size between the Top-K selections of two score arrays. | Input: (values_a: Sequence[float], values_b: Sequence[float], *, k: int, labels: Optional[Sequence[Hashable]] = None,) -> int |

### `src/alpha/core/metrics/stats.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_median_mad` | `src/alpha/core/metrics/stats.py:41` | Compute median and median absolute deviation (MAD). | Input: (values: ArrayLike1D, clean: bool = True) -> Tuple[float, float] |
| `calc_skewness_kurtosis` | `src/alpha/core/metrics/stats.py:54` | Compute skewness and kurtosis. | Input: (values: ArrayLike1D, bias: bool = True, fisher: bool = True, clean: bool = True,) -> Tuple[float, float] |
| `calc_abs_exceedance_rate` | `src/alpha/core/metrics/stats.py:81` | Compute empirical exceedance rate P(|x| > threshold). | Input: (values: ArrayLike1D, threshold: float = 3.0, clean: bool = True,) -> float |
| `calc_zscore_tail_probability` | `src/alpha/core/metrics/stats.py:99` | Compute empirical tail probability P(|z| > threshold). | Input: (values: ArrayLike1D, threshold: float = 3.0, standardize: bool = True, ddof: int = 1, clean: bool = True,) -> float |
| `fit_student_t_distribution` | `src/alpha/core/metrics/stats.py:136` | Fast moment-based Student-t parameter estimation. | Input: (values: ArrayLike1D, clean: bool = True, min_samples: int = 10, min_df: float = 2.1, max_df: float = 200.0,) -> Tuple[float, float, float] |
| `calc_quantiles` | `src/alpha/core/metrics/stats.py:187` | Compute empirical quantiles. | Input: (values: ArrayLike1D, quantiles: Sequence[float], method: str = "linear", clean: bool = True,) -> Dict[float, float] |
| `calc_iqr` | `src/alpha/core/metrics/stats.py:210` | Compute interquantile range (default IQR = Q3 - Q1). | Input: (values: ArrayLike1D, q_low: float = 0.25, q_high: float = 0.75, method: str = "linear", clean: bool = True,) -> float |
| `calc_normality_tests` | `src/alpha/core/metrics/stats.py:235` | Run normality tests on one-dimensional numeric data. | Input: (values: ArrayLike1D, tests: Optional[Sequence[str]] = None, alpha: float = 0.05, clean: bool = True,) -> Dict[str, Dict] |
| `calc_adf_stationarity` | `src/alpha/core/metrics/stats.py:297` | Run Augmented Dickey-Fuller stationarity test. | Input: (values: ArrayLike1D, autolag: str = "AIC", alpha: float = 0.05, clean: bool = True,) -> Dict |
| `calc_autocorrelation_series` | `src/alpha/core/metrics/stats.py:339` | Compute autocorrelation values for lags 1..max_lag. | Input: (values: ArrayLike1D, max_lag: int = 20, clean: bool = True,) -> pd.DataFrame |
| `calc_variance_homogeneity` | `src/alpha/core/metrics/stats.py:377` | Test variance homogeneity across groups. | Input: (groups: Sequence[ArrayLike1D], test: Literal["levene", "bartlett"] = "levene", alpha: float = 0.05, center: Literal["mean", "median", "trimmed"] = "median", clean: bool = True,) -> Dict[str, float | int | bool | str] |
| `calc_block_bootstrap_ci` | `src/alpha/core/metrics/stats.py:446` | Estimate a confidence interval via moving-block bootstrap. | Input: (values: ArrayLike1D, *, statistic: Callable[[np.ndarray], float] = np.mean, block_size: int = 5, n_bootstrap: int = 1000, ci: float = 0.95, random_state: Optional[int] = None, clean: bool = True,) -> Dict[str, float] |
| `calc_block_bootstrap_pvalue` | `src/alpha/core/metrics/stats.py:545` | Estimate bootstrap p-value for a one-sample statistic under moving blocks. | Input: (values: ArrayLike1D, *, statistic: Callable[[np.ndarray], float] = np.mean, block_size: int = 5, n_bootstrap: int = 2000, null_value: float = 0.0, alternative: Literal["two-sided", "greater", "less"] = "two-sided", random_state: Optional[int] = None, clean: bool = True,) -> Dict[str, float] |
| `calculate_tail_outlier_rates` | `src/alpha/core/metrics/stats.py:626` | Compute empirical rates for P(|z| > threshold) across multiple thresholds. | Input: (values: ArrayLike1D, thresholds: Sequence[float] = (3, 4, 5, 6), clean: bool = True,) -> Dict[str, float] |
| `calculate_basic_statistics` | `src/alpha/core/metrics/stats.py:646` | Compute a comprehensive set of univariate basic statistics. | Input: (values: ArrayLike1D, percentiles: Optional[Sequence[float]] = None, clean: bool = True,) -> Dict |
| `fit_parametric_distributions` | `src/alpha/core/metrics/stats.py:689` | Fit selected parametric distributions and report params/AIC/BIC. | Input: (values: ArrayLike1D, distributions: Optional[Sequence[str]] = None, clean: bool = True,) -> Dict[str, Dict] |
| `calculate_variance_ratio_summary` | `src/alpha/core/metrics/stats.py:758` | Summarize dispersion of a positive scale-like series (for example, std values). | Input: (values: ArrayLike1D, clean: bool = True,) -> Dict[str, float] |
| `calc_distribution_fingerprint` | `src/alpha/core/metrics/stats.py:780` | Compute a compact distribution fingerprint. | Input: (values: ArrayLike1D, clean: bool = True,) -> Dict[str, float] |

### `src/alpha/core/metrics/trend.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `calc_linear_slope_tstat` | `src/alpha/core/metrics/trend.py:6` | No docstring; see implementation. | Input: (values: np.ndarray) -> float |
| `calc_rolling_slope_tstat` | `src/alpha/core/metrics/trend.py:42` | Calculate rolling t-statistic of the slope from a linear time trend regression. | Input: (values: pd.Series, window: int = 60, min_periods: Optional[int] = None, use_log: bool = False) -> pd.Series |

## Formulas

### `src/alpha/core/formulas/bayesian.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_posterior_table` | `src/alpha/core/formulas/bayesian.py:9` | Build per-factor posterior probability table from t-stat evidence. | Input: (evidence: pd.DataFrame, *, tstat_col: str = "t_stat", prior_col: str = "prior_prob", factor_col: str = "factor_name", scale: float = 0.5,) -> pd.DataFrame |
| `compute_tier_assignment` | `src/alpha/core/formulas/bayesian.py:51` | Map posterior and optional hard gates to tiers A/B/C/D/E. | Input: (posterior_table: pd.DataFrame, *, posterior_col: str = "posterior_probability", multiplicity_pass_col: str | None = None, oos_survival_col: str | None = None, incremental_col: str | None = None, capacity_col: str | None = None, rationale_col: str | None = None, redundancy_col: str | None = None, review_col: str | None = None,) -> pd.DataFrame |

### `src/alpha/core/formulas/bootstrap.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_residual_null_distribution` | `src/alpha/core/formulas/bootstrap.py:39` | Bootstrap empirical null distribution from residual series. | Input: (residuals: ArrayLike1D, *, statistic: Callable[[np.ndarray], float] = np.mean, block_size: int = 5, n_bootstrap: int = 1000, random_state: int | None = None, center: bool = True,) -> np.ndarray |
| `compute_cluster_null_distribution` | `src/alpha/core/formulas/bootstrap.py:71` | Cluster-aware null distributions; each cluster bootstrapped independently. | Input: (residuals: pd.Series, clusters: pd.Series, *, statistic: Callable[[np.ndarray], float] = np.mean, block_size: int = 5, n_bootstrap: int = 500, random_state: int | None = None,) -> dict[object, np.ndarray] |
| `compute_calibrated_cutoffs` | `src/alpha/core/formulas/bootstrap.py:103` | Compute empirical significance cutoffs from null distribution. | Input: (null_distribution: ArrayLike1D, *, alpha: float = 0.05, two_sided: bool = True,) -> dict[str, float] |

### `src/alpha/core/formulas/capacity.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_impact_adjusted_alpha` | `src/alpha/core/formulas/capacity.py:9` | Net alpha after deducting parametric impact costs. | Input: (gross_alpha: pd.Series, trade_size: pd.Series, adv: pd.Series, *, c: float = 0.01, impact_alpha: float = 0.5,) -> pd.Series |
| `compute_aum_scaling_curve` | `src/alpha/core/formulas/capacity.py:37` | Compute net alpha over an AUM grid. | Input: (gross_alpha: float, alpha_min: float, turnover: float, adv: float, aum_grid: np.ndarray, *, c: float = 0.01, impact_alpha: float = 0.5,) -> pd.DataFrame |
| `compute_tradability_score` | `src/alpha/core/formulas/capacity.py:80` | Composite tradability score in [0, 1] from turnover/liquidity/borrow proxies. | Input: (turnover: pd.Series, liquidity_ratio: pd.Series, borrow_cost: pd.Series | None = None, *, w_turnover: float = 0.4, w_liquidity: float = 0.4, w_borrow: float = 0.2,) -> pd.Series |

### `src/alpha/core/formulas/card.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `RegistryInfo` | `src/alpha/core/formulas/card.py:9` | No docstring; see implementation. | Class |
| `RationaleInfo` | `src/alpha/core/formulas/card.py:16` | No docstring; see implementation. | Class |
| `ScreeningInfo` | `src/alpha/core/formulas/card.py:25` | No docstring; see implementation. | Class |
| `OrthogonalInfo` | `src/alpha/core/formulas/card.py:37` | No docstring; see implementation. | Class |
| `RedundancyInfo` | `src/alpha/core/formulas/card.py:46` | No docstring; see implementation. | Class |
| `MultiplicityInfo` | `src/alpha/core/formulas/card.py:54` | No docstring; see implementation. | Class |
| `SelectionBiasInfo` | `src/alpha/core/formulas/card.py:63` | No docstring; see implementation. | Class |
| `BootstrapNullInfo` | `src/alpha/core/formulas/card.py:71` | No docstring; see implementation. | Class |
| `ThresholdInfo` | `src/alpha/core/formulas/card.py:78` | No docstring; see implementation. | Class |
| `OOSInfo` | `src/alpha/core/formulas/card.py:86` | No docstring; see implementation. | Class |
| `CapacityInfo` | `src/alpha/core/formulas/card.py:97` | No docstring; see implementation. | Class |
| `IncrementalInfo` | `src/alpha/core/formulas/card.py:109` | No docstring; see implementation. | Class |
| `BayesianInfo` | `src/alpha/core/formulas/card.py:118` | No docstring; see implementation. | Class |
| `ReviewInfo` | `src/alpha/core/formulas/card.py:127` | No docstring; see implementation. | Class |
| `FactorSummary` | `src/alpha/core/formulas/card.py:138` | No docstring; see implementation. | Class |
| `FactorCard` | `src/alpha/core/formulas/card.py:150` | No docstring; see implementation. | Class |
| `FunnelBatch` | `src/alpha/core/formulas/card.py:176` | No docstring; see implementation. | Class |

### `src/alpha/core/formulas/drift.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_feature_drift` | `src/alpha/core/formulas/drift.py:42` | Compute drift metrics for multiple feature columns. | Input: (baseline_features: pd.DataFrame, current_features: pd.DataFrame, method: str = "psi", threshold: float = 0.2, bins: int = 10,) -> pd.DataFrame |
| `compute_target_drift` | `src/alpha/core/formulas/drift.py:107` | Compute drift metrics for a single target variable. | Input: (baseline_targets: Union[pd.Series, np.ndarray], current_targets: Union[pd.Series, np.ndarray], method: str = "psi", threshold: float = 0.2, bins: int = 10,) -> Dict |
| `compute_rolling_drift` | `src/alpha/core/formulas/drift.py:152` | Compute drift metrics over time using rolling windows. | Input: (baseline_data: Union[pd.Series, pd.DataFrame], rolling_data: Union[pd.Series, pd.DataFrame], window: int = 100, step: int = 20, method: str = "psi", bins: int = 10,) -> pd.DataFrame |

### `src/alpha/core/formulas/eda.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_tail_outlier_rates` | `src/alpha/core/formulas/eda.py:39` | Compute empirical tail probabilities for multiple thresholds. | Input: (values: ArrayLike1D, thresholds: Sequence[float] = (3, 4, 5, 6), clean: bool = True,) -> Dict[str, float] |
| `compare_parametric_distributions` | `src/alpha/core/formulas/eda.py:50` | Fit selected parametric distributions and compare AIC/BIC. | Input: (values: ArrayLike1D, distributions: Optional[Sequence[str]] = None, clean: bool = True,) -> Dict[str, Dict] |
| `compute_variance_ratio_summary` | `src/alpha/core/formulas/eda.py:65` | Summarize dispersion ratios from a scale-like numeric series. | Input: (values: ArrayLike1D, clean: bool = True,) -> Dict[str, float] |
| `summarize_basic_statistics` | `src/alpha/core/formulas/eda.py:75` | Compute basic statistics; optionally attach distribution fingerprint. | Input: (values: ArrayLike1D, percentiles: Optional[Sequence[float]] = None, clean: bool = True, include_fingerprint: bool = False,) -> Dict |
| `summarize_group_dispersion` | `src/alpha/core/formulas/eda.py:96` | Summarize dispersion statistics of `value_col` grouped by `group_col`. | Input: (data: pd.DataFrame, value_col: str, group_col: str, top_n: Optional[int] = None, min_count: int = 1, std_ddof: int = 1,) -> pd.DataFrame |
| `compute_group_variance_homogeneity` | `src/alpha/core/formulas/eda.py:148` | Compute variance homogeneity across groups defined in a DataFrame. | Input: (data: pd.DataFrame, value_col: str, group_col: str, test: Literal["levene", "bartlett"] = "levene", alpha: float = 0.05, min_group_size: int = 2, center: Literal["mean", "median", "trimmed"] = "median", clean: bool = True,) -> Dict[str, float | int | bool | str] |

### `src/alpha/core/formulas/factor.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_grouped_quantile_labels` | `src/alpha/core/formulas/factor.py:12` | Assign cross-sectional factor quantile labels within each group. | Input: (factor: pd.Series, groups: Optional[pd.Series] = None, group_level: Optional[str] = None, n_quantiles: int = 5,) -> pd.Series |
| `compute_grouped_ic` | `src/alpha/core/formulas/factor.py:47` | High-level interface: Aligns data and computes IC per group efficiently. | Input: (factor: pd.Series, target: pd.Series, groups: Optional[pd.Series] = None, group_level: Optional[str] = None, method: Literal["pearson", "spearman"] = "spearman",) -> pd.Series |
| `compute_ic_decay` | `src/alpha/core/formulas/factor.py:99` | Calculate IC decay summary across multiple target horizons. | Input: (factor: pd.Series, targets_by_horizon: Dict[str, pd.Series], groups: Optional[pd.Series] = None, group_level: Optional[str] = None, method: Literal["pearson", "spearman"] = "spearman", periods_per_year: int = 252,) -> pd.DataFrame |
| `compute_long_short_series` | `src/alpha/core/formulas/factor.py:145` | Calculate long-short return series from quantile return table. | Input: (quantile_returns: pd.DataFrame,) -> pd.Series |
| `compute_factor_return_series` | `src/alpha/core/formulas/factor.py:174` | Run cross-sectional regression within each group and return the factor slope series. | Input: (factor: pd.Series, forward_returns: pd.Series, groups: Optional[pd.Series] = None, group_level: Optional[str] = None, weights: Optional[pd.Series] = None, add_intercept: bool = True,) -> pd.Series |
| `compute_rank_autocorrelation` | `src/alpha/core/formulas/factor.py:260` | Calculate factor rank autocorrelation across groups. | Input: (factor: pd.Series, groups: Optional[pd.Series] = None, group_level: Optional[str] = None, ticker_level: str = "ticker", lag: int = 1, method: Literal["pearson", "spearman"] = "spearman",) -> pd.Series |
| `compute_grouped_quantile_returns` | `src/alpha/core/formulas/factor.py:334` | Calculate mean forward returns by factor quantile within each group. | Input: (factor: pd.Series, forward_returns: pd.Series, groups: Optional[pd.Series] = None, group_level: Optional[str] = None, n_quantiles: int = 5, weights: Optional[pd.Series] = None,) -> pd.DataFrame |
| `summarize_long_short` | `src/alpha/core/formulas/factor.py:417` | Summarize a long-short return series. | Input: (long_short_returns: pd.Series, periods_per_year: int = 252,) -> Dict[str, float] |
| `summarize_factor_return` | `src/alpha/core/formulas/factor.py:462` | Summarize a factor return (beta) series. | Input: (factor_return_series: pd.Series, periods_per_year: int = 252,) -> Dict[str, float] |

### `src/alpha/core/formulas/model.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_pairwise_cs_corr_series` | `src/alpha/core/formulas/model.py:230` | Compute cross-sectional pairwise correlation series across groups. | Input: (data: pd.DataFrame, columns: Sequence[str], *, group_level: str = "dt", method: Literal["pearson", "spearman"] = "spearman", min_entities: int = 3,) -> Dict[PairKey, List[float]] |
| `compute_pairwise_topk_jaccard_series` | `src/alpha/core/formulas/model.py:268` | Compute pairwise top-k or bottom-k Jaccard similarity series across groups. | Input: (data: pd.DataFrame, columns: Sequence[str], k: int, *, group_level: str = "dt", min_entities: int = 3, selection: Literal["top", "bottom"] = "top",) -> Dict[PairKey, List[float]] |
| `compute_cs_ic` | `src/alpha/core/formulas/model.py:337` | Compute cross-sectional information coefficient by group. | Input: (pred: pd.Series, target: pd.Series, *, group_level: str = "dt", method: Literal["pearson", "spearman"] = "spearman",) -> pd.Series |
| `summarize_pairwise_cs_corr` | `src/alpha/core/formulas/model.py:374` | Summarize pairwise cross-sectional correlation series into matrices. | Input: (data: pd.DataFrame, columns: Sequence[str], *, group_level: str = "dt", method: Literal["pearson", "spearman"] = "spearman", min_entities: int = 3, stats: Tuple[str, ...] = ("mean", "median", "p05", "p95"),) -> Dict[str, pd.DataFrame] |
| `generate_grouped_performance_table` | `src/alpha/core/formulas/model.py:424` | Generate a regime-stratified performance summary table for multiple models. | Input: (models: Sequence[str], preds: Dict[str, pd.Series], target: pd.Series, dt_to_regime: pd.Series, periods: int, ic_method: Literal["pearson", "spearman"] = "spearman", n_quantiles: int = 5,) -> pd.DataFrame |
| `generate_prediction_quality` | `src/alpha/core/formulas/model.py:522` | Generate core prediction-quality KPIs for multiple models. | Input: (preds: Dict[str, pd.Series], target: pd.Series, models: Sequence[str], periods: int, ic_method: Literal["pearson", "spearman"] = "spearman", worst_window: int = 20, n_quantiles: int = 5,) -> pd.DataFrame |
| `generate_stability_tail_risk` | `src/alpha/core/formulas/model.py:586` | Analyze IC stability and tail-risk characteristics for multiple models. | Input: (preds: Dict[str, pd.Series], target: pd.Series, models: Sequence[str], rolling_window: int = 21, ic_method: Literal["pearson", "spearman"] = "spearman", extreme_threshold: float = 0.02,) -> pd.DataFrame |
| `generate_similarity_stats` | `src/alpha/core/formulas/model.py:658` | Generate similarity statistics for predictions and prediction errors. | Input: (preds: Dict[str, pd.Series], target: pd.Series, models: Sequence[str], method: Literal["pearson", "spearman"] = "spearman", min_entities: int = 3,) -> Dict[str, Dict[str, pd.DataFrame]] |
| `generate_pred_corr_stats` | `src/alpha/core/formulas/model.py:724` | Summarize pairwise cross-sectional prediction correlations across groups. | Input: (preds: Mapping[str, pd.Series], models: Sequence[str], *, method: Literal["pearson", "spearman"] = "spearman", min_ticker: int = 3, stats: Sequence[str] = ("mean", "median", "p05", "p95"), group_level: str = "dt",) -> Dict[str, pd.DataFrame] |
| `generate_error_corr_stats` | `src/alpha/core/formulas/model.py:750` | Summarize pairwise cross-sectional error correlations across groups. | Input: (target: pd.Series, preds: Mapping[str, pd.Series], models: Sequence[str], *, method: Literal["pearson", "spearman"] = "spearman", min_ticker: int = 3, stats: Sequence[str] = ("mean", "median", "p05", "p95"), group_level: str = "dt",) -> Dict[str, pd.DataFrame] |
| `generate_pred_and_error_corr` | `src/alpha/core/formulas/model.py:786` | Return both prediction and error correlation summary tables. | Input: (preds: Mapping[str, pd.Series], target: pd.Series, models: Sequence[str], *, method: Literal["pearson", "spearman"] = "spearman", min_ticker: int = 3, stats: Sequence[str] = ("mean", "median", "p05", "p95"), group_level: str = "dt",) -> Dict[str, Dict[str, pd.DataFrame]] |
| `compute_ic_decay_by_model` | `src/alpha/core/formulas/model.py:820` | Compute IC decay statistics for each model over multiple horizons. | Input: (preds: Mapping[str, pd.Series], targets_by_horizon: Mapping[str, pd.Series], models: Sequence[str], *, periods: int, ic_method: Literal["pearson", "spearman"] = "spearman", group_level: str = "dt",) -> pd.DataFrame |
| `compute_leave_one_out_ir_contribution` | `src/alpha/core/formulas/model.py:868` | Compute leave-one-out ensemble IR contribution per model. | Input: (preds: Mapping[str, pd.Series], target: pd.Series, models: Sequence[str], *, periods: int, ic_method: Literal["pearson", "spearman"] = "spearman", group_level: str = "dt",) -> pd.DataFrame |
| `compute_single_model_ir_table` | `src/alpha/core/formulas/model.py:937` | Summarize per-model IR and annualized IR. | Input: (preds: Mapping[str, pd.Series], target: pd.Series, models: Sequence[str], *, periods: int, ic_method: Literal["pearson", "spearman"] = "spearman", group_level: str = "dt",) -> pd.DataFrame |
| `compute_baseline_delta_ic_ir` | `src/alpha/core/formulas/model.py:971` | Compare baseline ensemble vs baseline-plus-candidate for IC/IR deltas. | Input: (preds: Mapping[str, pd.Series], target: pd.Series, baseline_models: Sequence[str], candidate_models: Sequence[str] | None = None, *, periods: int, ic_method: Literal["pearson", "spearman"] = "spearman", group_level: str = "dt",) -> pd.DataFrame |
| `compute_leave_one_in_ir_contribution` | `src/alpha/core/formulas/model.py:1071` | Compute leave-one-in IR contribution by adding one model to the baseline. | Input: (preds: Mapping[str, pd.Series], target: pd.Series, baseline_models: Sequence[str], candidate_models: Sequence[str] | None = None, *, periods: int, ic_method: Literal["pearson", "spearman"] = "spearman", group_level: str = "dt",) -> pd.DataFrame |
| `compute_delta_significance_table` | `src/alpha/core/formulas/model.py:1130` | Estimate significance of baseline-vs-candidate IC deltas with block bootstrap. | Input: (preds: Mapping[str, pd.Series], target: pd.Series, baseline_models: Sequence[str], candidate_models: Sequence[str] | None = None, *, periods: int, ic_method: Literal["pearson", "spearman"] = "spearman", group_level: str = "dt", block_size: int = 5, n_bootstrap: int = 1000, ci: float = 0.95, random_state: int | None = None,) -> pd.DataFrame |
| `compute_rolling_oos_metrics` | `src/alpha/core/formulas/model.py:1276` | Compute rolling-window IC/IR metrics (OOS-style stability diagnostics). | Input: (preds: Mapping[str, pd.Series], target: pd.Series, models: Sequence[str], *, periods: int, rolling_window: int = 63, min_periods: int | None = None, ic_method: Literal["pearson", "spearman"] = "spearman", group_level: str = "dt",) -> pd.DataFrame |
| `compute_cost_capacity_table` | `src/alpha/core/formulas/model.py:1340` | Compute per-model cost-adjusted IR and simple turnover-capacity diagnostics. | Input: (preds: Mapping[str, pd.Series], target: pd.Series, models: Sequence[str], *, periods: int, n_quantiles: int = 5, cost_per_turnover: float = 0.0, turnover_limit: float | None = None, ic_method: Literal["pearson", "spearman"] = "spearman", group_level: str = "dt", ticker_level: str = "ticker",) -> pd.DataFrame |
| `build_trend_vol_regime_mapping` | `src/alpha/core/formulas/model.py:1464` | Map each panel group label to a trend-volatility regime label. | Input: (market_df: pd.DataFrame, target: pd.Series, *, group_level: str = "dt", date_col: str = "date", price_col: str = "close", trend_window: int = 60, tau: float = 2.0, vol_window: int = 20, smooth: bool = True, min_duration: int = 5,) -> pd.Series |
| `generate_regime_table_by_model` | `src/alpha/core/formulas/model.py:1497` | Generate regime-split IC and long-short summary table by model. | Input: (models: Sequence[str], preds: Mapping[str, pd.Series], target: pd.Series, dt_to_regime: pd.Series, *, periods: int, ic_method: Literal["pearson", "spearman"] = "spearman", group_level: str = "dt", n_quantiles: int = 5,) -> pd.DataFrame |

### `src/alpha/core/formulas/oos.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_walk_forward_ic` | `src/alpha/core/formulas/oos.py:11` | Walk-forward grouped IC series. | Input: (factor: pd.Series, target: pd.Series, *, group_level: str = "dt", method: Literal["pearson", "spearman"] = "spearman",) -> pd.Series |
| `compute_sign_flip_count` | `src/alpha/core/formulas/oos.py:40` | Count direction flips in IC time series. | Input: (ic_series: pd.Series) -> int |
| `compute_adversarial_shift_score` | `src/alpha/core/formulas/oos.py:55` | Distribution-shift proxy in [0,1] based on standardized mean gap. | Input: (train_scores: pd.Series, test_scores: pd.Series) -> float |
| `compute_cpcv_consistency` | `src/alpha/core/formulas/oos.py:74` | Lightweight CPCV-style consistency proxy from sign agreement across folds. | Input: (ic_series: pd.Series, *, min_splits: int = 3,) -> float |
| `summarize_oos_survival` | `src/alpha/core/formulas/oos.py:95` | Composite OOS survival summary. | Input: (walk_forward_ic: pd.Series, *, adversarial_shift_score: float,) -> pd.DataFrame |

### `src/alpha/core/formulas/orthogonal.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_orthogonal_residual` | `src/alpha/core/formulas/orthogonal.py:60` | Residualize a candidate factor against known factors within each group. | Input: (new_factor: pd.Series, known_factors: pd.DataFrame | dict[str, pd.Series], *, groups: Optional[pd.Series] = None, group_level: Optional[str] = None, add_intercept: bool = True,) -> pd.Series |
| `compute_residual_ic` | `src/alpha/core/formulas/orthogonal.py:94` | Compute grouped IC for an orthogonalized factor residual. | Input: (residual_factor: pd.Series, target: pd.Series, *, groups: Optional[pd.Series] = None, group_level: Optional[str] = None, method: Literal["pearson", "spearman"] = "spearman",) -> pd.Series |
| `compute_residual_spread` | `src/alpha/core/formulas/orthogonal.py:114` | Compute per-group quantile spread on residual factor (top minus bottom quantile mean target). | Input: (residual_factor: pd.Series, target: pd.Series, *, groups: Optional[pd.Series] = None, group_level: Optional[str] = None, n_quantiles: int = 5,) -> pd.Series |
| `summarize_orthogonal` | `src/alpha/core/formulas/orthogonal.py:160` | Build a one-row orthogonalization summary with residual IC/spread and uniqueness score. | Input: (new_factor: pd.Series, known_factors: pd.DataFrame | dict[str, pd.Series], target: pd.Series, *, groups: Optional[pd.Series] = None, group_level: Optional[str] = None, method: Literal["pearson", "spearman"] = "spearman", n_quantiles: int = 5,) -> pd.DataFrame |

### `src/alpha/core/formulas/portfolio.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_long_short_constituents` | `src/alpha/core/formulas/portfolio.py:28` | Export long/short constituents by group as a tidy table. | Input: (factor: pd.Series, groups: Optional[pd.Series] = None, group_level: Optional[str] = None, ticker_level: str = "ticker", n_quantiles: int = 5, weights: Optional[pd.Series] = None,) -> pd.DataFrame |
| `compute_long_short_turnover` | `src/alpha/core/formulas/portfolio.py:115` | Compute long/short membership turnover between consecutive groups. | Input: (factor: pd.Series, groups: Optional[pd.Series] = None, group_level: Optional[str] = None, ticker_level: str = "ticker", n_quantiles: int = 5,) -> pd.DataFrame |

### `src/alpha/core/formulas/redundancy.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_factor_rank_corr_matrix` | `src/alpha/core/formulas/redundancy.py:50` | Compute pairwise Spearman correlation matrix across factor columns. | Input: (factors: pd.DataFrame | dict[str, pd.Series], *, factor_names: Sequence[str] | None = None, group_level: str | None = "dt", ticker_level: str = "ticker", min_obs_per_group: int = 2,) -> pd.DataFrame |
| `compute_n_effective_eigenvalue` | `src/alpha/core/formulas/redundancy.py:100` | Compute effective number of factors from correlation eigen-spectrum. | Input: (corr_matrix: pd.DataFrame | np.ndarray, *, clip_negative_eigenvalues: bool = True,) -> float |
| `compute_factor_clusters` | `src/alpha/core/formulas/redundancy.py:133` | Cluster factors using hierarchical clustering on distance = 1 - |corr|. | Input: (corr_matrix: pd.DataFrame | np.ndarray, *, threshold: float = 0.7, method: str = "average",) -> pd.Series |
| `compute_n_effective_cluster` | `src/alpha/core/formulas/redundancy.py:173` | Effective factor count from cluster labels (number of unique clusters). | Input: (cluster_labels: pd.Series | Sequence[int]) -> float |
| `summarize_redundancy` | `src/alpha/core/formulas/redundancy.py:183` | Per-factor redundancy summary with representative/variant/redundant labels. | Input: (corr_matrix: pd.DataFrame | np.ndarray, cluster_labels: pd.Series | Sequence[int], *, redundancy_threshold: float = 0.8,) -> pd.DataFrame |

### `src/alpha/core/formulas/regime.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `map_trend_labels` | `src/alpha/core/formulas/regime.py:145` | No docstring; see implementation. | Input: (regimes: pd.Series) -> pd.Series |
| `map_ternary_labels` | `src/alpha/core/formulas/regime.py:149` | No docstring; see implementation. | Input: (regimes: pd.Series) -> pd.Series |
| `map_binary_vol_labels` | `src/alpha/core/formulas/regime.py:153` | No docstring; see implementation. | Input: (regimes: pd.Series) -> pd.Series |
| `detect_trend_regime` | `src/alpha/core/formulas/regime.py:159` | Detect trend regime using integer codes: | Input: (prices: pd.Series, fast_window: int = 20, slow_window: int = 60, threshold: float = 0.02, method: str = "moving_average",) -> pd.Series |
| `detect_trend_tstat_regime` | `src/alpha/core/formulas/regime.py:265` | Detect trend regime from rolling linear-slope t-statistics. | Input: (prices: pd.Series, window: int = 60, tau: float = 2.0, min_periods: Optional[int] = None, use_log: bool = True,) -> pd.Series |
| `detect_binary_volatility_regime` | `src/alpha/core/formulas/regime.py:299` | Binary volatility regime: | Input: (volatility: pd.Series, threshold: Optional[float] = None, quantile: float = 0.5, threshold_window: Optional[int] = None,) -> pd.Series |
| `detect_volatility_regime` | `src/alpha/core/formulas/regime.py:344` | Ternary volatility regime: | Input: (returns: pd.Series, window: int = 20, high_threshold: Optional[float] = None, low_threshold: Optional[float] = None, high_quantile: float = 0.67, low_quantile: float = 0.33, threshold_window: Optional[int] = None,) -> pd.Series |
| `detect_liquidity_regime` | `src/alpha/core/formulas/regime.py:412` | Ternary liquidity regime: | Input: (volume: pd.Series, window: int = 20, high_quantile: float = 0.75, low_quantile: float = 0.25,) -> pd.Series |
| `smooth_regime` | `src/alpha/core/formulas/regime.py:448` | Smooth regime series by replacing short consecutive blocks using vectorized operations. | Input: (regimes: pd.Series, min_duration: int = 5) -> pd.Series |
| `combine_regimes` | `src/alpha/core/formulas/regime.py:494` | Combine multiple regime series into one composite string series. | Input: (*regime_series: pd.Series, separator: str = "_", label_maps: Optional[Sequence[Optional[Dict[int, str]]]] = None, na_value: Optional[str] = None, require_all_valid: bool = True,) -> pd.Series |
| `compute_regime_statistics` | `src/alpha/core/formulas/regime.py:571` | Compute summary statistics by regime. | Input: (regimes: pd.Series, returns: Optional[pd.Series] = None, periods_per_year: Optional[int] = None, risk_free_rate: float = 0.0, include_missing: bool = False,) -> pd.DataFrame |
| `tag_regimes` | `src/alpha/core/formulas/regime.py:674` | Generic regime tagging pipeline. | Input: (prices: pd.Series, returns: Optional[pd.Series] = None, volume: Optional[pd.Series] = None, trend_method: str = "moving_average", volatility_method: str = "ternary", trend_params: Optional[Dict[str, Any]] = None, volatility_params: Optional[Dict[str, Any]] = None, liquidity_params: Optional[Dict[str, Any]] = None, smooth: bool = True, min_duration: int = 5, add_label_columns: bool = False, add_composite_label: bool = False,) -> pd.DataFrame |
| `tag_trend_vol_regime` | `src/alpha/core/formulas/regime.py:837` | High-level trend/volatility regime tagging for OHLCV-like data. | Input: (ohlcva: pd.DataFrame, date_col: str = "date", price_col: str = "close", trend_window: int = 60, tau: float = 2.0, vol_window: int = 20, smooth: bool = True, min_duration: int = 5,) -> pd.DataFrame |

### `src/alpha/core/formulas/review.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_ic_drift` | `src/alpha/core/formulas/review.py:30` | Recent IC mean minus baseline IC mean. | Input: (ic_series: pd.Series, *, baseline_window: int = 60, recent_window: int = 20,) -> float |
| `compute_return_decay` | `src/alpha/core/formulas/review.py:49` | Relative decay = 1 - recent_mean / baseline_mean. | Input: (alpha_series: pd.Series, *, baseline_window: int = 60, recent_window: int = 20,) -> float |
| `compute_pool_correlation_drift` | `src/alpha/core/formulas/review.py:72` | Mean absolute change in factor-to-pool correlation. | Input: (recent_corr_to_pool: pd.Series, baseline_corr_to_pool: pd.Series,) -> float |
| `compute_review_health_score` | `src/alpha/core/formulas/review.py:86` | Composite health score in [0, 1], where higher is healthier. | Input: (*, ic_drift: float, return_decay: float, pool_corr_drift: float, w_ic: float = 0.4, w_decay: float = 0.3, w_corr: float = 0.3,) -> float |
| `compute_review_flags` | `src/alpha/core/formulas/review.py:116` | Flag list + recommendation from review diagnostics. | Input: (*, review_health_score: float, ic_drift: float, return_decay: float, pool_corr_drift: float,) -> dict[str, object] |

### `src/alpha/core/formulas/risk.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `compute_sector_exposure` | `src/alpha/core/formulas/risk.py:14` | Calculate sector exposure for top pred | Input: (pred: np.ndarray, sectors: np.ndarray, top_pct: float = 0.2) -> Dict[str, float] |
| `summarize_drawdown_stats` | `src/alpha/core/formulas/risk.py:46` | Summarize drawdown-related statistics from a return series. | Input: (returns: pd.Series) -> dict |

### `src/alpha/core/formulas/shared.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `timer` | `src/alpha/core/formulas/shared.py:8` | A decorator that prints the execution time of the function. | Input: (func) |
| `validate_required_columns` | `src/alpha/core/formulas/shared.py:28` | No docstring; see implementation. | Input: (df: pd.DataFrame, columns: Sequence[str]) -> None |
| `align_series` | `src/alpha/core/formulas/shared.py:34` | Align factor and target series, removing NaN values. | Input: (factor: pd.Series, target: pd.Series,) -> Tuple[pd.Series, pd.Series] |
| `infer_groups` | `src/alpha/core/formulas/shared.py:56` | Infer group labels from index or provided groups. | Input: (index: pd.Index, groups: Optional[pd.Series] = None, group_level: Optional[str] = None,) -> pd.Series |
| `infer_tickers` | `src/alpha/core/formulas/shared.py:84` | No docstring; see implementation. | Input: (index: pd.Index, ticker_level: Optional[str] = "ticker",) -> pd.Series |
| `aggregate_series_to_matrix` | `src/alpha/core/formulas/shared.py:100` | Aggregate a Jaccard time series dict into an NxN matrix for a single statistic. | Input: (series: Dict[Tuple[str, str], List[float]], models: List[str], stat: str,) -> pd.DataFrame |
| `parse_horizon_days` | `src/alpha/core/formulas/shared.py:135` | Extract horizon in days from a model name. | Input: (model_name: str) -> int |
| `regime_mapping` | `src/alpha/core/formulas/shared.py:153` | Map intraday timestamps to regime labels based on trading date. | Input: (regime: pd.Series, targets: pd.DataFrame, level: str = 'dt') |
| `extract_price_series` | `src/alpha/core/formulas/shared.py:184` | No docstring; see implementation. | Input: (ohlcva: pd.DataFrame, price_col: str, date_col: Optional[str], sort_index: bool) -> pd.Series |
| `ensure_panel_series_index` | `src/alpha/core/formulas/shared.py:205` | Normalize a panel-like Series to a 2-level MultiIndex with standardized level names. | Input: (series: pd.Series, group_level: str = "dt", entity_level: str = "ticker",) -> pd.Series |
| `build_panel_wide_frame` | `src/alpha/core/formulas/shared.py:307` | Concatenate multiple panel Series into a wide DataFrame with a standardized 2-level index. | Input: (series_by_name: Dict[str, pd.Series], names: Sequence[str], group_level: str = "dt", entity_level: str = "ticker", column_name: str = "model",) -> pd.DataFrame |

## Pipeline

### `src/alpha/pipeline/analysis/_utils.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `resolve_interface` | `src/alpha/pipeline/analysis/_utils.py:9` | No docstring; see implementation. | Input: (interface: Interface | None) -> Interface |
| `resolve_trading_times` | `src/alpha/pipeline/analysis/_utils.py:15` | No docstring; see implementation. | Input: (configured_trading_times: Sequence[str] | None, calendar_trading_times: Sequence[str],) -> tuple[str, ...] |
| `resolve_periods_per_year` | `src/alpha/pipeline/analysis/_utils.py:22` | No docstring; see implementation. | Input: (periods_per_year: int | None, trading_times: Sequence[str],) -> int |
| `resolve_analysis_names` | `src/alpha/pipeline/analysis/_utils.py:33` | No docstring; see implementation. | Input: (available_names: Sequence[str], names: Sequence[str] | None, *, dedupe: bool = False, missing_message_prefix: str = "Unknown names",) -> list[str] |

### `src/alpha/pipeline/analysis/diag.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `DistributionConfig` | `src/alpha/pipeline/analysis/diag.py:25` | No docstring; see implementation. | Class |
| `DistributionInputs` | `src/alpha/pipeline/analysis/diag.py:41` | No docstring; see implementation. | Class |
| `DistributionContext` | `src/alpha/pipeline/analysis/diag.py:47` | No docstring; see implementation. | Class |
| `load_distribution_inputs` | `src/alpha/pipeline/analysis/diag.py:58` | Load raw in-memory data for diagnostics analysis. | Input: (*, y: pd.Series | None = None, df: pd.DataFrame | None = None,) -> DistributionInputs |
| `prepare_distribution_context` | `src/alpha/pipeline/analysis/diag.py:78` | Build a reusable diagnostics context. | Input: (config: DistributionConfig, inputs: DistributionInputs,) -> DistributionContext |
| `analyze_distribution_basic` | `src/alpha/pipeline/analysis/diag.py:167` | Compute basic univariate statistics from context. | Input: (ctx: DistributionContext) -> Dict[str, Any] |
| `analyze_distribution_tail_outliers` | `src/alpha/pipeline/analysis/diag.py:175` | Compute empirical tail outlier rates from context. | Input: (ctx: DistributionContext) -> Dict[str, float] |
| `analyze_distribution_normality` | `src/alpha/pipeline/analysis/diag.py:183` | Run normality tests from context. | Input: (ctx: DistributionContext) -> Dict[str, Dict[str, Any]] |
| `analyze_distribution_fit` | `src/alpha/pipeline/analysis/diag.py:191` | Fit candidate parametric distributions from context. | Input: (ctx: DistributionContext) -> Dict[str, Dict[str, Any]] |
| `analyze_distribution_stationarity` | `src/alpha/pipeline/analysis/diag.py:199` | Run ADF stationarity test from context. | Input: (ctx: DistributionContext) -> Dict[str, Any] |
| `analyze_distribution_autocorr` | `src/alpha/pipeline/analysis/diag.py:207` | Compute autocorrelation table from context. | Input: (ctx: DistributionContext) -> pd.DataFrame |
| `analyze_heteroscedasticity_group_stats` | `src/alpha/pipeline/analysis/diag.py:215` | Compute grouped dispersion tables and variance-ratio summaries. | Input: (ctx: DistributionContext,) -> Tuple[Dict[str, Any], pd.DataFrame, pd.DataFrame, pd.DataFrame] |
| `analyze_heteroscedasticity_levene` | `src/alpha/pipeline/analysis/diag.py:249` | Run Levene test across asset std buckets when feasible. | Input: (ctx: DistributionContext) -> Dict[str, Any] |

### `src/alpha/pipeline/analysis/factor.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `FactorBatchInputs` | `src/alpha/pipeline/analysis/factor.py:41` | No docstring; see implementation. | Class |
| `FactorAnalysisContext` | `src/alpha/pipeline/analysis/factor.py:51` | Reusable in-memory context for batch factor analysis. | Class |
| `FactorPortfolioLegResult` | `src/alpha/pipeline/analysis/factor.py:65` | No docstring; see implementation. | Class |
| `FactorBatchAnalysisConfig` | `src/alpha/pipeline/analysis/factor.py:75` | Runtime config for batch factor analysis (multi-factor orchestration layer). | Class |
| `FactorBatchAnalysisResult` | `src/alpha/pipeline/analysis/factor.py:101` | No docstring; see implementation. | Class |
| `load_factor_batch_inputs` | `src/alpha/pipeline/analysis/factor.py:327` | Load shared inputs once for multi-factor batch analysis. | Input: (config: FactorBatchAnalysisConfig, *, factor_names: Sequence[str] | None = None, interface: Interface | None = None,) -> FactorBatchInputs |
| `prepare_factor_context` | `src/alpha/pipeline/analysis/factor.py:416` | Build reusable per-factor series and IC artifacts for downstream analyzers. | Input: (config: FactorBatchAnalysisConfig, inputs: FactorBatchInputs,) -> FactorAnalysisContext |
| `analyze_factor_ic` | `src/alpha/pipeline/analysis/factor.py:485` | Compute IC summary metrics for selected factors in context. | Input: (ctx: FactorAnalysisContext, names: Sequence[str] | None = None,) -> pd.DataFrame |
| `analyze_factor_ic_decay` | `src/alpha/pipeline/analysis/factor.py:514` | Compute IC decay statistics by horizon for selected factors. | Input: (ctx: FactorAnalysisContext, names: Sequence[str] | None = None,) -> pd.DataFrame |
| `analyze_factor_portfolio` | `src/alpha/pipeline/analysis/factor.py:595` | Compute portfolio-leg outputs for selected factors. | Input: (ctx: FactorAnalysisContext, names: Sequence[str] | None = None,) -> dict[str, FactorPortfolioLegResult] |
| `analyze_factor_turnover` | `src/alpha/pipeline/analysis/factor.py:637` | Compute turnover summary table for selected factors. | Input: (ctx: FactorAnalysisContext, names: Sequence[str] | None = None,) -> pd.DataFrame |
| `analyze_factor_autocorr` | `src/alpha/pipeline/analysis/factor.py:648` | Compute rank autocorrelation series for selected factors. | Input: (ctx: FactorAnalysisContext, names: Sequence[str] | None = None,) -> dict[str, pd.Series] |
| `analyze_factor_summary` | `src/alpha/pipeline/analysis/factor.py:668` | Build factor-level summary table from IC, portfolio, and turnover analyses. | Input: (ctx: FactorAnalysisContext, names: Sequence[str] | None = None,) -> pd.DataFrame |
| `run_factor_batch` | `src/alpha/pipeline/analysis/factor.py:701` | Batch runner for multiple factors using load/context/analyze stages. | Input: (config: FactorBatchAnalysisConfig, *, interface: Interface | None = None,) -> FactorBatchAnalysisResult |

### `src/alpha/pipeline/analysis/factor.py` (funnel APIs)

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `FunnelConfig` | `src/alpha/pipeline/analysis/factor.py:53` | No docstring; see implementation. | Class |
| `FunnelInputs` | `src/alpha/pipeline/analysis/factor.py:74` | No docstring; see implementation. | Class |
| `FunnelContext` | `src/alpha/pipeline/analysis/factor.py:83` | No docstring; see implementation. | Class |
| `load_funnel_inputs` | `src/alpha/pipeline/analysis/factor.py:90` | Load funnel inputs from factor batch loader when an interface is provided. | Input: (config: FunnelConfig, interface: Interface | None = None) -> FunnelInputs |
| `prepare_funnel_context` | `src/alpha/pipeline/analysis/factor.py:120` | No docstring; see implementation. | Input: (config: FunnelConfig, inputs: FunnelInputs) -> FunnelContext |
| `analyze_funnel_screening` | `src/alpha/pipeline/analysis/factor.py:147` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_orthogonal` | `src/alpha/pipeline/analysis/factor.py:173` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_redundancy` | `src/alpha/pipeline/analysis/factor.py:218` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_multiplicity` | `src/alpha/pipeline/analysis/factor.py:262` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_selection_bias` | `src/alpha/pipeline/analysis/factor.py:308` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_bootstrap_null` | `src/alpha/pipeline/analysis/factor.py:312` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_threshold` | `src/alpha/pipeline/analysis/factor.py:316` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_oos` | `src/alpha/pipeline/analysis/factor.py:320` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_capacity` | `src/alpha/pipeline/analysis/factor.py:324` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_incremental` | `src/alpha/pipeline/analysis/factor.py:328` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_bayesian` | `src/alpha/pipeline/analysis/factor.py:332` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_review` | `src/alpha/pipeline/analysis/factor.py:371` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `analyze_funnel_tiers` | `src/alpha/pipeline/analysis/factor.py:432` | No docstring; see implementation. | Input: (ctx: FunnelContext) -> pd.DataFrame |
| `run_funnel` | `src/alpha/pipeline/analysis/factor.py:471` | No docstring; see implementation. | Input: (config: FunnelConfig, interface: Interface | None = None) -> list[FactorCard] |

### `src/alpha/pipeline/analysis/model.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `ModelAnalysisConfig` | `src/alpha/pipeline/analysis/model.py:45` | Runtime config for model analysis. | Class |
| `ModelAnalysisInputs` | `src/alpha/pipeline/analysis/model.py:83` | No docstring; see implementation. | Class |
| `ModelAnalysisContext` | `src/alpha/pipeline/analysis/model.py:93` | Reusable in-memory analysis context built from one input load. | Class |
| `prepare_context` | `src/alpha/pipeline/analysis/model.py:189` | Build reusable predictions and IC artifacts from loaded inputs. | Input: (config: ModelAnalysisConfig, inputs: ModelAnalysisInputs,) -> ModelAnalysisContext |
| `load_analysis_inputs` | `src/alpha/pipeline/analysis/model.py:271` | Load sessions, models, features, target, and multi-horizon targets. | Input: (config: ModelAnalysisConfig, interface: Interface | None = None,) -> ModelAnalysisInputs |
| `generate_predictions` | `src/alpha/pipeline/analysis/model.py:346` | Generate model predictions for the given feature panel. | Input: (models: Mapping[str, BaseFactorModel], features: pd.DataFrame, *, model_names: Sequence[str] | None = None,) -> dict[str, pd.Series] |
| `analyze_quality` | `src/alpha/pipeline/analysis/model.py:449` | Compute quality metrics for selected prediction series. | Input: (ctx: ModelAnalysisContext, names: Sequence[str] | None = None,) -> pd.DataFrame |
| `analyze_stability` | `src/alpha/pipeline/analysis/model.py:468` | Compute stability and tail-risk metrics for selected prediction series. | Input: (ctx: ModelAnalysisContext, names: Sequence[str] | None = None,) -> pd.DataFrame |
| `analyze_pairwise` | `src/alpha/pipeline/analysis/model.py:486` | Compute pairwise prediction, top-k overlap, and error-correlation summaries. | Input: (ctx: ModelAnalysisContext, names: Sequence[str] | None = None,) -> dict[str, dict[str, pd.DataFrame]] |
| `analyze_ic_decay` | `src/alpha/pipeline/analysis/model.py:533` | Compute IC decay metrics for selected prediction series. | Input: (ctx: ModelAnalysisContext, names: Sequence[str] | None = None,) -> pd.DataFrame |
| `analyze_contribution` | `src/alpha/pipeline/analysis/model.py:551` | Compute single-model IR and leave-one-out contribution for selected names. | Input: (ctx: ModelAnalysisContext, names: Sequence[str] | None = None,) -> dict[str, pd.DataFrame] |
| `analyze_incremental` | `src/alpha/pipeline/analysis/model.py:579` | Compute baseline-vs-candidate incremental statistics on selected names. | Input: (ctx: ModelAnalysisContext, *, baseline: Sequence[str], candidates: Sequence[str] | None = None,) -> dict[str, pd.DataFrame] |
| `analyze_block_marginal_gain` | `src/alpha/pipeline/analysis/model.py:643` | Compute per-model marginal gain inside each block via leave-one-out IR diagnostics. | Input: (ctx: ModelAnalysisContext, names: Sequence[str] | None = None, *, block_model_map: Mapping[str, Sequence[str]] | None = None,) -> pd.DataFrame |
| `analyze_block_incremental_gain` | `src/alpha/pipeline/analysis/model.py:681` | Compute candidate incremental gain for each block baseline. | Input: (ctx: ModelAnalysisContext, names: Sequence[str] | None = None, *, block_model_map: Mapping[str, Sequence[str]] | None = None, candidate_pool: Sequence[str] | None = None,) -> pd.DataFrame |
| `analyze_regime` | `src/alpha/pipeline/analysis/model.py:756` | Compute regime mapping and regime-split performance table. | Input: (ctx: ModelAnalysisContext, names: Sequence[str], market_df: pd.DataFrame, *, date_col: str = "date", price_col: str = "close", trend_window: int = 60, tau: float = 2.0, vol_window: int = 20, smooth: bool = True, min_duration: int = 5,) -> dict[str, Any] |
| `analyze_rolling_oos` | `src/alpha/pipeline/analysis/model.py:801` | Compute rolling-window out-of-sample diagnostics for selected names. | Input: (ctx: ModelAnalysisContext, names: Sequence[str] | None = None,) -> pd.DataFrame |
| `analyze_cost_capacity` | `src/alpha/pipeline/analysis/model.py:821` | Compute cost-capacity diagnostics for selected names. | Input: (ctx: ModelAnalysisContext, names: Sequence[str] | None = None,) -> pd.DataFrame |

## Interface

### `src/alpha/core/interface/calendar.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `Calendar` | `src/alpha/core/interface/calendar.py:7` | Trading/session calendar abstraction. | Class |
| `Calendar.sessions_between` | `src/alpha/core/interface/calendar.py:19` | Return sessions in [start, end], inclusive, sorted ascending. | Input: (self, start: str, end: str) -> list[str] |
| `Calendar.sessions_ending_at` | `src/alpha/core/interface/calendar.py:24` | Return the last `count` sessions ending at `end` (inclusive), sorted ascending. | Input: (self, end: str, count: int) -> list[str] |
| `Calendar.shift_session` | `src/alpha/core/interface/calendar.py:29` | Shift a session label by `offset` sessions. | Input: (self, session: str, offset: int) -> str |

### `src/alpha/core/interface/config.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `IndexSpec` | `src/alpha/core/interface/config.py:7` | Canonical index conventions for tables used across the project. | Class |
| `ColumnSpec` | `src/alpha/core/interface/config.py:28` | Canonical column conventions for tables used across the project. | Class |
| `DatasetSpec` | `src/alpha/core/interface/config.py:37` | Schema bundle used by interface to describe returned table shapes. | Class |
| `ParallelSpec` | `src/alpha/core/interface/config.py:47` | Cross-backend parallelism defaults for loaders/builders. | Class |

### `src/alpha/core/interface/interface.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `Interface` | `src/alpha/core/interface/interface.py:11` | Pipeline interface contract. | Class |

### `src/alpha/core/interface/loader.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `Loader` | `src/alpha/core/interface/loader.py:11` | Interface-agnostic dataset loader. | Class |
| `Loader.load_features` | `src/alpha/core/interface/loader.py:27` | Load feature tensors for the requested sessions. | Input: (self, target_sessions: Sequence[str], feature_names: Sequence[str],) -> pd.DataFrame |
| `Loader.load_target` | `src/alpha/core/interface/loader.py:46` | Load a single-horizon target for the given sessions. | Input: (self, target_sessions: Sequence[str], *, horizon: str,) -> pd.DataFrame |
| `Loader.load_targets` | `src/alpha/core/interface/loader.py:72` | Load multi-horizon targets for the given sessions. | Input: (self, target_sessions: Sequence[str], *, horizon: list[int],) -> pd.DataFrame |
| `Loader.load_dataset` | `src/alpha/core/interface/loader.py:101` | Convenience method: load an aligned feature+target dataset. | Input: (self, target_sessions: Sequence[str], feature_names: Sequence[str], *, horizon: str,) -> pd.DataFrame |

### `src/alpha/core/interface/model.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `Model` | `src/alpha/core/interface/model.py:12` | Model loading and inference interface. | Class |
| `Model.structure` | `src/alpha/core/interface/model.py:30` | Return the architecture structure describing the available blocks/layers. | Input: (self) -> Dict |
| `Model.load_model` | `src/alpha/core/interface/model.py:35` | Load a single factor model from `path` and cache it for `pred()`. | Input: (self, path: str | Path | None, *, name: str | None = None) -> BaseFactorModel |
| `Model.load_models` | `src/alpha/core/interface/model.py:42` | Load multiple factor models from `path` and cache them for `preds()`. | Input: (self, path: str | Path | None, *, names: list[str] | None = None) -> Dict[str, BaseFactorModel] |
| `Model.pred` | `src/alpha/core/interface/model.py:49` | Run inference with the single model cached by the last `load_model()` call. | Input: (self, features: pd.DataFrame) -> pd.Series |
| `Model.preds` | `src/alpha/core/interface/model.py:70` | Run inference with every model cached by the last `load_models()` call. | Input: (self, features: pd.DataFrame, names: list[str] | None = None) -> pd.DataFrame |

## Data

### `src/alpha/core/data/cv.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `CVStrategy` | `src/alpha/core/data/cv.py:10` | Base class for CV strategies | Class |
| `CVStrategy.split` | `src/alpha/core/data/cv.py:18` | Generate CV splits | Input: (self, groups: np.ndarray) -> Iterator[Tuple[np.ndarray, np.ndarray]] |
| `CVStrategy.get_group_sizes_for_fold` | `src/alpha/core/data/cv.py:31` | Get group_sizes for training and validation sets of a fold (for lambdarank) | Input: (self, groups: np.ndarray, train_idx: np.ndarray, valid_idx: np.ndarray) -> Tuple[List[int], List[int]] |
| `TimeKFoldStrategy` | `src/alpha/core/data/cv.py:48` | Time-based K-fold + embargo splitting strategy | Class |
| `TimeKFoldStrategy.split` | `src/alpha/core/data/cv.py:69` | Generate time-based K-fold splits | Input: (self, groups: np.ndarray) -> Iterator[Tuple[np.ndarray, np.ndarray]] |
| `TimeKFoldStrategy.get_group_sizes_for_fold` | `src/alpha/core/data/cv.py:120` | Get group_sizes for training and validation sets of a fold | Input: (self, groups: np.ndarray, train_idx: np.ndarray, valid_idx: np.ndarray) -> Tuple[List[int], List[int]] |
| `FixedTimeSplitStrategy` | `src/alpha/core/data/cv.py:143` | Fixed time-based split strategy with Purge + Embargo | Class |
| `FixedTimeSplitStrategy.split` | `src/alpha/core/data/cv.py:194` | Generate fixed time-based splits | Input: (self, groups: np.ndarray) -> Iterator[Tuple[np.ndarray, np.ndarray]] |
| `FixedTimeSplitStrategy.get_group_sizes_for_fold` | `src/alpha/core/data/cv.py:280` | Get group_sizes for training and validation/test sets | Input: (self, groups: np.ndarray, train_idx: np.ndarray, valid_idx: np.ndarray) -> Tuple[List[int], List[int]] |
| `FixedTimeSplitStrategy.get_split_info` | `src/alpha/core/data/cv.py:302` | Get detailed information about the split | Input: (self, groups: np.ndarray) -> dict |
| `CVManager` | `src/alpha/core/data/cv.py:350` | Time-based CV splitting manager with support for K-fold and fixed splits | Class |
| `CVManager.split` | `src/alpha/core/data/cv.py:419` | Generate time-based K-fold splits | Input: (self, groups: np.ndarray) -> Iterator[Tuple[np.ndarray, np.ndarray]] |
| `CVManager.get_group_sizes_for_fold` | `src/alpha/core/data/cv.py:432` | Get group_sizes for training and validation sets of a fold (for lambdarank) | Input: (self, groups: np.ndarray, train_idx: np.ndarray, valid_idx: np.ndarray) -> Tuple[List[int], List[int]] |
| `CVManager.get_split_info` | `src/alpha/core/data/cv.py:448` | Get detailed information about the split (only for fixed_split method) | Input: (self, groups: np.ndarray) -> Optional[dict] |

### `src/alpha/core/data/mock.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `generate_mock_dt_ticker_index` | `src/alpha/core/data/mock.py:38` | Convenience: MultiIndex product of dt and ticker. | Input: (dt_index: Sequence[str] | pd.Index, tickers: Sequence[str],) -> pd.MultiIndex |
| `generate_mock_tickers` | `src/alpha/core/data/mock.py:50` | Generate random (synthetic) ticker symbols. | Input: (n: int, *, min_len: int = 3, max_len: int = 5, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", seed: int | None = None, unique: bool = True,) -> list[str] |
| `generate_mock_dt_index` | `src/alpha/core/data/mock.py:99` | Create a dt index as strings in YYYYMMDDHHMMSS format. | Input: (start_dt: str, periods: int, freq: str = "1min",) -> pd.Index |
| `RandomSpec` | `src/alpha/core/data/mock.py:129` | Parameters for generating random returns/features. | Class |
| `generate_mock_features` | `src/alpha/core/data/mock.py:139` | Type 1: Features (long, multi-feature). | Input: (dt_index: Sequence[str] | pd.Index, tickers: Sequence[str], *, features: Sequence[str] | None = None, n_features: int | None = None, feature_prefix: str = "feature_", spec: RandomSpec = RandomSpec(mean=0.0, std=1.0, seed=None),) -> pd.DataFrame |
| `generate_mock_target` | `src/alpha/core/data/mock.py:182` | Type 2: Target (long). | Input: (dt_index: Sequence[str] | pd.Index, tickers: Sequence[str], *, name: str = "target", spec: RandomSpec = RandomSpec(mean=0.0, std=0.01, seed=None),) -> pd.DataFrame |
| `generate_mock_forward_returns` | `src/alpha/core/data/mock.py:209` | Type 3: Forward returns (long, multi-horizon). | Input: (dt_index: Sequence[str] | pd.Index, tickers: Sequence[str], *, steps: Sequence[int] = (1, 3, 5, 10), spec_1step: RandomSpec = RandomSpec(mean=0.0, std=0.01, seed=None), drop_tail_nan: bool = True,) -> pd.DataFrame |
| `iter_dt_strings_for_day` | `src/alpha/core/data/mock.py:266` | Build dt strings from a YYYYMMDD date and iterable of HHMMSS times. | Input: (date: str, times: Iterable[str],) -> list[str] |
| `MockLinearModel` | `src/alpha/core/data/mock.py:284` | Tiny linear model for notebook/debug workflows. | Class |
| `MockLinearModel.random` | `src/alpha/core/data/mock.py:311` | Build a deterministic random linear model. | Input: (cls, feature_names: Sequence[str], *, seed: int | None = None, weight_scale: float = 1.0, bias: float = 0.0,) -> "MockLinearModel" |
| `MockLinearModel.fit` | `src/alpha/core/data/mock.py:333` | Fit linear coefficients by least squares (with intercept). | Input: (cls, X: pd.DataFrame, y: pd.Series | pd.DataFrame, *, feature_names: Sequence[str] | None = None,) -> "MockLinearModel" |
| `MockLinearModel.predict` | `src/alpha/core/data/mock.py:369` | Predict from a row-like input, DataFrame, or keyword features. | Input: (self, row: pd.DataFrame | pd.Series | Mapping[str, float] | Sequence[float] | None = None, **feature_values: float,) -> float | pd.Series |
| `MockLinearModel.predict_frame` | `src/alpha/core/data/mock.py:387` | Vectorized predictions for a feature frame. | Input: (self, X: pd.DataFrame) -> pd.Series |
| `MockLinearModel.predict_row` | `src/alpha/core/data/mock.py:395` | Single-row prediction from Series/Mapping/sequence. | Input: (self, row: pd.Series | Mapping[str, float] | Sequence[float]) -> float |

### `src/alpha/core/data/preprocess.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `get_date_groups` | `src/alpha/core/data/preprocess.py:15` | Extract normalized trading-date grouping key from MultiIndex. | Input: (index, dt_level: str = "dt", dt_format: str = "%Y%m%d%H%M%S") |
| `add_intraday_time_columns` | `src/alpha/core/data/preprocess.py:52` | Add date and minute_of_day columns from a datetime column. | Input: (df: pd.DataFrame, dt_col: str = "datetime", copy: bool = True,) -> pd.DataFrame |
| `standardize_features` | `src/alpha/core/data/preprocess.py:89` | Standardize features | Input: (features: pd.DataFrame, method: str = 'zscore', axis: int = 0, clip: Optional[float] = None) -> pd.DataFrame |
| `standardize_by_date` | `src/alpha/core/data/preprocess.py:137` | Z-score target within each trading date. | Input: (df, target_col: str = "target", dt_level: str = "dt", dt_format: str = "%Y%m%d%H%M%S", eps: float = 1e-12) |
| `cross_sectional_standardize` | `src/alpha/core/data/preprocess.py:163` | Standardize data cross-sectionally (across assets at each time point) | Input: (data: pd.DataFrame, method: str = 'zscore', clip: Optional[float] = None) -> pd.DataFrame |
| `winsorize` | `src/alpha/core/data/preprocess.py:184` | Winsorize data by clipping extreme values | Input: (data: pd.DataFrame, lower: float = 0.01, upper: float = 0.99) -> pd.DataFrame |
| `handle_missing_values` | `src/alpha/core/data/preprocess.py:206` | Handle missing values in data | Input: (data: pd.DataFrame, method: str = 'drop', fill_value: Optional[Union[float, str]] = None, threshold: Optional[float] = None) -> pd.DataFrame |

## Integration

### `src/alpha/integration/aixi/calendar.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `AixiCalendar` | `src/alpha/integration/aixi/calendar.py:11` | AIXI calendar adapter that implements the generic Calendar contract. | Class |
| `AixiCalendar.sessions_between` | `src/alpha/integration/aixi/calendar.py:20` | No docstring; see implementation. | Input: (self, start: str, end: str) -> list[str] |
| `AixiCalendar.sessions_ending_at` | `src/alpha/integration/aixi/calendar.py:23` | No docstring; see implementation. | Input: (self, end: str, count: int) -> list[str] |
| `AixiCalendar.shift_session` | `src/alpha/integration/aixi/calendar.py:26` | No docstring; see implementation. | Input: (self, session: str, offset: int) -> str |

### `src/alpha/integration/aixi/common/func.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `load_pretd` | `src/alpha/integration/aixi/common/func.py:5` | No docstring; see implementation. | Input: (dt, lag=0) |
| `load_psttd` | `src/alpha/integration/aixi/common/func.py:12` | No docstring; see implementation. | Input: (dt, lag=0) |
| `load_tdates` | `src/alpha/integration/aixi/common/func.py:19` | No docstring; see implementation. | Input: (start=None, end=None) |
| `proc_ticker` | `src/alpha/integration/aixi/common/func.py:37` | No docstring; see implementation. | Input: (ticker) |

### `src/alpha/integration/aixi/common/settings.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `load_td` | `src/alpha/integration/aixi/common/settings.py:18` | No docstring; see implementation. | Input: () |

### `src/alpha/integration/aixi/interface.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `load_legacy_modules` | `src/alpha/integration/aixi/interface.py:13` | No docstring; see implementation. | Input: () |
| `AixiInterface` | `src/alpha/integration/aixi/interface.py:19` | AIXI backend implementation of the core Interface contract. | Class |
| `create_backend` | `src/alpha/integration/aixi/interface.py:32` | Convenience factory for callers that want a simple default backend instance. | Input: () -> AixiInterface |

### `src/alpha/integration/aixi/loader.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `AixiLoader` | `src/alpha/integration/aixi/loader.py:14` | AIXI dataset loader adapter around the legacy `DataBuilder`. | Class |
| `AixiLoader.load_features` | `src/alpha/integration/aixi/loader.py:28` | No docstring; see implementation. | Input: (self, target_sessions: Sequence[str], feature_names: Sequence[str],) -> pd.DataFrame |
| `AixiLoader.load_target` | `src/alpha/integration/aixi/loader.py:41` | No docstring; see implementation. | Input: (self, target_sessions: Sequence[str], *, horizon: str,) -> pd.DataFrame |
| `AixiLoader.load_targets` | `src/alpha/integration/aixi/loader.py:60` | Load targets for multiple horizons [1, 3, 5, 10, 15, 20]. | Input: (self, target_sessions: Sequence[str], *, horizon: list[int],) -> pd.DataFrame |
| `AixiLoader.load_dataset` | `src/alpha/integration/aixi/loader.py:72` | No docstring; see implementation. | Input: (self, target_sessions: Sequence[str], feature_names: Sequence[str], *, horizon: str,) -> pd.DataFrame |

### `src/alpha/integration/aixi/model.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `AixiModel` | `src/alpha/integration/aixi/model.py:15` | AIXI model store adapter. | Class |
| `AixiModel.structure` | `src/alpha/integration/aixi/model.py:43` | No docstring; see implementation. | Input: (self) -> Dict |
| `AixiModel.load_model` | `src/alpha/integration/aixi/model.py:54` | Load a single factor model and cache it for ``pred()``. | Input: (self, path: str | Path | None = MODEL_TEMPLATE_PATH, *, name: str | None = None,) -> BaseFactorModel |
| `AixiModel.load_models` | `src/alpha/integration/aixi/model.py:65` | Load multiple factor models and cache them for ``preds()``. | Input: (self, path: str | Path | None = MODEL_TEMPLATE_PATH, *, names: list[str] | None = BLOCK_NAMES,) -> Dict[str, BaseFactorModel] |
| `AixiModel.pred` | `src/alpha/integration/aixi/model.py:80` | Predict with the model cached by ``load_model()``. | Input: (self, features: pd.DataFrame) -> pd.Series |
| `AixiModel.preds` | `src/alpha/integration/aixi/model.py:93` | Predict with every model cached by ``load_models()``. | Input: (self, features: pd.DataFrame, names: list[str] | None = None) -> pd.DataFrame |

### `src/alpha/integration/aixi/signals/signals.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `Model` | `src/alpha/integration/aixi/signals/signals.py:9` | Base model class (abstract class) | Class |
| `Model.predict` | `src/alpha/integration/aixi/signals/signals.py:25` | Use model for prediction (abstract method) | Input: (self, terms: pd.DataFrame) -> pd.Series |
| `LightGBM` | `src/alpha/integration/aixi/signals/signals.py:41` | LightGBM model wrapper class | Class |
| `LightGBM.predict` | `src/alpha/integration/aixi/signals/signals.py:48` | Use LightGBM model for prediction | Input: (self, terms: pd.DataFrame) -> pd.Series |

### `src/alpha/integration/aixi/sources/config.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `load_td` | `src/alpha/integration/aixi/sources/config.py:127` | No docstring; see implementation. | Input: () |
| `get_block_models` | `src/alpha/integration/aixi/sources/config.py:150` | Get list of models in a block | Input: (block_name: str) -> List[str] |
| `get_ensemble_weights` | `src/alpha/integration/aixi/sources/config.py:163` | Get ensemble weights for a specific ensemble | Input: (layer: int, ensemble_name: str) -> Dict[str, float] |
| `get_trading_time_points` | `src/alpha/integration/aixi/sources/config.py:184` | Get list of trading time points | Input: () -> List[str] |
| `is_trading_time` | `src/alpha/integration/aixi/sources/config.py:194` | Check if a time string is a valid trading time point | Input: (time_str: str) -> bool |
| `load_pretd` | `src/alpha/integration/aixi/sources/config.py:209` | No docstring; see implementation. | Input: (dt, lag=0) |
| `load_psttd` | `src/alpha/integration/aixi/sources/config.py:216` | No docstring; see implementation. | Input: (dt, lag=0) |
| `load_tdates` | `src/alpha/integration/aixi/sources/config.py:223` | No docstring; see implementation. | Input: (start=None, end=None) |
| `proc_ticker` | `src/alpha/integration/aixi/sources/config.py:241` | No docstring; see implementation. | Input: (ticker) |
| `load_factor_model` | `src/alpha/integration/aixi/sources/config.py:257` | Load a factor model from disk and coerce it into a BaseFactorModel. | Input: (path: Union[str, Path], *, name: Optional[str] = None,) -> BaseFactorModel |
| `load_models` | `src/alpha/integration/aixi/sources/config.py:288` | No docstring; see implementation. | Input: (path: str, block_names: List[str]) |
| `load_by_blocks` | `src/alpha/integration/aixi/sources/config.py:311` | No docstring; see implementation. | Input: (models: Dict = None, path: str = None, block_names: List[str] = None) |

### `src/alpha/integration/aixi/sources/data.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `DataBuilder` | `src/alpha/integration/aixi/sources/data.py:335` | Data builder: unified and decoupled data loading interface (pandas-only). | Class |
| `DataBuilder.load_features` | `src/alpha/integration/aixi/sources/data.py:499` | Load features only (X) | Input: (self, dates: List[str], terms: List[str], y_horizon: Optional[str] = None, use_feature_dates: bool = True, format: Literal['tuple', 'dataframe'] = 'dataframe') -> Union[Tuple[np.ndarray, np.ndarray, List[int]], pd.DataFrame] |
| `DataBuilder.load_target` | `src/alpha/integration/aixi/sources/data.py:531` | Load targets only (y) for a single horizon. | Input: (self, y_dates: List[str], y_horizon: str, format: Literal['tuple', 'dataframe'] = 'dataframe') -> Union[Tuple[np.ndarray, np.ndarray, List[int]], pd.DataFrame] |
| `DataBuilder.load_targets` | `src/alpha/integration/aixi/sources/data.py:549` | Load targets for multiple horizons. | Input: (self, y_dates: List[str], horizons: Optional[List[int]] = None, format: Literal['dataframe'] = 'dataframe') -> pd.DataFrame |
| `DataBuilder.build` | `src/alpha/integration/aixi/sources/data.py:570` | Build training data with aligned features and targets | Input: (self, y_dates: List[str], terms: List[str], y_horizon: str, format: Literal['tuple', 'dataframe'] = 'tuple') -> Union[Tuple[np.ndarray, np.ndarray, np.ndarray, List[int]], pd.DataFrame] |
| `DataBuilder.build_with_fixed_split` | `src/alpha/integration/aixi/sources/data.py:594` | Build training data with fixed train/valid/test split | Input: (self, y_dates: List[str], terms: List[str], y_horizon: str, embargo: int = 5, train_ratio: float = 0.7, valid_ratio: float = 0.15, test_ratio: float = 0.15, use_three_way_split: bool = True) -> Dict |

### `src/alpha/integration/aixi/sources/prod.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `task` | `src/alpha/integration/aixi/sources/prod.py:8` | No docstring; see implementation. | Input: (y_dt, terms, y_horizon, output) |
| `load_obs` | `src/alpha/integration/aixi/sources/prod.py:31` | No docstring; see implementation. | Input: (y_dates, terms, y_horizon) |
| `main` | `src/alpha/integration/aixi/sources/prod.py:43` | No docstring; see implementation. | Input: (latest_y) |
| `agg_model` | `src/alpha/integration/aixi/sources/prod.py:71` | No docstring; see implementation. | Input: (latest_y) |

### `src/alpha/integration/mock/calendar.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `MockCalendar` | `src/alpha/integration/mock/calendar.py:12` | Synthetic session calendar for offline notebook/testing workflows. | Class |
| `MockCalendar.sessions_between` | `src/alpha/integration/mock/calendar.py:26` | No docstring; see implementation. | Input: (self, start: str, end: str) -> list[str] |
| `MockCalendar.sessions_ending_at` | `src/alpha/integration/mock/calendar.py:31` | No docstring; see implementation. | Input: (self, end: str, count: int) -> list[str] |
| `MockCalendar.shift_session` | `src/alpha/integration/mock/calendar.py:38` | No docstring; see implementation. | Input: (self, session: str, offset: int) -> str |

### `src/alpha/integration/mock/interface.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `MockInterface` | `src/alpha/integration/mock/interface.py:12` | Mock backend implementation for notebook and testing workflows. | Class |
| `create_backend` | `src/alpha/integration/mock/interface.py:22` | Convenience factory for callers that want a default mock backend instance. | Input: () -> MockInterface |

### `src/alpha/integration/mock/loader.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `_stable_seed` | `src/alpha/integration/mock/loader.py:14` | No docstring; see implementation. | Input: (*tokens: object) -> int |
| `_normalize_horizon` | `src/alpha/integration/mock/loader.py:22` | No docstring; see implementation. | Input: (horizon: int | str) -> int |
| `MockLoader` | `src/alpha/integration/mock/loader.py:35` | Synthetic data loader backed by deterministic random generation. | Class |
| `MockLoader.load_features` | `src/alpha/integration/mock/loader.py:90` | No docstring; see implementation. | Input: (self, target_sessions: Sequence[str], feature_names: Sequence[str],) -> pd.DataFrame |
| `MockLoader.load_target` | `src/alpha/integration/mock/loader.py:101` | No docstring; see implementation. | Input: (self, target_sessions: Sequence[str], *, horizon: str,) -> pd.DataFrame |
| `MockLoader.load_targets` | `src/alpha/integration/mock/loader.py:112` | No docstring; see implementation. | Input: (self, target_sessions: Sequence[str], *, horizon: list[int],) -> pd.DataFrame |
| `MockLoader.load_dataset` | `src/alpha/integration/mock/loader.py:127` | No docstring; see implementation. | Input: (self, target_sessions: Sequence[str], feature_names: Sequence[str], *, horizon: str,) -> pd.DataFrame |

### `src/alpha/integration/mock/model.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `_stable_seed` | `src/alpha/integration/mock/model.py:15` | No docstring; see implementation. | Input: (*tokens: object) -> int |
| `MockFactorModel` | `src/alpha/integration/mock/model.py:24` | Lightweight linear factor model used by the mock backend. | Class |
| `MockFactorModel.predict` | `src/alpha/integration/mock/model.py:32` | No docstring; see implementation. | Input: (self, terms: pd.DataFrame) -> pd.Series |
| `MockModel` | `src/alpha/integration/mock/model.py:43` | Deterministic synthetic model store for offline analysis workflows. | Class |
| `MockModel.structure` | `src/alpha/integration/mock/model.py:59` | No docstring; see implementation. | Input: (self) -> Dict |
| `MockModel.load_model` | `src/alpha/integration/mock/model.py:79` | No docstring; see implementation. | Input: (self, path: str | Path | None = None, *, name: str | None = None,) -> BaseFactorModel |
| `MockModel.load_models` | `src/alpha/integration/mock/model.py:91` | No docstring; see implementation. | Input: (self, path: str | Path | None = None, *, names: list[str] | None = None,) -> Dict[str, BaseFactorModel] |
| `MockModel.pred` | `src/alpha/integration/mock/model.py:103` | No docstring; see implementation. | Input: (self, features: pd.DataFrame) -> pd.Series |
| `MockModel.preds` | `src/alpha/integration/mock/model.py:108` | No docstring; see implementation. | Input: (self, features: pd.DataFrame, names: list[str] | None = None) -> pd.DataFrame |

### `src/alpha/integration/utils.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `create_default_interface` | `src/alpha/integration/utils.py:12` | Create the default runtime backend interface. | Input: () -> Interface |
| `normalize_horizon` | `src/alpha/integration/utils.py:19` | Normalize horizon labels like 1 / "1" / "1d" into numeric string form. | Input: (horizon: int | str) -> str |
| `normalize_horizons` | `src/alpha/integration/utils.py:31` | Normalize and deduplicate horizon labels while preserving order. | Input: (horizons: Sequence[int | str]) -> list[str] |
| `filter_by_trading_time` | `src/alpha/integration/utils.py:43` | Filter panel data by intraday HHMMSS suffix on the group-level index. | Input: (data: pd.Series | pd.DataFrame, *, group_level: str, trading_times: Sequence[str] | None,) -> pd.Series | pd.DataFrame |
| `to_target_series` | `src/alpha/integration/utils.py:68` | Resolve a canonical target series from a target DataFrame. | Input: (target_df: pd.DataFrame) -> pd.Series |
| `extract_targets_by_horizon` | `src/alpha/integration/utils.py:83` | Extract horizon -> target series mapping from a multi-horizon target table. | Input: (targets_df: pd.DataFrame, horizons: Sequence[int | str],) -> dict[str, pd.Series] |

## Models

### `src/alpha/models/base.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `Predictor` | `src/alpha/models/base.py:13` | No docstring; see implementation. | Class |
| `Predictor.predict` | `src/alpha/models/base.py:14` | No docstring; see implementation. | Input: (self, X: pd.DataFrame | ArrayLike, **kwargs: Any) -> ArrayLike |
| `BaseFactorModel` | `src/alpha/models/base.py:19` | Minimal inference interface for factor models. | Class |
| `BaseFactorModel.predict` | `src/alpha/models/base.py:28` | Predict from a factor DataFrame. | Input: (self, terms: pd.DataFrame) -> pd.Series |

### `src/alpha/models/lightgbm.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `LightGBMFactorModel` | `src/alpha/models/lightgbm.py:13` | LightGBM inference wrapper that selects the model's `term_list` columns. | Class |
| `LightGBMFactorModel.predict` | `src/alpha/models/lightgbm.py:23` | No docstring; see implementation. | Input: (self, terms: pd.DataFrame) -> pd.Series |

## Report

### `src/alpha/report/factor.py`

| Function Name | File Path | Brief Description | Input/Output Types |
|---|---|---|---|
| `plot_factor_analysis_overview` | `src/alpha/report/factor.py:211` | Build a compact overview dashboard for one factor in context. | Input: (ctx: FactorAnalysisContext, factor_name: str, *, title: str | None = None, rolling_window: int = 20, figsize: tuple[float, float] = (14.0, 10.0),) -> Figure |
| `plot_factor_ic_decay` | `src/alpha/report/factor.py:363` | Plot IC decay summary by horizon for one factor in context. | Input: (ctx: FactorAnalysisContext, factor_name: str, *, title: str | None = None, figsize: tuple[float, float] = (9.0, 4.5),) -> Figure |
| `plot_factor_batch_summary` | `src/alpha/report/factor.py:411` | Plot batch-level summary metrics as a grid of bar charts. | Input: (result: FactorBatchAnalysisResult, *, metrics: Sequence[str] | None = None, figsize: tuple[float, float] = (14.0, 8.0),) -> Figure |
| `generate_factor_report_figures` | `src/alpha/report/factor.py:473` | Build a figure bundle for factor reporting. | Input: (*, ctx: FactorAnalysisContext | None = None, factor_name: str | None = None, batch_result: FactorBatchAnalysisResult | None = None,) -> dict[str, Figure] |
| `generate_factor_funnel_report_tables` | `src/alpha/report/factor.py:594` | Run full funnel analyzers and return per-stage tables + status + card summary. | Input: (ctx: FunnelContext, *, respect_config: bool = True,) -> dict[str, pd.DataFrame] |
| `plot_funnel_stage_status` | `src/alpha/report/factor.py:650` | No docstring; see implementation. | Input: (stage_status: pd.DataFrame, *, title: str = "Funnel Stage Status", figsize: tuple[float, float] = (8.0, 4.0),) -> Figure |
| `plot_funnel_tier_distribution` | `src/alpha/report/factor.py:675` | No docstring; see implementation. | Input: (card_summary: pd.DataFrame, *, title: str = "Tier Distribution", figsize: tuple[float, float] = (8.0, 4.0),) -> Figure |
| `plot_funnel_screening_scatter` | `src/alpha/report/factor.py:700` | No docstring; see implementation. | Input: (screening_table: pd.DataFrame, *, title: str = "Screening: IC Mean vs IC IR", figsize: tuple[float, float] = (8.0, 5.0),) -> Figure |
| `plot_funnel_confidence_ranking` | `src/alpha/report/factor.py:731` | No docstring; see implementation. | Input: (card_summary: pd.DataFrame, *, title: str = "Final Confidence Ranking", figsize: tuple[float, float] = (10.0, 4.6),) -> Figure |
| `plot_funnel_redundancy_heatmap` | `src/alpha/report/factor.py:760` | No docstring; see implementation. | Input: (corr_matrix: pd.DataFrame | None, *, title: str = "Factor Redundancy Correlation Matrix", figsize: tuple[float, float] = (7.0, 6.0),) -> Figure |
| `generate_factor_funnel_report_figures` | `src/alpha/report/factor.py:786` | Build funnel-level figures from stage tables and context artifacts. | Input: (ctx: FunnelContext, *, tables: dict[str, pd.DataFrame] | None = None,) -> dict[str, Figure] |
| `generate_factor_funnel_report` | `src/alpha/report/factor.py:810` | Build full funnel report artifacts: stage tables + report figures. | Input: (ctx: FunnelContext, *, respect_config: bool = True,) -> dict[str, dict[str, pd.DataFrame] | dict[str, Figure]] |
