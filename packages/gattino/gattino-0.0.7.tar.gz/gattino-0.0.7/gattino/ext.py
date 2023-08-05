import abc
from .gattino import Gattino, GattinoEvent


class ExtBase(metaclass=abc.ABCMeta):
    conf_key = "gattino_ext"

    def __init__(self, app: Gattino):
        self.app = app
        if app is not None:
            self.__init_app(app)

    @abc.abstractmethod
    def load_conf(self):
        pass

    def __init_app(self, app):
        app.ext.append(self)

    def bind_event(self, event: GattinoEvent, handle):
        self.app.events[event.value].append(handle)