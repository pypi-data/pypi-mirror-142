from datetime import datetime
from decimal import Decimal
from typing import Iterable
from zoneinfo import ZoneInfo

from marketa.data.instrument_data import InstrumentData
from marketa.shared.exceptions import MarketaException
from .repository_base import RepositoryBase

# ensure all entities are imported,
# so that they will be created automatically with repo.create_all() call
from .application import Application
from .market import Market
from .watchlist import Watchlist
from .instrument import Instrument
from .price_daily import PriceDaily
from .price_intraday import PriceIntraday


class Repository(RepositoryBase):
    def __init__(self, in_memory=False):
        super().__init__(in_memory)

    def create_all(self):
        super(Repository, self).create_all()

        # seed database if there are no symbols yet
        if len(self.get_watchlist_symbols()) == 0:
            self.add_watchlist_item('AAAU')


    def create_market(self, market: Market):
        self._session.add(market)

    
    def get_markets(self) -> Iterable[Market]:
        return self._session.query(Market).all()


    def create_instrument(self, instrument: Instrument):
        if instrument.symbol is None:
            raise MarketaException('symbol for the instrument is none')
        self._session.add(instrument)


    def get_instruments(self) -> Iterable[Instrument]:
        return self._session.query(Instrument).all()


    def get_watchlist_symbols(self):
        items = self._session.query(Watchlist).all()
        if len(items) == 0:
            return []
        return list(map(lambda x: x.symbol, items))

    def add_watchlist_item(self, symbol: str):
        item = Watchlist()
        item.symbol = symbol
        item.updated_at = gmt_time_now()
        self._session.add(item)
        self.commit()

    def update_watchlist_item_timestamp(self, symbol: str):
        item: Watchlist = self._session.query(Watchlist).one()
        item.updated_at = gmt_time_now()
        self.commit()


    def create_intraday_price(self, symbol: str, data: PriceIntraday):
        market: Market = self._session.query(Market).one()
        instrument: Instrument = (self._session
            .query(Instrument)
            .filter(Instrument.symbol == symbol)
            .one()
        )
        data.instrument_id = instrument.id
        data.market_id = market.id
        self._session.add(data)


    def get_intraday_prices(self, symbol: str) -> Iterable[Instrument]:
        market: Market = self._session.query(Market).one()
        instrument: Instrument = (self._session
            .query(Instrument)
            .filter(Instrument.symbol == symbol)
            .one()
        )
        prices: PriceIntraday = (self._session
            .query(PriceIntraday)
            .filter(
                PriceIntraday.instrument_id == instrument.id, 
                PriceIntraday.market_id == market.id
            )
            .all()
        )
        return prices
        

    def upsert_instruments(self, instruments):
        for instrument in instruments:
            self.upsert_instrument(instrument, commit=False)
        self.commit()

    def upsert_instrument(self, data: Instrument, commit=True):
        instrument: Instrument = (self._session
            .query(Instrument)
            .filter(
                Instrument.symbol == data.symbol
            )
            .one_or_none()
        )
        if instrument is None:
            self.create_instrument(data)
        else:
            if data.symbol is not None:
                instrument.symbol = data.symbol
            if data.name is not None:
                instrument.name = data.name
            if data.description is not None:
                instrument.description = data.description
            if data.type is not None:
                instrument.type = data.type
            if data.currency is not None:
                instrument.currency = data.currency

        if commit:
            self.commit()

    

    def upsert_instrument_data(self, data: InstrumentData):
        market: Market = self._session.query(Market).one()
        self.upsert_instrument(data.instrument)
        instrument: Instrument = (self._session
            .query(Instrument)
            .filter(
                Instrument.symbol == data.instrument.symbol
            )
            .one()
        )
        
        price = data.price_intraday
        now = gmt_time_now()
        price.datetime = now
        price.imported_at = now
        
        price.instrument_id = instrument.id
        price.market_id = market.id

        self.create_intraday_price(instrument.symbol, price)
        
        for price_daily in data.price_daily_history:
            price_daily.market_id = market.id
            price_daily.instrument_id = instrument.id
            price_daily.imported_at = now
            self._session.add(price_daily)

        self.commit()


def gmt_time_now():
     return datetime.now().astimezone(ZoneInfo(key='GMT')) # in db its stored as gmt