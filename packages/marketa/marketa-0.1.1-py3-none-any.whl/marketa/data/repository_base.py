from pytest import Session
from sqlalchemy import create_engine, false
from sqlalchemy.orm import sessionmaker
from .base import Base


class RepositoryBase:
    def __init__(self, in_memory=False):
        
        if in_memory:
            self._engine = create_engine('sqlite://', echo=False)
            self._engine.execute("ATTACH DATABASE ':memory:' AS my_database")
        else:
            #engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
            self._engine = create_engine('sqlite:///marketa.sqlite', echo = False)
        
        self._create_session = sessionmaker(bind=self._engine)
        self._session: Session = self._create_session()
    

    def create_all(self):
        Base.metadata.create_all(self._engine)
        self.commit()

    def recreate_all(self):
        Base.metadata.drop_all(self._engine)
        self.commit()
        self.create_all()

    def commit(self):
        self._session.commit()


    def __enter__(self):
        self._ensure_session()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.__exit__(exc_type, exc_value, traceback)
        self._session = None


    def _ensure_session(self):
        if not self._session:
            self._session = self._create_session()
