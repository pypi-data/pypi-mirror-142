__version__ = '0.1.0'       # semver MAJOR.MINOR.PATCH

# apply extension methods
from .shared import extensions
del(extensions)

# create default facade instance
from .facade import Facade
from .shared.container import Container

_container = Container()
def get_facade() -> Facade:
    from .facade import Facade
    return _container.resolve(Facade)

del(Container, Facade) # cleanup global namespace