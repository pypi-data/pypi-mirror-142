
from sqlalchemy import Column, DateTime, Enum, Integer, Numeric, ForeignKey, Date
from .base import Base


class PriceDaily(Base):
    """Daily report of a price of an instrument traded on a particular market at particular date"""

    __tablename__ = 'prices_daily'
    id = Column(Integer, primary_key=True)
    market_id = Column(Integer, ForeignKey('market.id'))
    instrument_id = Column(Integer, ForeignKey('instrument.id'))
    #id = Column(UUID(as_uuid=True), primary_key=True, default=uuid_time_nextval)

    
    open = Column(Numeric)
    close = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)

    volume = Column(Integer)

    date = Column(Date)                # day when instrument had that price
    imported_at = Column(DateTime)   # when price was imported