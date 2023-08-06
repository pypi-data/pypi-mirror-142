# This file is placed in the Public Domain.


"module table"


from .object import Object, get


def __dir__():
    return (
        "Tbl",
    )


class Table(Object):

    mod = Object()

    @staticmethod
    def add(o):
        Table.mod[o.__name__] = o

    @staticmethod
    def get(nm):
        return get(Table.mod, nm, None)
