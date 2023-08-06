# This file is placed in the Public Domain.


"object programming tests"


import inspect
import os
import sys
import unittest


from bot.object import Object, keys, values
from bot.table import Table


import bot.table


Table.add(bot.table)


class Test_Table(unittest.TestCase):

    def test_mod(self):
        self.assertTrue("bot.table" in keys(Table.mod))
