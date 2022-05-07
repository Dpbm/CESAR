from random import randint
from tkinter import *
from random import randint
from time import ctime

dataMain = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '[', '{', ']', '}', ':', ';', ''', ''', '|', '\\', '<', ',', '>', '.', '?', '/', '', ' ']
key = []


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
    window = Tk()
    window.title('cifra de Cesar modificado')

    window.resizable(False, False)

    label = Label(window, text='repeticoes: ')
    label.pack(side=LEFT)

    entry = Entry(window, width=20)
    entry.pack(side=LEFT)

    entry1 = Entry(window, width=20)
    entry1.pack(side=RIGHT)

    label1 = Label(window, text='texto: ')
    label1.pack(side=RIGHT)

    textKey = Label(window, text=None)
    textKey.pack(side=BOTTOM)

    textFinal = Label(window, text=None, fg='black')
    textFinal.pack(side=BOTTOM)

    button = Button(window, text='enter', command=brain, width=10, height=2)
    button.pack(side=LEFT)

    window.mainloop()

except KeyboardInterrupt:
    exit()
