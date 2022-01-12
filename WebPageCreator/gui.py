import main
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import commands


def createGui(self):
    """
    creates the window gui
    :param self: the tkinter frame we'd like to create the gui in
    :return:
    """
    self.lbl_title = tk.Label(self.master, text='Title')
    self.lbl_title.grid(row=0, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lbl_body = tk.Label(self.master, text='Body')
    self.lbl_body.grid(row=2, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)

    self.txt_title = tk.Entry(self.master, text='')
    self.txt_title.grid(row=1, column=0, rowspan=1, padx=(30, 40), pady=(0, 0), sticky=N + W)

    self.text = tk.Text(self.master, height=25, width=80)

    # does have to be above the text.configure as it is used in the parameters
    self.scrolly = tk.Scrollbar(self.master)
    # not worth the trouble -_-
    # self.scrollx = tk.Scrollbar(self.master)
    self.text.configure(yscrollcommand=self.scrolly.set)
    self.text.grid(row=3, column=0, padx=(27, 0), pady=(10, 0), sticky=E + W, columnspan=5)


    self.scrolly.config(command=self.text.yview)
    self.scrolly.grid(sticky=E + N + S, column=5, row=3, pady=(10, 0))

    # not worth the trouble -_-
    # self.scrollx.config(command=self.text.xview)
    # self.scrollx.grid(sticky=E + W + S, column=5, row=2, pady=(10, 0))

    self.btn_new = tk.Button(self.master, width=15, height=2, text='New Webpage', command=lambda: commands.newPage(self))
    self.btn_new.grid(row=8, column=2, padx=(25, 0), pady=(45, 10), sticky=W)

    self.btn_commit = tk.Button(self.master, width=15, height=2, text='Commit Changes', command=lambda: commands.commitChanges(self))
    self.btn_commit.grid(row=8, column=0, padx=(35, 0), pady=(45, 10), sticky=W)

    self.btn_loadPage = tk.Button(self.master, width=15, height=2, text='Load from file', command=lambda: commands.openWebPage(self))
    self.btn_loadPage.grid(row=8, column=1, padx=(35, 0), pady=(45, 10), sticky=W)

    self.btn_brwsrOpen = tk.Button(self.master, width=15, height=2, text='Open in browser', command=lambda: commands.openInBrowser(self))
    self.btn_brwsrOpen.grid(row=8, column=3, padx=(35, 0), pady=(45, 10), sticky=W)



