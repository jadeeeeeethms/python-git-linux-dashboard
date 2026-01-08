# python-git-linux-dashboard


# QUANT A - SINGLE ASSET ANALYSIS

Quant A is an interactive analysis module developed with Streamlit.  
Its purpose is to study and backtest simple quantitative strategies applied to a
single financial asset, using historical market data.

The module is designed as an introductory quantitative framework, focusing on
clarity, robustness, and interpretability rather than model complexity.


# objective

The main objective of Quant A is to analyze the behaviour of one asset at a time
and evaluate the performance of basic trading strategies.

The analysis is conducted under the following assumptions:
- univariate setting (one asset)
- daily frequency data
- simple and transparent strategy logic
- emphasis on performance interpretation and risk analysis

This module serves as a foundation for more advanced quantitative extensions.


# Data acquisition and processing

Market data is retrieved from Yahoo Finance** through the `yfinance` API.

- Daily closing prices are downloaded over a rolling one-year period  
- Data requests are cached locally with a 5-minute time-to-live to limit repeated
  calls to the API  
- Several validation checks are performed to ensure data integrity  

Price loading and return computation are handled by shared utility functions to
maintain consistency across the project.

# Implemented strategies

Two trading strategies are implemented and can be selected through the user
interface.

# Buy & Hold

The Buy & Hold strategy assumes a constant full exposure to the asset throughout
the entire investment horizon.  
It is used as a benchmark to evaluate the added value of more dynamic strategies.

# Momentum with volatility targeting

This strategy combines a momentum signal with risk control mechanisms:

- momentum is computed from past asset returns over a rolling window  
- volatility is estimated using historical returns  
- position size is dynamically adjusted to target a fixed annual volatility  

All parameters (lookback windows and volatility target) are fully configurable
from the dashboard.

# Performance metrics

For each strategy, several performance indicators are computed:

- total return  
- annualized return  
- annualized volatility  
- Sharpe ratio  
- maximum drawdown  

These metrics allow for a joint evaluation of performance and risk, and are
computed using shared functions from the project’s metrics module.

# User interface

The Streamlit dashboard provides an interactive environment allowing the user to:

- select an asset  
- choose a strategy  
- tune strategy parameters  
- visualize cumulative performance  
- monitor strategy exposure over time  

Key performance indicators are displayed directly on the interface.  
An optional debug mode can be enabled to inspect raw prices and return statistics.

# Robustness and error handling

To ensure stability, the module includes defensive checks at each stage of the
data pipeline:
- empty or missing price series  
- absent ticker columns  
- invalid or empty return series  

When an issue is detected, the application stops gracefully and displays a clear
error message instead of crashing.

# Integration within the project

Quant A relies on shared project components for:
- market data retrieval  
- return computation  
- performance metrics  
- single-asset strategy implementation  

This modular structure ensures coherence with other quantitative modules and
facilitates future extensions of the project.

# Interpretation of results

The dashboard presents the performance of different strategies applied to a
single financial asset.

The Buy & Hold strategy is used as a benchmark and reflects the natural price
evolution of the asset. Its performance strongly depends on market trends.
The momentum strategy with volatility targeting aims to control risk by
adjusting exposure dynamically. This generally leads to smoother performance
and lower volatility, but may also reduce participation in strong market trends.

These results illustrate the trade-off between return and risk management, and
highlight that risk-controlled strategies do not systematically outperform
simple passive benchmarks.

