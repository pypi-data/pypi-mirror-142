from .base import Base
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Table, UniqueConstraint, Index

class Watchlist(Base):
   """Watchlist is a set of securities that an investor monitors 
      for potential trading or investing opportunities"""

   __tablename__ = 'watchlist'

   id = Column(Integer, primary_key=True)
   symbol = Column(String)
   updated_at = Column(DateTime)

   #name = Column(String)
   #UniqueConstraint('name', 'symbol', name='name_symbol')
