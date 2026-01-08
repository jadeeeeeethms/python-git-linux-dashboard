import pandas as pd
import numpy as np
from data.fetchers import fetch_price

def loadPrices(tickers):
    prices = []
    for t in tickers:
        prices.append(fetch_price(t))
    return pd.concat(prices, axis=1)

def computeReturns(prices):
    return prices.pct_change().dropna()

def computePortfolioReturns(returns, weights):
    return returns.dot(weights)

def computeCumulativeReturns(returns):
    return (1 + returns).cumprod()

def computePortfolioVolatility(portfolio_returns):
    return portfolio_returns.std()*np.sqrt(252)

def computePortfolioAnnualReturn(portfolio_returns):
    return portfolio_returns.mean()*252

def computeCorrelationMatrix(returns):
    return returns.corr()
