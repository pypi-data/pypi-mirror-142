from .base import Base
from sqlalchemy import Column, String

class Application(Base):
    """Container for global application settings"""

    __tablename__ = 'application'

    key = Column(String, primary_key=True)
    value = Column(String)
