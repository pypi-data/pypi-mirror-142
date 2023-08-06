import lagom
from typing import Any, TypeVar, Callable
from ..data.repository import Repository
from ..services.feed import Feed, NasdaqFeed


TAbstract = TypeVar("TAbstract")
T = TypeVar("T")
class Container:
    def __init__(self):
        self.container = lagom.Container()
        self.register_singleton(Repository)
        self.register_singleton_pair(Feed, NasdaqFeed)

    def register_singleton_pair(self, tabstract: TAbstract, tconcrete: T, override=False):
        if override and tabstract in self.container._registered_types:
            self.container._registered_types.pop(tabstract, None)
        self.container[tabstract] = lagom.Singleton(tconcrete)

    def register_singleton(self, type):
        self.container[type] = lagom.Singleton(type)
    
    def register_singleton_factory(self, type: T, factory: Callable[[], T]):
        self.container[type] = factory


    def resolve(self, type: T) -> T:
        result = self.container[type]
        if not result:
            raise Exception(f'unable to instantiate type {type}')
        return result
