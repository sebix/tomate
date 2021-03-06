from wiring import Interface


class TrayIcon(Interface):
    def show(*args, **kwargs):
        pass

    def hide(*args, **kwargs):
        pass


class UI(Interface):
    widget = ""

    def run(*args, **kwargs):
        pass

    def quit(*args, **kwargs):
        pass

    def show(*args, **kwargs):
        pass

    def hide(*args, **kwargs):
        pass
