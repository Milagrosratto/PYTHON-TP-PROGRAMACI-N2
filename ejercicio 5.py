"""5)
A partir de la lista:
numeros = [3, 8, 21, 17, 12, 20, 86, 71, 39]
Crear una lista llamada numeros_pares que contenga todos los números pares y una
lista numeros_impares que contenga los números impares, una vez finalizado el
programa debemos mostrarle al usuario la cantidad de números en ambas listas.
“En la lista numeros_pares hay X numeros”
“En la lista numeros_impares hay X numeros”
Para saber si un numero es par podemos usar la siguiente formula if (numero % 2 == 0) par"""




numeros = [3, 8, 21, 17, 12, 20, 86, 71, 39]
numeros_pares = []
numeros_impares = []
num=0

for x in range(0,9):
      num = numeros[x]
      if (num % 2 == 0):
            numeros_pares.append(num) 
      else: 
            numeros_impares.append(num) 

canti_par= str(len(numeros_pares))
canti_impar= str(len(numeros_impares))
print("Numeros :", numeros_pares)
print("En la lista numeros_pares hay "+ canti_par +" numeros")
print(" ")
print("Numeros impares:", numeros_impares)
print("En la lista numeros_impares hay "+ canti_impar +" numeros")