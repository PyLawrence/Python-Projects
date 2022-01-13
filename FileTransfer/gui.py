from tkinter import *
import tkinter as tk
import commands


def createGui(self):
    """
    creates the window gui
    :param self: the tkinter frame we'd like to create the gui in
    :return:
    """
    self.lbl_From = tk.Label(self.master, text='From Folder')
    self.lbl_From.grid(row=0, column=1, padx=(5, 0), pady=(10, 0), sticky=N + W)

    self.lbl_body = tk.Label(self.master, text='To Folder')
    self.lbl_body.grid(row=2, column=1, padx=(5, 0), pady=(10, 0), sticky=N + W)

    self.lbl_ext = tk.Label(self.master, text='Extension')
    self.lbl_ext.grid(row=4, column=1, padx=(5, 0), pady=(10, 0), sticky=N + W)

    self.from_entry = tk.Entry(self.master, text='', width=40, font="Helvetica 10")
    self.from_entry.grid(row=1, column=1, columnspan=5, padx=(5, 40), ipady=3, sticky=E)
    #
    self.to_entry = tk.Entry(self.master, text='', width=40, font="Helvetica 10")
    self.to_entry.grid(row=3, column=1, columnspan=5, padx=(5, 40), ipady=3, sticky=E)


    self.ext_comp = tk.Entry(self.master, text='', width=40, font="Helvetica 10")
    self.ext_comp.grid(row=5, column=1, columnspan=5, padx=(5, 40), ipady=3, sticky=E)
    self.ext_comp.insert(0, '.txt')


    #
    #
    # self.btn_new = tk.Button(self.master, width=15, height=2, text='New Webpage', command=lambda x: x)
    # self.btn_new.grid(row=2, column=0, padx=(25, 0), pady=(45, 10), sticky=W)
    #
    self.setExt = tk.Button(self.master, width=10, height=1, text='Set Ext', command=lambda: commands.updateExtComp(self))
    self.setExt.grid(row=5, column=0, padx=(15, 0), sticky=W)

    self.btn_fromFolder = tk.Button(self.master, width=10, height=1, text='Location', command=lambda: commands.getStartingFolder(self))
    self.btn_fromFolder.grid(row=1, column=0, padx=(15, 0), sticky=W)
    #
    self.btn_loadPage = tk.Button(self.master, width=10, height=1, text='Location', command=lambda: commands.getResultingFolder(self))
    self.btn_loadPage.grid(row=3, column=0, padx=(15, 0), sticky=W)

    self.autoRun = tk.Button(self.master, width=15, height=1, text='Auto: Enabled', command=lambda: commands.enableDisableSchedule(self))
    self.autoRun.grid(row=6, column=1, padx=(15, 0), sticky=W)

    self.Frequencybtn = tk.Button(self.master, width=15, height=1, text='Frequency: Day', command=lambda: commands.updateFrequency(self))
    self.Frequencybtn.grid(row=7, column=1, padx=(15, 0), sticky=W)

    self.manualRun = tk.Button(self.master, width=10, height=1, text='Manual', command=lambda: commands.transferFiles(self))
    self.manualRun.grid(row=6, column=4, padx=(15, 0), pady=(10, 10), sticky=W)

    self.lbl_Status = tk.Label(self.master, text='Status:')
    self.lbl_Status.grid(row=7, column=4, padx=(15, 0), pady=(10, 0), sticky=N + W)

    #
    # self.btn_brwsrOpen = tk.Button(self.master, width=15, height=2, text='Open in browser', command=lambda x: x)
    # self.btn_brwsrOpen.grid(row=8, column=3, padx=(35, 0), pady=(45, 10), sticky=W)



