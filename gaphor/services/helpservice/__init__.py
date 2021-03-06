"""About and help services. (help browser anyone?)"""


import importlib

from gi.repository import GdkPixbuf, Gtk

from gaphor import __version__
from gaphor.abc import ActionProvider, Service
from gaphor.core import action


class HelpService(Service, ActionProvider):
    def __init__(self, main_window):
        self.main_window = main_window

    def shutdown(self):
        pass

    @action(name="app.about")
    def about(self):
        builder = Gtk.Builder()
        with importlib.resources.path(
            "gaphor.services.helpservice", "about.glade"
        ) as glade_file:
            builder.add_objects_from_file(str(glade_file), ("about",))

        about = builder.get_object("about")

        about.set_version(str(__version__))

        about.set_transient_for(self.main_window.window)

        about.show_all()
        about.run()
        about.destroy()

    @action(name="app.shortcuts")
    def shortcuts(self):
        builder = Gtk.Builder()
        with importlib.resources.path(
            "gaphor.services.helpservice", "shortcuts.glade"
        ) as glade_file:
            builder.add_objects_from_file(str(glade_file), ("shortcuts-gaphor",))

        shortcuts = builder.get_object("shortcuts-gaphor")
        shortcuts.set_transient_for(self.main_window.window)

        shortcuts.show_all()
        return shortcuts
