from email.policy import default
from random import randint
from tkinter import LEFT, RIGHT, BOTTOM
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
        print(error)
        logger.error('An Error has been occorred - Failed on encrypt')
        setLabelTextByName('label-result', 'Error, please try another time')


try:
    window_title = 'PyCesar'
    window_resizable = (False, False)

    window = Window(window_title, window_resizable)

    window.addLabel(text='Repetitions: ', side=LEFT, name='label-repetitions')
    window.addEntry(width=20, side=LEFT, name='entry-repetitions')
    window.addEntry(width=20, side=RIGHT, name='entry-text')
    window.addLabel(text='Text: ', side=RIGHT, name='label-text')
    window.addLabel(text=None, side=BOTTOM,  name='label-key')
    window.addLabel(text=None, side=BOTTOM, name='label-result')
    window.addButton(text='Enter', command=brain,
                     width=10, height=2, side=LEFT, name='button-enter')

    window.runWindow()

except Exception:
    logger.error('An Error has been occorred - The program has been closed')
    exit(1)
