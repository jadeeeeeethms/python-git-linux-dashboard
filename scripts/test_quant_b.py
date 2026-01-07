from core.utils import (loadPrices,computeReturns,computePortfolioReturns,computeCumulativeReturns,computePortfolioVolatility, computePortfolioAnnualReturn, computeCorrelationMatrix)

tickers = ["AAPL", "MSFT", "GOOGL"]
freq = "1d"

prices = loadPrices(tickers, freq) #charg prices
print("Prices:")
print(prices.head(), "\n")

returns = computeReturns(prices)
print("Returns:")
print(returns.head(), "\n")

portfolio = computePortfolioReturns(returns)
print("Portfolio returns:")
print(portfolio.head(), "\n")

cumulative = computeCumulativeReturns(portfolio) #metriques port
vol = computePortfolioVolatility(portfolio)
annual = computePortfolioAnnualReturn(portfolio)
corr = computeCorrelationMatrix(returns)
#affichage
print("Cumulative portfolio:")
print(cumulative.tail(), "\n")
print("Annual return:", round(annual, 4))
print("Volatility:", round(vol, 4), "\n")
print("Correlation matrix:")
print(corr)
