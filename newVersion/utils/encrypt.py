from string import ascii_letters, punctuation, digits
from utils.checkInteger import checkInteger
from random import randint
from utils.logger import logger
from time import ctime


class Cesar:
    def __init__(self, getEntryDataByName, setLabelTextByName):
        self.final_text = ''
        self.complete_key = []
        self.default_characters = list(
            ascii_letters + punctuation + digits + ' ')
        self.characters = list(ascii_letters + punctuation + digits + ' ')
        self.repetitions = checkInteger(
            getEntryDataByName('entry-repetitions'))
        self.enter_text = getEntryDataByName('entry-text')

        self.getEntryDataByName = getEntryDataByName
        self.setLabelTextByName = setLabelTextByName

    def calculate(self):
        try:

            for _ in range(self.repetitions):
                deslocation = randint(0, len(self.characters) - 1)
                self.characters = [
                    *self.characters[deslocation:], *self.characters[:deslocation]]
                self.complete_key.append(deslocation)

            for index in self.enter_text:
                self.final_text += self.characters[self.default_characters.index(
                    index)]

            encrypted_message_file = open('encrypted.txt', 'a')
            encrypted_message_file.write(
                f'\n---Encrypted Message---\ndate: {ctime()}\n key: {self.complete_key}\nencryped: {self.final_text}\n-----------------------\n')
            encrypted_message_file.close()

            logger.info('Created a new encrypted text')
            self.setLabelTextByName(
                'label-result', 'Done, check the encrypted.txt file')

        except Exception:
            logger.error('An Error has been occorred - Failed on encrypt')
            self.setLabelTextByName(
                'label-result', 'Error, please try another time')
