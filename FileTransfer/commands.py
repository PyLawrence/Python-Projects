import os
from tkinter import filedialog
# schedule module is not included with python
import schedule
import time
import threading
import shutil



def updateExtComp(self):
    self.fileExt = self.ext_comp.get()

def transferFiles(self):
    try:
        file_names = os.listdir(self.fromLocation)

        matchedFiles = 0
        for file_name in file_names:
            if self.fileExt in file_name:
                matchedFiles += 1
                shutil.move(os.path.join(self.fromLocation, file_name), self.toLocation)
        # when the function fires, the status will update
        # if the function found files, it will move them and and state it was successful
        # cleared means it worked, however there were no files to move
        if matchedFiles > 0:
            self.lbl_Status['text'] = "Status: Success"
        else:
            self.lbl_Status['text'] = "Status: Cleared"

    except FileNotFoundError:
        self.lbl_Status['text'] = "Status: Error"
    except:
        self.lbl_Status['text'] = "Status: Error"

def enableDisableSchedule(self):
    if self.AutoEnabled is True:
        # don't change to false in here as it is handled in cancelSchedule
        cancelSchedule(self)
        self.autoRun['text'] = "Auto: Disabled"
    else:
        self.AutoEnabled = True
        defaultSchedule(self)
        self.autoRun['text'] = "Auto: Enabled"


def defaultSchedule(self, freq=True):
    # create a schedule thread and pass frequency
    self.scheduleThread = threading.Thread(target=scheduleThreadFunc, args=(self, freq))
    self.scheduleThread.start()

def scheduleThreadFunc(self, freq=True):
    if freq:
        # pretty self explanatory, run transferFiles every day at 10:30(AM, consider military time)
        schedule.every().day.at("10:30").do(transferFiles, self)
    else:
        # run every second, only used for testing tbh so that we can verify it works.  Default is daily
        self.currentSchedule = schedule.every().second.do(transferFiles, self)
    while self.AutoEnabled:
        # run at scheduled times, sleep so that the program doesn't eat up our resources
        # now technically since it would be running once a day, we could sleep longer
        # this could potentially free up more resources when this thread isn't otherwise doing anything
        schedule.run_pending()
        time.sleep(1)

# this will have to get called when we exit the program as well
def cancelSchedule(self):
    schedule.cancel_job(self.currentSchedule)
    # setting here to avoid having to call it 20 times
    self.AutoEnabled = False
    # if the thread is alive, we need to kill it
    # quitting the program doesn't auto delete threads
    if self.scheduleThread.is_alive():
        self.scheduleThread.join()


def getStartingFolder(self):
    directory = filedialog.askdirectory()

    if directory:
        self.fromLocation = directory
        updateFromTextBox(self, directory)
    # if we don't select one, we don't want to change anything

def updateFromTextBox(self, dirStr):
    self.from_entry.delete(0, "end")
    self.from_entry.insert(0, dirStr)

def getResultingFolder(self):
    directory = filedialog.askdirectory()

    if directory:
        self.toLocation = directory
        updateToTextBox(self, directory)

def updateToTextBox(self, dirStr):
    self.to_entry.delete(0, "end")
    self.to_entry.insert(0, dirStr)

def closeWindow(self):
    # cancelling so that we can free up resources
    cancelSchedule(self)
    os._exit(0)


def updateFrequency(self):
    # cancel the currently active schedule, then doing a new schedule with the correct frequency
    cancelSchedule(self)
    time.sleep(0.5)
    self.AutoEnabled = True
    # default is True, use daily
    if self.Frequency:
        defaultSchedule(self, False)
        self.Frequencybtn['text'] = "Frequency: Second"
        self.Frequency = False
    # every second
    else:
        defaultSchedule(self)
        self.Frequencybtn['text'] = "Frequency: Day"
        self.Frequency = True


