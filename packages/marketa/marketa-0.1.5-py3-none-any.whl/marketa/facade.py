import shutil
import matplotlib
from matplotlib import pyplot as plt
from .services.feed import Feed
from .entities.ticker import Ticker
from .shared.utils import  check_internet as is_online
from .shared.exceptions import MarketaException
from .data.repository import Repository
from .shared.taskeeper import taskeeper

class Facade:

    def __init__(self, 
        repository: Repository, 
        feed_provider: Feed):
        self._repository = repository
        self._feed_provider = feed_provider
        repository.create_all()
        self.__apply_extension_methods()


    def is_watching(self, symbol:str):
        raise NotImplementedError()
        symbol = symbol.upper()
        state = load_state()
        watchlist = state['watchlists']['default']
        return symbol in watchlist


    def watch(self, symbol:str):
        raise NotImplementedError()
        symbol = symbol.upper()
        state = load_state()
        watchlist = state['watchlists']['default']
        if symbol in watchlist:
            raise Exception(f'symbol {symbol} is already in the watchlist')
        watchlist.append(symbol)
        save_state(state)


    def unwatch(self, symbol:str):
        raise NotImplementedError()
        symbol = symbol.upper()
        state = load_state()
        watchlist = state['watchlists']['default']
        if symbol not in watchlist:
            raise Exception(f'symbol {symbol} is not in the watchlist') 
        watchlist.remove(symbol)    
        save_state(state)


    def pull(self, make_inet_check = True):
        if make_inet_check and not is_online(): 
            raise MarketaException('unable to pull data as there is no internet connection available')

        watchlist = self._repository.get_watchlist_symbols()

        with taskeeper(steps = len(watchlist) + 2) as task:
            with task.step('loading tradable nasdaq symbols'):
                tradable_instruments = self._feed_provider.load_instruments()
            
            with task.step('updating database'):
                self._repository.upsert_instruments(tradable_instruments)
            
            tradable_symbols = list(map(lambda x: x.symbol, tradable_instruments))
            for s in watchlist:
                if s not in tradable_symbols:
                    raise Exception(f'symbol "{s}" in not listed on nasdaq exchange')

                with task.step(f'loading "{s}" symbol data'):
                    data = self._feed_provider.load_instrument_data(s)
                    self._repository.upsert_instrument_data(data)
                    self._repository.update_watchlist_item_timestamp(s)
                
            task.set_info(f'data successfully loaded for {len(watchlist)} symbol(s)')


    def get_state(self):
        raise NotImplementedError()
        state = load_state()
        return state


    def clear_caches(self):
        raise NotImplementedError()
        path = get_state_path().parent.resolve()
        shutil.rmtree(path, ignore_errors=True)


    def get_ticker(self, symbol: str) -> Ticker:
        return self._feed_provider.load_instrument_data(symbol)


    def plot(self, ticker: Ticker):
        mpl_backend = 'QTAgg'
        matplotlib.use(mpl_backend)
        with plt.ion():
            plt.plot([1,2,3])
        raise NotImplementedError()

    def __apply_extension_methods(self):
        from .shared import extensions
        del(extensions)
