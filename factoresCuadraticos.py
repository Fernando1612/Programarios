from tkinter import *
from tkinter import ttk
from math import sin
from  math import cos
from  math import tan
from  math import exp
import tkinter.font as tkFont
import tkinter as tk

#Clase para la ventana
class ventanaLin:
    def __init__(self, master):
        self.master = master
        #Titulo
        self.master.title('Factores cuadraticos ')
        #Tamaño
        self.master.geometry('300x400')
        #Fondo
        self.master.config(bg='#49A')
        self.frame = Frame(self.master, bg ='#49A' )
        self.frame.pack()