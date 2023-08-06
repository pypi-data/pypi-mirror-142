# This file is placed in the Public Domain.


"repeaters"


from .timer import Timer
from .thread import launch


def __dir__():
    return (
        "Repeater",
    )


class Repeater(Timer):

    def run(self):
        thr = launch(self.start)
        super().run()
        return thr
