import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Enum, Numeric, ForeignKey, Table
from sqlalchemy.orm import relationship
from sequential_uuids.generators import uuid_time_nextval
from .security_type import SecurityType
from .base import Base
from .price_daily import PriceDaily
from .price_intraday import PriceIntraday


class Instrument(Base):
    """Financial instruments are assets that can be traded, or they
       can also be seen as packages of capital that may be traded."""
    
    __tablename__ = 'instrument'

    id = Column(Integer, primary_key=True)
    #id = Column(UUID(as_uuid=True), primary_key=True, default=uuid_time_nextval)
    name = Column(String)
    symbol = Column(String)
    type = Column(Enum(SecurityType))
    description = Column(String)
    currency = Column(String)
    
    prices_daily = relationship(PriceDaily)
    prices_intraday = relationship(PriceIntraday)



