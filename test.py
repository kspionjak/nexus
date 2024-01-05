import gi
from datetime import datetime

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

class MainWindow(Gtk.Window):
  
  def __init__(self):
    Gtk.Window.__init__(self, title="Time App")

    self.box = Gtk.Box(spacing=6)
    self.add(self.box)

    self.label = Gtk.Label()
    self.box.pack_start(self.label, True, True, 0)
  
  def displayclock(self):
    datetimenow = str(datetime.now())
    self.label.set_label(datetimenow)
    return True
  
  def startclocktimer(self):
    GObject.timeout_add(1000, self.displayclock)

win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
win.startclocktimer()
Gtk.main()
