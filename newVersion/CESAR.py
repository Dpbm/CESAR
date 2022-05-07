from email.policy import default
from random import randint
from tkinter import LEFT, RIGHT, BOTTOM, W
from utils.window_creator import Window
from utils.logger import logger
from string import ascii_letters, punctuation, digits


class Cesar:
    def __init__(self):
        pass


def brain(getEntryDataByName, setLabelTextByName):
    try:
        repetitions = int(getEntryDataByName('entry-repetitions'))
        enter_text = getEntryDataByName('entry-text')

        final_text = ''

        default_characters = list(ascii_letters + punctuation + digits + ' ')
        characters = list(ascii_letters + punctuation + digits + ' ')
        complete_key = []

        for _ in range(repetitions):
            deslocation = randint(0, len(characters) - 1)
            characters = [*characters[deslocation:], *characters[:deslocation]]
            complete_key.append(deslocation)

        for index in enter_text:
            final_text += characters[default_characters.index(index)]

        setLabelTextByName('label-result', final_text)
        setLabelTextByName('label-key', complete_key)

    except Exception as error:
        logger.error('An Error has been occorred - Failed on encrypt')
        setLabelTextByName('label-result', 'Error, please try another time')


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

    window.addLabel(text=None,  name='label-key')
    window.addLabel(text=None,  name='label-result')

    window.addGrid(name='label-key', column=0, row=2)
    window.addGrid(name='label-result', column=0, row=3)

    window.addButton(text='Enter', command=brain,
                     width=10, name='button-enter')
    window.addGrid(name='button-enter', column=0, row=4)
    window.runWindow()

except Exception:
    logger.error('An Error has been occorred - The program has been closed')
    exit(1)
