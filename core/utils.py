import pandas as pd
from typing import List
from data.fetchers import fetch_price


def loadPrices(tickers, freq="1d"):
    prices = []
    for ticker in tickers:
        data = fetch_price(ticker, freq)
        #data["price"] est un DataFrame à 1 colonne
        df = data[["price"]].rename(columns={"price": ticker})
        prices.append(df)
    priceDf = pd.concat(prices, axis=1)
    priceDf = priceDf.dropna()
    return priceDf


def computeReturns(priceDf):
    returns = priceDf.pct_change()
    returns = returns.dropna()
    return returns

def computePortfolioReturns(returnsDf, weights=None):
    nbAssets = returnsDf.shape[1]
    if weights is None:
        weights = [1/nbAssets]*nbAssets
    portfolioReturns = returnsDf.dot(weights)
    return portfolioReturns

#rendement cumulé portefeuille
def computeCumulativeReturns(portfolioReturns):
    cumulative = (1 + portfolioReturns).cumprod()
    return cumulative

#volatilité portefeuille
def computePortfolioVolatility(portfolioReturns):
    vol = portfolioReturns.std()*(252**0.5)
    return vol

#rendement annuel moyen portefeuille
def computePortfolioAnnualReturn(portfolioReturns):
    avgReturn = portfolioReturns.mean()*252
    return avgReturn

#mat correlation
def computeCorrelationMatrix(returnsDf):
    corr=returnsDf.corr()
    return corr

