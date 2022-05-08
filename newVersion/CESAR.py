from tkinter import W
from utils.encrypt import Cesar
from utils.window_creator import Window
from utils.logger import logger


try:
    window_title = 'PyCesar'
    window_resizable = (False, False)

    window = Window(window_title, window_resizable)

    window.addLabel(text='Repetitions: ', name='label-repetitions')
    window.addLabel(text='Text: ', name='label-text')

    window.addEntry(width=20, name='entry-repetitions')
    window.addEntry(width=20, name='entry-text')

    window.addGrid(name='label-repetitions', column=0, row=0, sticky=W)
    window.addGrid(name='label-text', column=0, row=1, sticky=W)

    window.addGrid(name='entry-repetitions', column=1, row=0)
    window.addGrid(name='entry-text', column=1, row=1)

    window.addLabel(text=None,  name='label-result')

    window.addGrid(name='label-result', column=0, row=2)

    window.addButton(text='Enter', command=lambda: Cesar(window.getEntryDataByName, window.setLabelTextByName).calculate(),
                     width=10, name='button-enter')
    window.addGrid(name='button-enter', column=0, row=3)
    window.runWindow()

except Exception:
    logger.error('An Error has been occorred - The program has been closed')
    exit(1)
