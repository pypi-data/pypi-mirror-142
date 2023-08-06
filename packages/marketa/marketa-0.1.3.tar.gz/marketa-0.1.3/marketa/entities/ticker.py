import pandas as pd
import yfinance as yf
from ..data.security_type import SecurityType


class Ticker:
    """Stock ticker is a report of the price of certain securities, updated continuously
    throughout the trading session by a particular stock market exchange."""
    
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.history = pd.DataFrame()

    
