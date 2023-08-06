# This file is placed in the Public Domain.


"core functions"


import getpass
import os
import pwd
import time


from .bus import Bus
from .config import Config
from .event import Event
from .parse import parse


def __dir__():
    return (
        "Config",
        "boot",
        "kcmd",
        "privileges",
        "root"
    )


class Config(Config):

    console = False
    daemon = False
    debug = False
    index = 0
    otxt = ""
    txt = ""
    verbose = False
    workdir = ""


def boot(txt):
    parse(Config, txt)
    Config.console = "c" in Config.opts
    Config.daemon = "d" in Config.opts
    Config.verbose = "v" in Config.opts
    Config.debug = "z" in Config.opts


def kcmd(clt, txt):
    if not txt:
        return False
    Bus.add(clt)
    e = Event()
    e.channel = ""
    e.orig = repr(clt)
    e.txt = txt
    clt.handle(e)
    e.wait()
    return e.result


def privileges(name=None):
    if os.getuid() != 0:
        return
    if name is None:
        try:
            name = getpass.getuser()
        except KeyError:
            pass
    try:
        pwnam = pwd.getpwnam(name)
    except KeyError:
        return False
    os.setgroups([])
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)
    os.umask(0o22)
    return True


def root():
    if os.geteuid() != 0:
        return False
    return True


def wait():
    while 1:
        time.sleep(1.0)
