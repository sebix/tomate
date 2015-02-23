from __future__ import division, unicode_literals

from gi.repository import GObject
from wiring import implements, Interface

from .signals import tomate_signals

# Borrowed from Tomatoro create by Pierre Quillery.
# https://github.com/dandelionmood/Tomatoro
# Thanks Pierre!


class ITimer(Interface):

    time_ratio = ''

    time_left = ''

    def start(seconds):
        pass

    def stop():
        pass

    def finish():
        pass


@implements(ITimer)
class Timer(object):

    def __init__(self):
        self.running = False
        self.__seconds = self.__time_left = 0

    def start(self, seconds):
        self.running = True
        self.__seconds = self.__time_left = seconds

        GObject.timeout_add(1000, self.__update)

    def __update(self):
        '''Timer loop.

        Method executed every second to update the counter.
        '''
        if not self.running:
            return False

        if self.__time_left <= 0:
            return self.finish()

        return self.update()

    def update(self):
        self.__time_left -= 1

        self.emit('timer_updated')

        return True

    def finish(self):
        self.stop()

        self.emit('timer_finished')

        return False

    def stop(self):
        self.running = False
        self.__seconds = self.__time_left = 0

        return False

    @property
    def time_ratio(self):
        try:
            ratio = round(1.0 - self.__time_left / self.__seconds, 1)

        except ZeroDivisionError:
            ratio = 0

        return ratio

    @property
    def time_left(self):
        return self.__time_left

    def emit(self, signal):
        tomate_signals.emit(
            signal,
            time_left=self.time_left,
            time_ratio=self.time_ratio)
