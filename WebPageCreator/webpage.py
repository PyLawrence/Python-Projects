"""
when creating a new page, we will treat it as an object
this way we can create methods to modify specific parts
all changes are auto saved, currently we can modify the title and body
I really like how this was designed, except for the tkinter import..
however it was the easiest way to retain independence of this file
"""

from tkinter.filedialog import asksaveasfile
from definitions import *
import os

class WebPage:
    fileName = ""
    __bodyContent = ""
    __titleContent = ""
    defaultPage = DEFAULT_PAGE  # technically unused

    def __init__(self, fileName=None):
        if fileName is not None:
            self.fileName = fileName
        else:
            self.fileName = DEFAULT_FILENAME

        if self.fileExists(self.fileName):
            self.__loadPage()
        else:
            self.__setupNewPage()

    # these setup methods should only get called by this class
    def __setupNewPage(self):
        file = asksaveasfile(mode='w', defaultextension=".html")
        file.close()
        if file.name is not None:
            with open(file.name, "w") as f:
                f.write(self.defaultPage)
            self.fileName = file.name
        else:
            return

        # after setting up a new one, we can just use our normal loading sequence
        self.__loadPage()

    def __loadPage(self):
        with open(self.fileName, "r") as f:
            text = f.read()
            # was gonna use regex, and ALMOST considered using beautiful soup
            # but I figured I'd have some fun and figure it out
            self.__bodyContent = text.partition(BODY)[2].partition(c_BODY)[0]
            self.__titleContent = text.partition(TITLE)[2].partition(c_TITLE)[0]

    @staticmethod
    def fileExists(file):
        return os.path.exists(file)

    def printPageDetails(self):
        print("Title: {}\nBody Content: {}".format(self.__titleContent, self.__bodyContent))

    def __rebuildPage(self):
        """
        probably the weirdest way I've done this, if you're reading this, I'm sorry LOL
        I decided since an HTML file only has so many moving parts, and this is supposed to be really basic,
        I would basically cheat. when modifying from this program, everything but the title and body are static, so
        everything can be stored in variables, strung back together, and written back to the file
        :return:
        """
        dataTuple = (REBUILD_1, self.__titleContent, REBUILD_2, self.__bodyContent, REBUILD_3)
        tempPageString = "".join(dataTuple)
        with open(self.fileName, "w") as f:
            f.write(tempPageString)

    @property
    def Body(self):
        return self.__bodyContent

    @Body.setter
    def Body(self, newContent):
        self.__bodyContent = newContent
        self.__rebuildPage()

    @property
    def Title(self):
        return self.__titleContent

    @Title.setter
    def Title(self, newContent):
        self.__titleContent = newContent
        self.__rebuildPage()

if __name__ == '__main__':
    pass



