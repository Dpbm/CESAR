from random import randint
from tkinter import *
from random import randint
from time import ctime
import logging
from os import path

logger_log_file = path.join('newVersion', 'logs.log')

if(not path.exists(logger_log_file)):
    open(logger_log_file, 'w').close()


logger = logging.getLogger(__name__)

logging.basicConfig(
    filename=logger_log_file,
    level=logging.DEBUG,
    format='%(asctime)s:%(name)s:%(message)s'
)


dataMain = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '[', '{', ']', '}', ':', ';', ''', ''', '|', '\\', '<', ',', '>', '.', '?', '/', '', ' ']
key = []


class Cesar:
    def __init__(self):
        pass


class Window:
    def __init__(self, title, resizable):
        resizable_width, resizable_height = resizable

        self.window = Tk()
        self.window.title(title)
        self.window.resizable(resizable_width, resizable_height)

    def addLabel(self, text, side):
        new_label = Label(self.window, text=text)
        new_label.pack(side=side)

    def addEntry(self, width, side):
        new_entry = Entry(self.window, width=width)
        new_entry.pack(side=side)

    def addButton(self, text, command, width, height, side):
        new_button = Button(self.window, text=text, command=command,
                            width=width, height=height)
        new_button.pack(side=side)

    def runWindow(self):
        try:
            self.window.mainloop()
        except:
            logger.error(
                'An Error has been occorred - The program has been closed')
            exit(1)


def brain():
    try:
        dataTool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                    'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '[', '{', ']', '}', ':', ';', ''', ''', '|', '\\', '<', ',', '>', '.', '?', '/', '', ' ']
        counter = int(entry.get())
        data = ''

        for x in range(counter):
            x = randint(0, len(dataTool))
            key.append(x)
            for y in range(x):
                dataTool.insert(0, dataTool[-1])
                dataTool.pop()

        for x in range(len(entry1.get())):
            data += dataTool[dataMain.index(entry1.get()[x])]

        textFinal['text'] = data
        textFinal['fg'] = 'black'
        textKey['text'] = f'key: {key}'

        with open('logs.txt', 'a') as arq:
            arq.write(
                f'data: {ctime()}   text: {entry1.get()}    counter entry: {counter}    text Final: {data}  key: {key}')

    except Exception as error:
        textFinal['text'] = error
        textFinal['fg'] = 'red'


try:
    window_title = 'PyCesar'
    window_resizable = (False, False)

    window = Window(window_title, window_resizable)

    window.addLabel(text='Repetições: ', side=LEFT)
    window.addEntry(width=20, side=LEFT)
    window.addEntry(width=20, side=RIGHT)
    window.addLabel(text='Texto: ', side=RIGHT)
    window.addLabel(text=None, side=BOTTOM)
    window.addLabel(text=None, side=BOTTOM)
    window.addButton(text='Enter', command=brain,
                     width=10, height=2, side=LEFT)

    window.runWindow()

except Exception:
    logger.error('An Error has been occorred - The program has been closed')
    exit(1)
