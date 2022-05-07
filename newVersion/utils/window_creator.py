from tkinter import *
from utils.logger import logger


class Window:
    def __init__(self, title, resizable):
        resizable_width, resizable_height = resizable

        self.window = Tk()
        self.window.title(title)
        self.window.resizable(resizable_width, resizable_height)

        self.widgets_ = {}

    def addLabel(self, text, side, name):
        new_label = Label(self.window, name=name, text=text)
        self.widgets_[name] = new_label
        new_label.pack(side=side)

    def addEntry(self, width, name, side):
        new_entry = Entry(self.window, name=name, width=width)
        self.widgets_[name] = new_entry
        new_entry.pack(side=side)

    def addButton(self, text, command, width, height, name, side):
        new_button = Button(self.window, text=text, name=name, command=lambda: command(self.getEntryDataByName, self.setLabelTextByName),
                            width=width, height=height)
        self.widgets_[name] = new_button
        new_button.pack(side=side)

    def getEntryDataByName(self, name) -> str:
        return self.widgets_[name].get()

    def setLabelTextByName(self, name, newText):
        self.widgets_[name]['text'] = newText

    def runWindow(self):
        try:
            self.window.mainloop()
        except:
            logger.error(
                'An Error has been occorred - The program has been closed')
            exit(1)
