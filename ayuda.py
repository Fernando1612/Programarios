from tkinter import *
import tkinter.font as tkFont


class ventanaAyuda:
    def __init__(self, master):
        self.master = master
        self.master.title('Regla Falsa')
        self.master.geometry('300x400')
        self.master.config(bg='#49A')
        self.frame = Frame(self.master, bg ='#49A' )
        self.frame.pack()

        #Widgets
        self.fontStyle = tkFont.Font(family="Helvetica", size=12)
        self.etiqueta2 = Label(self.master, text="Para poder "
                                             "utilizar los metodos "'\n'
                                             "deben ingresarse las funciones "'\n'
                                             "en su forma lambda para que "'\n'
                                             "python las reconozca "
                          , bg="#49A", font=self.fontStyle, pady=20).pack()

        self.etiqueta3 = Label(self.master, text="Ejemplos: ", bg="#49A", font=self.fontStyle, pady=10).pack()
        self.etiqueta4 = Label(self.master, text="La funcion: "'\n'
                                             "x^3+4x^2−10", bg="#49A", font=self.fontStyle).pack()
        self.etiqueta5 = Label(self.master, text="Se escribe: "'\n'
                                             "x**3+4*(x**2)-10", bg="#49A", font=self.fontStyle).pack()
        self.etiqueta4 = Label(self.master, text="La funcion: "'\n'
                                             "x^2+5x−9", bg="#49A", font=self.fontStyle, pady=10).pack()
        self.etiqueta5 = Label(self.master, text="Se escribe: "'\n'
                                             "x**2+5*x-9", bg="#49A", font=self.fontStyle).pack()


