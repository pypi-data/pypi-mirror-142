# This file is placed in the Public Domain.


"configuration"


from .object import Object


def __dir__():
    return (
        "Config",
    )


class Config(Object):

    name = "botlib"
