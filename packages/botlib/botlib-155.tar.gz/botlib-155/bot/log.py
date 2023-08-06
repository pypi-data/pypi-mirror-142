# This file is placed in the Public Domain.


"log text"


def __dir__():
    return (
        "log",
    )


from .cls import Class
from .command import Command
from .database import save
from .object import Object


class Log(Object):

    def __init__(self):
        super().__init__()
        self.txt = ""


def log(event):
    if not event.rest:
        event.reply("log <txt>")
        return
    o = Log()
    o.txt = event.rest
    save(o)
    event.reply("ok")


Class.add(Log)
Command.add(log)
