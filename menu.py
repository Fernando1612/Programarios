from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from reglaFalsa import ventanaReglaFalsa
from ayuda import ventanaAyuda
from newtonRaphson import ventanaNewton
from factoresCuadraticos import ventanaLin



def main():
    raiz = tk.Tk()
    app = Menu(raiz)
    raiz.mainloop()

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title('Programario')
        self.master.geometry('300x400')
        self.master.config(bg='#49A')
        fontStyle = tkFont.Font(family="Helvetica", size=20)
        self.frame = Frame(self.master, bg ='#49A' )
        self.frame.pack()
        self.e1 = Label(self.master, text="Metodos numericos", bg="#49A", font=fontStyle, pady=20).pack()
        self.boton1 = Button(self.master, text="Regla Falsa", width=15, height=2, command=self.nuevaVentana1).pack(pady=15)
        self.boton2 = Button(self.master, text="Newton-Raphson", width=15, height=2,command=self.nuevaVentana3).pack(pady=15)
        self.boton3 = Button(self.master, text="Factores cuadraticos", width=15, height=2,command=self.nuevaVentana4).pack(pady=15)
        self.boton4 = Button(self.master, text="Ayuda", width=15, height=2, command=self.nuevaVentana2).pack(pady=15)

    #Ventana regla falsa
    def nuevaVentana1(self):
        self.nuevaVentana1 = Toplevel(self.master)
        self.app = ventanaReglaFalsa(self.nuevaVentana1)
    #Ventana ayuda
    def nuevaVentana2(self):
        self.nuevaVentana2 = Toplevel(self.master)
        self.app = ventanaAyuda(self.nuevaVentana2)
    #Ventana newton
    def nuevaVentana3(self):
        self.nuevaVentana3 = Toplevel(self.master)
        self.app = ventanaNewton(self.nuevaVentana3)
    #Ventana Lin
    def nuevaVentana4(self):
        self.nuevaVentana4 = Toplevel(self.master)
        self.app = ventanaLin(self.nuevaVentana4)



if __name__ == '__main__':
    main()
