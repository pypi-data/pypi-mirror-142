from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime
from .base import Base


class PriceIntraday(Base):
    """Intraday price of an instrument traded on a particular market at particular time and date"""

    __tablename__ = 'prices_intraday'
    id = Column(Integer, primary_key=True)
    #id = Column(UUID(as_uuid=True), primary_key=True, default=uuid_time_nextval)

    market_id = Column(Integer, ForeignKey('market.id'))
    instrument_id = Column(Integer, ForeignKey('instrument.id'))
    
    # market price of an instrument
    price = Column(Numeric)
    
    # orderbook aggregate data
    bid = Column(Numeric)
    bid_size = Column(Integer)
    ask = Column(Numeric)
    ask_size = Column(Integer)

    datetime = Column(DateTime)      # when instrument had that price
    imported_at = Column(DateTime)   # when price was imported

