# This file is placed in the Public Domain.


"todo items"


def __dir__():
    return (
        "todo"
    )


import time



from .cls import Class
from .command import Command
from .database import find, fntime, save
from .object import Object
from .parse import aliases, elapsed


class Todo(Object):

    def __init__(self):
        super().__init__()
        self.txt = ""


def todo(event):
    if not event.rest:
        nr = 0
        for fn, o in find("todo"):
            event.reply("%s %s %s" % (nr, o.txt, elapsed(time.time() - fntime(fn))))
        return
    o = Todo()
    o.txt = event.rest
    save(o)
    event.reply("ok")


Class.add(Todo)
Command.add(todo)
aliases.tdo = "todo"
