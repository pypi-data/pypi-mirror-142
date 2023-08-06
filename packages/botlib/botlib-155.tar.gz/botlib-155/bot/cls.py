# This file is placed in the Public Domain.


"classes table"


from .function import register
from .object import Object, get


def __dir__():
    return (
        "Class",
    )


class Class(Object):

    cls = Object()

    @staticmethod
    def add(clz):
        register(Class.cls, "%s.%s" % (clz.__module__, clz.__name__), clz)

    @staticmethod
    def full(name):
        name = name.lower()
        res = []
        for cln in Class.cls:
            if cln.split(".")[-1].lower() == name:
                res.append(cln)
        return res

    @staticmethod
    def get(nm):
        return get(Class.cls, nm)
