"""4)
Ingresar una cadena y devolver al usuario si la cadena está escrita en mayúsculas,
minúsculas o una mezcla de ambas.
Datos que debe ingresar el usuario:
cadena = STR"""
ibande=0
cad= str(input("Ingrese una cadena: "))
while ibande == 0:
  if cad.isalpha():

     if cad.isupper():
           print("La cadena esta en mayusculas")
           ibande=1
     else:
           if cad.islower():
               print("La cadena esta en minusculas")
               ibande=1
           else:
               print("La cadena contiene mezcla de mayusculas y minusculas ")
               ibande=1
  else:
        print("Ingrese una cadena valida.")
        ibande=0
        cad= str(input("Ingrese una cadena: "))