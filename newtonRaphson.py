from tkinter import *
from math import sin
from math import cos
from sympy import sin
from math import tan
from math import exp
from sympy.parsing.sympy_parser import parse_expr
import tkinter.font as tkFont
import sympy as sy


class ventanaNewton:
    def __init__(self, master):
        self.master = master
        self.master.title('Newton-Raphson')
        self.master.geometry('300x400')
        self.master.config(bg='#49A')
        self.frame = Frame(self.master, bg ='#49A' )
        self.frame.pack()

        #Entradas
        self.entradaEntry1 = StringVar()
        self.entradaEntry2 = StringVar()
        self.entradaEntry3 = StringVar()
        self.resultado = StringVar()
        self.error = StringVar()

        # Etiquetas y Entrys
        fontStyle = tkFont.Font(family="Helvetica", size=12)
        self.e1 = Label(self.master, text="Ingresa la funcion: ", bg="#49A", font=fontStyle, pady=10).pack()
        self.en1 = Entry(self.master, textvariable=self.entradaEntry1).pack()
        self.e2 = Label(self.master, text="Ingresa la aproximacion: ", bg="#49A", font=fontStyle,
                        pady=10).pack()
        self.en2 = Entry(self.master, textvariable=self.entradaEntry2).pack()
        # Boton
        self.btn1 = Button(self.master, text="Obtener raiz", width=12, height=2,command=self.entrada).pack(pady=20)
        self.res = Label(self.master, textvariable=self.resultado, bg="#49A", font=fontStyle).pack()
        self.err = Label(self.master, textvariable=self.error, bg="#49A", font=fontStyle).pack()

    def entrada(self):
        #Castear los valoros obtenidos
        self.f = self.entradaEntry1.get()
        #Flotantes
        #Aproximacion
        self.a = float(self.entradaEntry2.get())
        self.newton_Raphson(self.f, self.a)



    def newton_Raphson(self,f,a):
        #Parse de la funcion
        funcion = parse_expr(f)
        # x es un simbolo
        x = sy.symbols('x')
        # primera derivada de la funcion
        df = sy.diff(funcion,x)
        # Segunda derivada
        df2 = sy.diff(df,x)
        # Valor en el cual converge la funcion
        xr = a

        # se subtituye x por xr a continuandicon se evalua
        fx = funcion.evalf(subs={x: xr})
        # Primera derivada valuada numericamente
        oneD = df.evalf(subs={x: xr})
        # segunda derivada valuada numericamente
        twoD = df2.evalf(subs={x: xr})
        # Metodo de convergencia
        X0 = abs((fx * twoD) / (oneD * oneD))
        # Solo es un salto de linea
        print("")
        # Nos muestra la funcion
        print("La funcion es: ", funcion)
        # Muestra La primera derivada
        print("La primera derivada es: ", df)
        # Muestra la segunda derivada
        print("La segunda derivada es: ", df2)
        # Muestra valor de convergencia X0<1 para que converga
        print("Valor de la convergencia: ", X0, "\n")
        # Asignamos valores iniciales solo para que el programa no marque error
        Eabs = 100 / 100
        contador = 0

        # Datos de la tabla
        print(
            "--------------------------------------------------------------------------------------------------------------------")
        print("| i  |\t\t\txi\t\t\t|\t\t\tf(x)\t\t\t|\t\tf'(x)\t\t\t|\teabs")
        print(
            "--------------------------------------------------------------------------------------------------------------------")
        # Iniciamos con las iteraciones
        while Eabs > 0:
            # Nuevo valor de xi en otras palabras x(i+1)
            xa = xr
            # Nueva funcion numerica
            nuevafx = funcion.evalf(subs={x: xr})
            # Nueva primera derivada numerica
            nuevafxuno = df.evalf(subs={x: xr})
            # Aplicando Metodo de Newton Rapshon
            M_Newton_R = x - (funcion / df)
            # Asignando nuevo valor de xi
            xr = M_Newton_R.evalf(subs={x: xr})
            # Obteniendo el error absoluto
            Eabs = abs(xr - xa)
            # Impresion de los datos obtenidos
            print("| ", contador, "|", "{:.14f}".format(xa), "\t|", "{:.20f}".format(nuevafx), "\t|","{:.14f}".format(nuevafxuno), "\t|", Eabs)
            print("--------------------------------------------------------------------------------------------------------------------")
            # Controlador de iteraciones
            contador += 1
        self.resultado.set('\nLa raiz es: %0.5f' % xa)
