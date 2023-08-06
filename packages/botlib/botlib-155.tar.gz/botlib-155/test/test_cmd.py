# This file is placed in the Public Domain.


"command tests"


import inspect
import random
import unittest


from bot.callback import Callback
from bot.cls import Class
from bot.command import Command
from bot.event import Event
from bot.function import format
from bot.handler import Handler, dispatch
from bot.kernel import Config
from bot.object import Object, get, keys, values
from bot.parse import aliases
from bot.table import Table
from bot.thread import launch


events = []
cmds = "commands,delete,display,fetch,find,fleet,log,meet,more,remove,rss,threads,todo"


param = Object()
param.commands = [""]
param.config = ["nick=opbot", "server=localhost", "port=6699"]
#param.delete = ["root@shell", "test@user"]
param.display = ["reddit title,summary,link", ""]
param.fetch = [""]
param.find = ["log", "log txt==test", "rss", "rss rss==reddit", "config server==localhost"]
param.fleet = ["0", ""]
param.log = ["test1", "test2"]
param.meet = ["root@shell", "test@user"]
param.more = [""]
param.nick = ["opb", "opbot", "op_"]
param.password = ["bart blabla"]
#param.remove = ["reddit", ""]
param.rss = ["https://www.reddit.com/r/python/.rss"]
param.todo = ["things todo"]


class CLI(Handler):

     def __init__(self):
         Handler.__init__(self)

     def raw(self, txt):
         if Config.verbose:
             print(txt)
        
         
c = CLI()
c.start()

def consume(events):
    fixed = []
    res = []
    for e in events:
        e.wait()
        fixed.append(e)
    for f in fixed:
        try:
            events.remove(f)
        except ValueError:
            continue
    return res


class Test_Commands(unittest.TestCase):

    #def setUp(self):
    #    c.start()
        
    #def tearDown(self):
    #    c.stop()

    def test_commands(self):
        cmds = sorted(Command.cmd)
        random.shuffle(cmds)
        for cmd in cmds:
            for ex in get(param, cmd, [""]):
                e = Event()
                e.txt = cmd + " " + ex
                e.orig = repr(c)
                launch(Callback.callback(e))
                events.append(e)
        for cmd in keys(aliases):
            for ex in get(param, cmd, [""]):
                e = Event()
                e.txt = cmd + " " + ex
                e.orig = repr(c)
                launch(Callback.callback(e))
                events.append(e)
        consume(events)
        self.assertTrue(not events)
