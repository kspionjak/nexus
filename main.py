import gi
import time

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Nexus():
  def __init__(self):
    self.builder = Gtk.Builder()
    self.builder.add_from_file("nexus.glade")
    self.builder.connect_signals(self)

    self.windowMain = self.builder.get_object("window_main")
    self.windowAbout = self.builder.get_object("window_about")
    self.windowMain.show()  

    # display time
    self.timeDisplay = self.builder.get_object("time_display")
    self.timeDisplay.show()

    # current time
    time_now = time.strftime('%H:%M:%S')

  def on_window_main_destroy(self, widget, data=None):
    Gtk.main_quit()

  def on_file_quit_activate(self, menuitem, data=None):
    Gtk.main_quit()
  
  def on_help_about_activate(self, menuitem, data=None):
    self.response = self.windowAbout.run()
    self.windowAbout.hide()

  def main(self):
    Gtk.main()

if __name__ == "__main__":
  application = Nexus()
  application.main()