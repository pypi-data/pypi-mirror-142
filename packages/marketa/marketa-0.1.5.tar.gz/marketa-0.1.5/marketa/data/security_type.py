from enum import Enum

from marketa.shared.exceptions import MarketaException

class SecurityType(Enum):
    stock = 0   # common stock
    mutual = 1  # mutual fund
    etf = 2     # exchange traded fund
    index = 3   # index fund

    def parse(s: str):
        if s.upper() == 'ETF': return SecurityType.etf
        if s.upper() == 'INDEX': return SecurityType.index
        if s.upper() == 'STOCK': return SecurityType.stock
        raise MarketaException(f'unknown security type {s}')