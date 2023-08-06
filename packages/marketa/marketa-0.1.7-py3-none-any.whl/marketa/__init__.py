__version__ = '0.1.0'       # semver MAJOR.MINOR.PATCH

container = None

def get_facade():
    global container
    from .facade import Facade
    from .shared.container import Container
    if container is None:
        container = Container()
    return container.resolve(Facade)