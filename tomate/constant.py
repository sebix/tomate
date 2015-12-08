from __future__ import unicode_literals

import enum


@enum.unique
class Base(enum.Enum):

    @classmethod
    def by_index(cls, number):
        for (index, attr) in enumerate(cls):
            if index == number:
                return attr


class Task(Base):
    pomodoro = 0
    shortbreak = 1
    longbreak = 2


class State(Base):
    stopped = 0
    started = 1
    finished = 3
    changed = 4
    showing = 5
    hiding = 6
    reset = 7