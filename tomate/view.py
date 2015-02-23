from __future__ import unicode_literals


class IView(object):

    state = ''

    def run(self):
        pass

    def quit(self):
        pass

    def show(self):
        pass

    def hide(self):
        pass
