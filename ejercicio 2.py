"""2)
Crear un programa que le permita al usuario ingresar 5 números validos (Un numero
valido es un número igual o mayor que 1) e imprimir cada vez que se ingresa un
numero si valido e invalido. Una vez finalizado el programa se debe imprimir la
cantidad de números inválidos ingresados.
Datos que debe ingresar el usuario:
numero = INT"""

lista = [] #Declaramos la lista


cont = 0
num = int (input ("Ingrese un numero : ")) 
while cont < 5: #Mientras que con sea menor a 5
 if num >= 1:
    
    print("Ingreso un numero valido")
    lista.append(num)
    
    print("")
    if cont < 4:
       num = int (input ("Ingrese un numero : ")) 
    cont=cont+1
 else:
    print("Ingreso un numero invalido")
    print("")
    if cont < 4:
       num = int (input ("Ingrese un numero : ")) 


print(lista)
