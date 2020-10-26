from tkinter import *
from math import sin
from  math import cos
from  math import tan
from  math import exp
import tkinter.font as tkFont

#Clase para la ventana
class ventanaReglaFalsa:
    def __init__(self, master):
        self.master = master
        #Titulo
        self.master.title('Regla Falsa')
        #Tamaño
        self.master.geometry('300x400')
        #Fondo
        self.master.config(bg='#49A')
        self.frame = Frame(self.master, bg ='#49A' )
        self.frame.pack()

        #Entradas
        self.entradaEntry1 = StringVar()
        self.entradaEntry2 = StringVar()
        self.entradaEntry3 = StringVar()
        self.entradaEntry4 = StringVar()
        self.resultado = StringVar()
        self.error = StringVar()

        #Etiquetas y Entrys
        fontStyle = tkFont.Font(family="Helvetica", size=12)
        self.e1 = Label(self.master, text="Ingresa la funcion: ", bg="#49A", font=fontStyle, pady=10).pack()
        self.en1 = Entry(self.master, textvariable=self.entradaEntry1).pack()
        self.e2 = Label(self.master, text="Ingresa el primer intervalo: ", bg="#49A", font=fontStyle,
                          pady=10).pack()
        self.en2 = Entry(self.master, textvariable=self.entradaEntry2).pack()
        self.e3 = Label(self.master, text="Ingresa el segundo intervalo: ", bg="#49A", font=fontStyle,
                          pady=10).pack()
        self.en3 = Entry(self.master, textvariable=self.entradaEntry3).pack()
        self.e4= Label(self.master, text="Ingresa la tolerancia: ", bg="#49A", font=fontStyle, pady=10).pack()
        self.en4 = Entry(self.master, textvariable=self.entradaEntry4).pack()
        #Boton
        self.btn1 = Button(self.master, text="Obtener raiz", width=12, height=2, command=self.castear).pack(pady=20)
        self.res = Label(self.master, textvariable=self.resultado, bg="#49A", font=fontStyle).pack()
        self.err = Label(self.master, textvariable=self.error, bg="#49A", font=fontStyle).pack()

    def castear(self):
        #Castear los valoros obtenidos
        #Funcion lambda
        self.f = lambda x: eval(self.entradaEntry1.get())
        #Flotantes
        #Primer inervalo
        self.a = float(self.entradaEntry2.get())
        #Segundo Intervalo
        self.b = float(self.entradaEntry3.get())
        #Toloreancia
        self.t = float(self.entradaEntry4.get())

        #Criterio de convergencia
        if self.f(self.a) * self.f(self.b) > 0.0:
            self.error.set('La convergencia no se cumple')
        else:
            self.reglaFalsa(self.f, self.a, self.b, self.t)

    def reglaFalsa(self,f, a, b, t):
        #Condicion
        condition = True
        iteracion = 1
        #Se rompre el ciclo cuando la condicion es falsa
        while condition:
            #Formula para xi
            raiz = a + (a - b) * f(a) / (f(b) - f(a))
            print('Iteracion %d, raiz = %0.5f y f(raiz) = %0.5f' % (iteracion,raiz,f(raiz)))
            print()
            #Asignar nuevos valores
            if f(a) * f(raiz) < 0:
                b = raiz
            else:
                a = raiz
            #Condicion de tolerancia
            condition = abs(f(raiz)) > t
            iteracion += 1
        self.resultado.set('\nLa raiz es: %0.5f' % raiz)