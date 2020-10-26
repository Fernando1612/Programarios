from sympy import sin
import sympy as sy
#x es un simbolo
x=sy.symbols('x')
#funcion original
funcion=((1/2)*sin(x))-x+2
#primera derivada de la funcion
onederivada=sy.diff(funcion,x)
#Segunda derivada de la funcion
twoderivada=sy.diff(onederivada, x)
#Intervalo que converge a+b/2 donde a= 2 y b=3
x_0=2.5
#Le damos valor a xr
xr=x_0

#se subtituye x por xr a continuandicon se evalua
fx=funcion.evalf(subs={x: xr})
#primera derivada  numerica
oneD=onederivada.evalf(subs={x: xr})
#Segunda derivada numerica
twoD=twoderivada.evalf(subs={x: xr})
#Metodo de convergencia
X0=abs((fx*twoD)/(oneD*oneD))
#Solo es un salto de linea
print("")
#Nos muestra la funcion
print("La funcion es: ", funcion)
#Muestra La primera derivada
print("La primera derivada es: ", onederivada)
#Muestra la segunda derivada
print("La segunda derivada es: ", twoderivada)
#Muestra valor de convergencia X0<1 para que converga
print("Valor de la convergencia: ",X0,"\n")
#Asignamos valores iniciales solo para que el programa no marque error
Eabs=100/100
contador=0
#Datos de la tabla
print("--------------------------------------------------------------------------------------------------------------------")
print("| i  |\t\t\txi\t\t\t|\t\t\tf(x)\t\t\t|\t\tf'(x)\t\t\t|\teabs")
print("--------------------------------------------------------------------------------------------------------------------")
#Iniciamos con las iteraciones
while Eabs>0:
#Nuevo valor de xi en otras palabras x(i+1)
    xa=xr
#Nueva funcion numerica
    nuevafx=funcion.evalf(subs={x: xr})
#Nueva primera derivada numerica
    nuevafxuno=onederivada.evalf(subs={x: xr})
#Aplicando Metodo de Newton Rapshon 
    M_Newton_R=x-(funcion/onederivada)
#Asignando nuevo valor de xi
    xr=M_Newton_R.evalf(subs={x: xr})
#Obteniendo el error absoluto
    Eabs=abs(xr-xa)
#Impresion de los datos obtenidos
    print("| ",contador,"|","{:.14f}".format(xa),"\t|","{:.20f}".format(nuevafx),"\t|","{:.14f}".format(nuevafxuno),"\t|",Eabs)
    print("--------------------------------------------------------------------------------------------------------------------")
#Controlador de iteraciones
    contador+=1