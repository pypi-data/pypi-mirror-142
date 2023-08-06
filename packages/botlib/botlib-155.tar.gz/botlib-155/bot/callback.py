# This file is placed in the Public Domain.


"callback table"


from .function import register
from .object import Object, get
from .thread import launch


def __dir__():
    return (
        "Callback",
    )


class Callback(Object):

    cbs = Object()
    threaded = False

    @staticmethod
    def add(name, cb):
        register(Callback.cbs, name, cb)

    @staticmethod
    def callback(e):
        f = Callback.get(e.type)
        if f:
            f(e)

    @staticmethod
    def get(cmd):
        return get(Callback.cbs, cmd)


    @staticmethod
    def dispatch(e):
        if Callback.threaded:
            e.thrs.append(launch(Callback.callback, e, name=e.txt))
            return
        Callback.callback(e)
