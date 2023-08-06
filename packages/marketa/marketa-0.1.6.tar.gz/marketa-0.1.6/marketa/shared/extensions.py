from typing import Any, Callable, TypeVar

from pandas import DataFrame
from diskcache import Cache


def search(self: DataFrame, val: str, case=False, regex=False):
    """Search all the text columns of `df`, return rows with any matches."""
    textlikes = self.select_dtypes(include=[object, "string"])
    return self[
        textlikes.apply(
            lambda column: column.str.contains(val, regex=regex, case=case, na=False)
        ).any(axis=1)
    ]
DataFrame.search = search
del(search) # clean up namespace


def drop_rows(self: DataFrame, column: str, predicate: Callable[[object], bool]):
    indexNames = self[lambda x: predicate(self[column])].index
    self.drop(indexNames , inplace=True)
DataFrame.drop_rows = drop_rows
del(drop_rows)


T = TypeVar("T")
def getf(self:Cache, key: str, getter: Callable[[], T], timeout:int) -> T:
    val = self.get(key)
    if val is None:
        val = getter()
        self.set(key, val, expire=timeout)
    return val
Cache.getf = getf
del(getf)