from zoneinfo import ZoneInfo
from sqlalchemy import Column, Integer, Interval, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base


markets_instruments_association = Table('markets_instruments', Base.metadata,
    Column('market_id', Integer, ForeignKey('market.id')),
    Column('instrument_id', Integer, ForeignKey('instrument.id'))
)

class Market(Base):
    """Market where financial instruments are traded"""

    __tablename__ = 'market'
    id = Column(Integer, primary_key=True)
    #id = Column(UUID(as_uuid=True), primary_key=True, default=uuid_time_nextval)
    name = Column(String)
    description = Column(String)
    timezone_name = Column(String)

    instruments = relationship("Instrument", secondary=markets_instruments_association)
