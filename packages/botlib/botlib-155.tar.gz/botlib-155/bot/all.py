# This file is placed in the Public Domain.


"all modules"


def __dir__():
    return (
        "find",
        "log",
        "irc",
        "rss",
        "status",
        "todo",
        "udp",
        "user"
    )



from bot.table import Table


from bot import find
from bot import log
from bot import irc
from bot import rss
from bot import status
from bot import todo
from bot import udp
from bot import user


for mn in __dir__():
    md = getattr(locals(), mn, None)
    if md:
        Table.add(md)
