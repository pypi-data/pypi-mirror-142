# This file is placed in the Public Domain


"command table"


from .function import register
from .object import Object, get


def __dir__():
    return (
        "Command",
    )


class Command(Object):

    cmd = Object()

    @staticmethod
    def add(command):
        register(Command.cmd, command.__name__, command)

    @staticmethod
    def get(command):
        f =  get(Command.cmd, command)
        return f
