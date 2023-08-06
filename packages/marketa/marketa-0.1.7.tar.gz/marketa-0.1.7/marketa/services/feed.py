from decimal import Decimal
from typing import Final, Iterable, List
import pandas as pd
import io, requests
from pandas import DataFrame
from purl import URL
from marketa.data.instrument_data import InstrumentData
from marketa.data.market import Market
from marketa.data.instrument import Instrument
from marketa.data.price_daily import PriceDaily
from marketa.data.price_intraday import PriceIntraday
from marketa.entities.ticker import Ticker
from ..data.security_type import SecurityType
from ..shared.exceptions import MarketaException
import yfinance as yf
from abc import ABC, abstractmethod


class Feed(ABC):

    @abstractmethod
    def load_market(self) -> Market: pass

    @abstractmethod
    def load_instruments(self) -> Iterable[Instrument]: pass

    @abstractmethod
    def load_instrument_data(self, symbol: str) -> InstrumentData: pass



class NasdaqFeed(Feed):
    """Responsible for importing data from nasdaq.com website pages that contain securities feeds.
       Feeds are produced by online stock screener. Stock screeners are tools that allow investors 
       and traders to sort through thousands of individual securities to find those that fit their own needs."""

    headers: Final = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

    def __init__(self):
        pass


    def load_market(self) -> Market:
        result = Market()
        result.name = 'NASDAQ'
        result.description = 'Nasdaq is a global electronic marketplace for buying and selling securities. Originally an acronym for "National Association of Securities Dealers Automated Quotations"—it was a subsidiary of the National Association of Securities Dealers (NASD), now known as the Financial Industry Regulatory Authority (FINRA). Nasdaq was created as a site where investors could trade securities on a computerized, speedy, and transparent system.1 It commenced operations on Feb. 8, 1971'
        # load any ticker to get exchange timezone
        t = yf.Ticker('AAAU')
        result.timezone_name = t.info['exchangeTimezoneName']
        return result


    def load_instruments(self) -> Iterable[Instrument]:
        data = DataFrame()
        data_traded = self.__fetch_nasdaq_traded_symbols()
        data_index = self.__fetch_nasdaq_index_symbols()

        # merge results into a single dataframe
        data = data.append(data_traded)
        data = data.append(data_index)
        data.reset_index(
            drop=True, # removes old incorrect integer row index and replaces it with updated one
            inplace=True
        )

        # convert into a typed collection
        result: List[Instrument] = []
        for idx, row in data.iterrows():
            instrument = Instrument()
            instrument.symbol = row['symbol']
            instrument.name = row['name']
            instrument.type = SecurityType.parse(row['type'])
            result.append(instrument)
        return result


    def load_instrument_data(self, symbol: str) -> InstrumentData:
        instrument = Instrument()
        price_intraday = PriceIntraday()
        price_daily_today = PriceDaily() # we will store potentially incomplete aggregate values available
        price_daily_history: List[PriceDaily] = []

        t = yf.Ticker(symbol)
        
        instrument.symbol = symbol
        instrument.name = t.info['longName']
        
        if 'quoteType' in dict(t.info).keys():
            instrument.type = SecurityType.parse(t.info['quoteType'])

        if 'longBusinessSummary' in dict(t.info).keys():
            instrument.description = t.info['longBusinessSummary']
        
        instrument.currency = t.info['currency']
        price_daily_today.volume = int(t.info['regularMarketVolume'])

        price_daily_today.open = Decimal(t.info['open'])
        price_daily_today.high = t.info['dayHigh']
        price_daily_today.low = t.info['dayLow']
        # close is ambiguous here, as it seems we don't have field indicating if market closed or not
        # and regularMarketPreviousClose may indicate close for previous day
        #if not t.info['tradeable']:
        #    price_daily_today.last_close = self.price # after market closes, last_close should equal to price
        #else:
        #    self.last_close = t.info['regularMarketPreviousClose']
        
        price_intraday.price = Decimal(t.info['regularMarketPrice'])
        price_intraday.bid = t.info['bid']
        price_intraday.bid_size = t.info['bidSize']
        price_intraday.ask = t.info['ask']
        price_intraday.ask_size = t.info['askSize']

        history:DataFrame = yf.download(symbol, period='max', progress=False)
        if len(history.index) == 0:
            raise Exception(f'no historical data for "{symbol}" symbol')

        for idx, row in history.iterrows():
            price_item = PriceDaily()
            price_item.open = row['Open']
            price_item.close = row['Close']
            price_item.high = row['High']
            price_item.low = row['Low']
            price_item.volume = row['Volume']
            price_item.date = row.name.to_pydatetime().date()
            price_daily_history.insert(0, price_item)

        price_daily_history.append(price_daily_today)
        return InstrumentData(instrument, price_intraday, price_daily_history)



    def __fetch_nasdaq_traded_symbols(self) -> DataFrame:
        url = URL('https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqtraded.txt')
        csv_text = requests.get(url, headers = self.headers).text
        df: DataFrame = pd.read_csv(io.StringIO(csv_text), sep="|")
        
        # drop test rows
        df.drop_rows(column = 'Test Issue', predicate = lambda c: c == 'Y')

        df.drop(columns=[
            'Nasdaq Traded', 'Test Issue', 'Round Lot Size', 'Market Category', 
            'Listing Exchange', 'Financial Status', 'CQS Symbol', 'NASDAQ Symbol', 'NextShares'
        ], inplace=True)
        
        df.rename(columns={
            'Symbol': 'symbol',
            'Security Name': 'name',
            'ETF': 'etf',
        }, inplace=True)
        
        df['type'] = df['etf'].apply(lambda x: SecurityType.stock.name if x == 'N' else SecurityType.etf.name)
        df.drop(columns=['etf'], inplace=True)

        return df


    def __fetch_nasdaq_index_symbols(self) -> DataFrame:
        df = DataFrame()
        url = URL('https://api.nasdaq.com/api/screener/index')
        
        # we can only query 50 pages per request, otherwise it won't work
        offset = 0
        while True:
            url = URL('https://api.nasdaq.com/api/screener/index?offset=' + str(offset))
            json = requests.get(url, headers = self.headers).json()
            rows = json['data']['records']['data']['rows']
            for irow, row in enumerate(rows):
                df.append(pd.Series(dtype='object'), ignore_index=True) # insert empty row
                for col_name in row:
                    df.loc[irow + offset, col_name] = row[col_name]
            offset+=50
            if offset > json['data']['records']['totalrecords']:
                break
        
        df.drop(columns=['lastSalePrice', 'netChange', 'percentageChange', 'deltaIndicator'], inplace=True)
        df.rename(columns={ 'companyName': 'name' }, inplace=True)
        df = df.assign(type=SecurityType.index.name) # adds 'type' attribute with 'index' value to all rows
        if 'symbol' not in df.columns:
            raise MarketaException('nasdaq index feed is missing "symbol" column')
        return df
