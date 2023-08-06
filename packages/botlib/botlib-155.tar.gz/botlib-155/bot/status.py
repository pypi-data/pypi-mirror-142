# This file is placed in the Public Domain.


"status commands"


import threading
import time


from .bus import Bus
from .command import Command
from .object import Object, get, keys, update
from .parse import aliases, elapsed
from .thread import getname, starttime


def __dir__():
    return (
        "commands",
        "fleet"
        "threads"
    )


def commands(event):
    event.reply(",".join((sorted(keys(Command.cmd)))))


cmd = commands

def fleet(event):
    try:
        index = int(event.args[0])
        event.reply(Bus.objs[index])
        return
    except (KeyError, TypeError, IndexError, ValueError):
        pass
    event.reply(" | ".join([getname(o) for o in Bus.objs]))


flt = fleet


def threads(event):
    result = []
    for t in sorted(threading.enumerate(), key=lambda x: x.getName()):
        if str(t).startswith("<_"):
            continue
        o = Object()
        update(o, vars(t))
        if get(o, "sleep", None):
            up = o.sleep - int(time.time() - o.state.latest)
        else:
            up = int(time.time() - starttime)
        thrname = t.getName()
        if not thrname:
            continue
        if thrname:
            result.append((up, thrname))
    res = []
    for up, txt in sorted(result, key=lambda x: x[0]):
        res.append("%s(%s)" % (txt, elapsed(up)))
    if res:
        event.reply(" ".join(res))


thr = threads


Command.add(commands)
Command.add(fleet)
Command.add(threads)
aliases.cmd = "commands"
aliases.flt = "fleet"
aliases.thr = "threads"
