"""
Commands for the webpage creator
"""
import os
from tkinter import filedialog
import webpage

def openWebPage(self):
    file_path = filedialog.askopenfilename(filetypes=(("html files", "*.html"), ("all files", "*.*")))
    if file_path != "":
        if file_path is not None:
            temp = webpage.WebPage(file_path)
            self.webPageRef = temp
            self.TitleRef = temp.Title
            self.BodyRef = temp.Body
            self.txt_title.delete(0, "end")
            self.txt_title.insert(0, temp.Title)
            self.text.delete("1.0", "end")
            self.text.insert("1.0", temp.Body)


    return None

def commitChanges(self):
    """
    button should call this function
    this function will update the title and body of a webpage
    :return:
    """
    self.webPageRef.Title = self.txt_title.get()
    self.webPageRef.Body = self.text.get("1.0", "end")

def newPage(self):
    temp = webpage.WebPage()
    self.webPageRef = temp
    self.TitleRef = temp.Title
    self.BodyRef = temp.Body
    self.txt_title.delete(0, "end")
    self.txt_title.insert(0, temp.Title)
    self.text.delete("1.0", "end")
    self.text.insert("1.0", temp.Body)

def openInBrowser(self):
    os.startfile(self.webPageRef.fileName)


if __name__ == "__main__":
    pass


