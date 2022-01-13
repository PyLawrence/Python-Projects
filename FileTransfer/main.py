"""

"""

from tkinter import *
import tkinter as tk
import commands
import gui

class ParentWindow(Frame):
    fromLocation = ""
    toLocation = ""
    fileExt = ".txt"
    AutoEnabled = True
    currentSchedule = None
    scheduleThread = None
    # currently not scalable, only has 2 available frequencies
    # True is daily, False is every second
    Frequency = True

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master

        self.master.geometry("425x300")

        self.master.resizable(False, False)
        self.master.title("AutoFileTransfer")
        self.master.configure(bg="#F0F0F0")
        # since I had to close out the thread, we needed manual functionality
        self.master.protocol("WM_DELETE_WINDOW", lambda: commands.closeWindow(self))

        gui.createGui(self)

        # it will attempt to auto run by default
        commands.defaultSchedule(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

