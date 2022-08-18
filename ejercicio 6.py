"""6)
Permitirle al usuario ingresar un diccionario de comidas donde las claves son el 
nombre de las comidas y el valor el precio de estas. Las comidas se pueden ingresar 
infinitamente hasta que el precio de una sea 0. Una vez finalizado el ingreso, debemos
mostrarle al usuario las comidas con sus respectivos precios y permitirle elegir una y la 
cantidad que va a comer. Si la comida que eligió el usuario no existe debemos mostrar 
un error. Si la comida existe, mostrar el precio total que va a pagar.
Para cargar el diccionario, debemos utilizar un While.
Para recorrer el diccionario con sus claves y valores podemos hacer un for con dicc.items()
Para saber si existe la comida ingresada, podemos usar el método in:
if comida_ingresada in diccionario.keys():
Datos que debe ingresar el usuario:
comida = STR
cantidad = INT"""

from multiprocessing.sharedctypes import Value
ibande=0
total=0
dicc ={}
comida= str(input("Ingrese su comida: "))
comida= comida.title()
precio = int(input("Ingrese precio:"))
while precio != 0:
  dicc[comida] = precio
  comida= str(input("Ingrese su comida: "))
  comida= comida.title()
  precio = int(input("Ingrese precio:")) 


for key,value in dicc.items():
 print("Comida: ", key, " Precio: ",value)





while ibande==0:
  comida_ingresada=str(input("Elija una comida:"))
  comida_ingresada= comida_ingresada.title()
  
  if comida_ingresada in dicc.keys():
        cantidad=int(input("Cantidad de comida que va comer: "))
        total = dicc[comida_ingresada]*cantidad
        ibande=1
  else:
        print("Error, la comida ingresada NO EXISTE...")

print("Comida: ", comida_ingresada, " Precio total: ", total)



