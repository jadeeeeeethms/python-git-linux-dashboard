import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from datetime import datetime
from core.utils import loadPrices, computeReturns, computePortfolioReturns, computePortfolioAnnualReturn, computePortfolioVolatility
import numpy as np



tickers = ["AAPL","MSFT","GOOGL"]
weights = [1/3,1/3,1/3]

prices = loadPrices(tickers)
returns = computeReturns(prices)
portfolio = computePortfolioReturns(returns, weights)
cum = (1 + portfolio).cumprod()
rolling_max = cum.cummax()
drawdown = (cum - rolling_max) / rolling_max
max_dd = drawdown.min()
annual = computePortfolioAnnualReturn(portfolio)
vol = computePortfolioVolatility(portfolio)

date = datetime.now().strftime("%Y-%m-%d")
os.makedirs("reports", exist_ok=True)

with open(f"reports/report_{date}.txt","w") as f:
    f.write(f"Date: {date}\n")
    f.write(f"Annual return: {annual:.2%}\n")
    f.write(f"Volatility: {vol:.2%}\n")
    f.write(f"Max drawdown: {max_dd:.2%}\n")

os.system("git add reports/*.txt") #automatiser le push sur git
os.system(f'git commit -m "chore: daily report {date}"')
os.system("git push")


 