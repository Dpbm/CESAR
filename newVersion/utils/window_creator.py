from tkinter import *
from tkinter.ttk import *
from utils.logger import logger


class Window:
    def __init__(self, title, resizable):
        resizable_width, resizable_height = resizable

        self.window = Tk()
        self.window.title(title)
        self.window.resizable(resizable_width, resizable_height)

        self.widgets_ = {}

    def addLabel(self, text, name):
        new_label = Label(self.window, name=name, text=text)
        self.widgets_[name] = new_label

    def addEntry(self, name, width):
        new_entry = Entry(self.window, name=name, width=width)
        self.widgets_[name] = new_entry

    def addButton(self, text, command, width, name):
        new_button = Button(self.window, text=text, name=name, command=command,
                            width=width)
        self.widgets_[name] = new_button

    def getEntryDataByName(self, name) -> str:
        return self.widgets_[name].get()

    def setLabelTextByName(self, name, newText):
        self.widgets_[name]['text'] = newText

    def addGrid(self, name, row, column, sticky=None):
        self.widgets_[name].grid(
            row=row, column=column, pady=2, sticky=sticky)

    def runWindow(self):
        try:
            self.window.mainloop()
        except Exception:
            logger.error(
                'An Error has been occorred - The program has been closed')
            exit(1)
