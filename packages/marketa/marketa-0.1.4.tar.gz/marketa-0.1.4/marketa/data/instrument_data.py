from typing import Iterable
from marketa.data.instrument import Instrument
from marketa.data.price_daily import PriceDaily
from marketa.data.price_intraday import PriceIntraday


class InstrumentData:
    def __init__(self, 
                 instrument: Instrument, 
                 price_intraday: PriceIntraday, 
                 price_daily_history: Iterable[PriceDaily]):
        self.instrument = instrument
        self.price_intraday = price_intraday
        self.price_daily_history = price_daily_history