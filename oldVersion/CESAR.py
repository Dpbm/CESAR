from random import randint
from tkinter import *
from time import sleep


class principal(object):
    def __init__(self):

        def logica():
            self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                             "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            self.errados = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*",
                            "(", ")", "_", "-", "+", "=", "[", "{", "]", "}", ":", ";", '"', '"', "|", "\\", "<", ",", ">", ".", "?", "/"]
            self.contador = 0

            print(len(self.entry1.get()))

            self.lista_invalidos = []
            self.lista_vazio = []

            for self.c in range(0, len(self.entry1.get())):

                if ((self.entry1.get()[self.c]) in (self.errados)):
                    if ((self.entry1.get()[self.c]) in (self.lista_invalidos)):
                        pass
                    elif (self.entry1.get()[self.c] == ''):
                        self.lista_vazio.append()

                    else:
                        if (self.entry1.get()[self.c] in self.errados):
                            self.lista_invalidos.append(
                                self.entry1.get()[self.c])
                            self.incorretos['text'] = (f'invalidos = ')
                            self.incorretos2['text'] = (self.lista_invalidos)

                        elif (self.entry1.get()[self.c] == ' '):
                            self.lista_vazio.append(' ')
                            if (len(self.entry1.get()) == len(self.lista_vazio)):
                                self.incorretos['text'] = (' ')
                                self.incorretos2['text'] = (' ')

                else:
                    self.incorretos['text'] = ('')
                    self.incorretos2['text'] = ('')

        # cria uma janela com a instacia de TK
        self.janela = Tk()

        # cria um titulo
        self.janela.title("cifra de Cesar")

        # faz com que o tamanho da janela nao seja modificavel
        self.janela.resizable(False, False)

        self.label = Label(self.janela, text="repeticoes: ")
        self.label.pack(side=LEFT)

        self.entry = Entry(self.janela)
        self.entry.pack(side=LEFT)

        self.incorretos2 = Label(self.janela, text="", fg="red")
        self.incorretos2.pack(side=RIGHT)

        self.incorretos = Label(self.janela, text="", fg="red")
        self.incorretos.pack(side=RIGHT)

        self.entry1 = Entry(self.janela)
        self.entry1.pack(side=RIGHT)

        self.label1 = Label(self.janela, text="texto: ")
        self.label1.pack(side=RIGHT)

        self.button = Button(self.janela, text="enter",
                             command=logica, width=10, height=2)
        self.button.pack(side=LEFT)

        self.janela.mainloop()


principal()
