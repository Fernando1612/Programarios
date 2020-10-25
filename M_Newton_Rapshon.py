from sympy import sin
import sympy as sy
#x es un simbolo
x=sy.symbols('x')
#funcion 
funcion=((1/2)*sin(x))-x+2
#primera derivada de la funcion
onederivada=sy.diff(funcion,x)
#Segunda derivada
twoderivada=sy.diff(onederivada, x)
#Valor en el cual converge la funcion a+b/2
x_0=2.5
xr=x_0

#se subtituye x por xr a continuandicon se evalua
fx=funcion.evalf(subs={x: xr})
#Primera derivada valuada numericamente
oneD=onederivada.evalf(subs={x: xr})
#segunda derivada valuada numericamente
twoD=twoderivada.evalf(subs={x: xr})
#Metodo de convergencia
X0=abs((fx*twoD)/(oneD**2))
#print("Valor de la convergencia: ",fx,"\n")
#iteraciones
Eabs=100/100
#Dando valor al contador
contador=0

print("i\t|xi\t\t\t|eabs|")
#Verificando que el valor absoluto sea menor a cerp
while Eabs>0:
    #Xi-1 es decir el anterior
    xa=xr
    #Numero de iteraciones
    contador+=1
    #Metodo de Newton Rapshon
    M_Newton_R=x-(funcion/onederivada)
    #Numero valor de Xi
    xr=M_Newton_R.evalf(subs={x: xr})
    #Nueva funcion valuada
    nuevafx=funcion.evalf(subs={x: xr})
    #Error absoluto
    Eabs=abs(xr-xa)
print("Iteracion: ",contador,"\t|","Raiz: ",xa,"\t|","Error: ",Eabs,"|")