from __future__ import unicode_literals

import logging

from tomate.dispatcher import Dispatcher

logger = logging.getLogger(__name__)

tomate_signals = Dispatcher()

# Timer
timer_updated = tomate_signals.signal('timer_updated')
timer_finished = tomate_signals.signal('timer_finished')

# Pomodoro
start_session = tomate_signals.signal('start_session')
session_started = tomate_signals.signal('session_started')

reset_sessions = tomate_signals.signal('reset_sessions')
sessions_reseted = tomate_signals.signal('sessions_reseted')

interrupt_session = tomate_signals.signal('interrupt_session')
session_interrupted = tomate_signals.signal('session_interrupted')

session_ended = tomate_signals.signal('session_ended')

change_task = tomate_signals.signal('change_task')
task_changed = tomate_signals.signal('task_changed')

app_exit = tomate_signals.signal('app_exit')

# Window
window_visible = tomate_signals.signal('window_visibility_changed')

# Settings
session_duration_changed = tomate_signals.signal('session_duration_changed')


class ConnectSignalMixin(object):

    signals = ()

    def connect_signals(self):
        for (signal, method) in self.signals:
            tomate_signals.connect(signal, getattr(self, method))

            logger.debug('method %s.%s connect to signal %s.',
                         self.__class__.__name__, method, signal)

    def disconnect_signals(self):
        for (signal, method) in self.signals:
            tomate_signals.disconnect(signal, getattr(self, method))

            logger.debug('method %s.%s disconnect from signal %s.',
                         self.__class__.__name__, method, signal)
