"""
WebPage Generator
Creates all the necessary tags and adjustments in HTML
User just needs to add the content
"""

from tkinter import *
import tkinter as tk

import gui


class ParentWindow(Frame):
    # I don't like these but I needed a consistent reference to my webpage object
    webPageRef = None
    TitleRef = ""
    BodyRef = ""

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master

        self.master.geometry("700x600")

        self.master.resizable(False, False)
        self.master.title("Test")
        self.master.configure(bg="#F0F0F0")

        # self.master.protocol("WM_DELETE_WINDOW", lambda: func.ask_quit(self))
        arg = self.master


        gui.createGui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


