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

Market data is retrieved from Yahoo Finance through the `yfinance` API.

- Daily closing prices are downloaded over a rolling one-year period  
- Data requests are cached locally with a 5mn time-to-live to limit repeated
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

# Optional bonus – Predictive model

As an optional extension, a simple predictive model is included to provide a basic
forecast of future asset prices.
The model is based on a linear regression applied to the logarithm of historical
prices. Future values are projected over a user-defined horizon, and confidence
intervals are added to illustrate forecast uncertainty. The results are displayed
directly on the dashboard alongside historical data.
This component is intentionally simple and is meant to illustrate how basic
forecasting methods can be integrated into a quantitative analysis framework,
rather than to generate trading signals.

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


# QUANT B – MULTI-ASSET PORTFOLIO ANALYSIS

Quant B is the multivariate extension of the project developed with Streamlit.
Its purpose is to analyze several financial assets simultaneously and construct custom portfolios using historical and real-time market data. The module is designed to simulate a professional portfolio management environment, focusing on diversification, risk analysis and interpretability rather than model complexity.

# objective

The main objective of Quant B is to build and analyze multi-asset portfolios in order to study diversification effects and compare individual asset performance with portfolio performance. The analysis is conducted in a multivariate setting using daily frequency data and transparent portfolio construction rules. The emphasis is placed on risk management and diversification analysis. This module naturally extends Quant A toward a more realistic portfolio framework.

# Data acquisition and processing

This module relies on two complementary data sources. Historical price data is retrieved using the yfinance API. Daily closing prices over a one-year period are downloaded and used to compute returns, correlations and portfolio performance. Data requests are cached locally with a five-minute time-to-live in order to limit API calls and improve application performance. This source is exclusively used for all historical computations and backtesting procedures.

Real-time market data is retrieved using the Finnhub API. This API provides live quotes which are used to display the current price and daily variation of each selected asset. An important limitation is that the free Finnhub plan does not provide access to historical price data. For this reason, Yahoo Finance is used for historical analysis while Finnhub is used only for real-time monitoring. This hybrid architecture mimics professional trading systems where historical databases and live market feeds are separated.

# Portfolio construction

Users can select between two and five assets among AAPL, MSFT, GOOGL, AMZN and META. Portfolio weights are defined using interactive sliders with values between zero and one. The system automatically normalizes weights so that their sum always equals one. This allows the construction of equal-weight portfolios as well as custom allocations and enables the study of risk concentration effects.

# Mathematical framework

Daily returns are computed as the relative price variation between two consecutive days. Portfolio returns are obtained as the weighted sum of individual asset returns. Cumulative performance is computed as the product of one plus daily returns over time. This methodology ensures consistency with classical quantitative finance standards.

# Performance metrics

Several portfolio indicators are computed including annualized return, annualized volatility and the correlation matrix. These metrics allow a joint evaluation of performance and risk and provide insight into diversification benefits and asset dependencies.

# User interface

The Streamlit dashboard allows the user to select multiple assets, define portfolio weights, monitor real-time prices, visualize cumulative performance and inspect the correlation matrix. The main chart displays both individual asset performance and the cumulative value of the portfolio, allowing direct visual comparison.

# Robustness and error handling

Defensive checks are implemented at each stage of the data pipeline. API failures, missing price series and invalid data are detected automatically. When an issue occurs, the application stops safely and displays a clear error message. This prevents crashes and ensures professional reliability.

# Integration within the project

Quant B relies on shared project components for data retrieval, return computation and performance metrics. This modular structure ensures coherence with Quant A and facilitates future extensions of the platform.

# Interpretation of results

The dashboard illustrates diversification benefits and volatility reduction. The portfolio curve is generally smoother and more stable than individual asset curves due to imperfect correlations and risk spreading. This highlights the trade-off between return and stability and demonstrates the impact of portfolio construction on risk management.


and lower volatility, but may also reduce participation in strong market trends.

