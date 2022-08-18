def eliminar_lista(lista1,lista2):
  for item in lista1:
        if (item in lista2):
              lista1.remove(item)
                 
    
  return lista1
  


lista_1=[]
lista_2=[]
lista_nueva=[]

print("--------Bienvenido--------")
print("Cargue las dos listas numericas")



for x in range (0, 5): 
     print("Lista_1")
     num =int(input( "Ingrese un numero:" )) 
     lista_1.append(num)

op = int(input("Si desea seguir cargando la lista ingrese 1 caso contrario aprete cualquier numero ")) 
while op == 1:
     print("Lista_1")
     num = int(input( "Ingrese un numero: " )) 
     lista_1.append(num)
     op = int(input("Si desea seguir cargando la lista ingrese 1 caso contrario aprete cualquier numero ")) 





for y in range (0, 2): 
   print("Lista_2")
   num = int(input( "Ingrese un numero: " )) 
   lista_2.append(num)

op = int(input("Si desea seguir cargando la lista ingrese 1 caso contrario aprete cualquier numero ")) 
while op == 1:
     print("Lista_2")
     num = int(input( "Ingrese un numero:" )) 
     lista_2.append(num)
     op = int(input("Si desea seguir cargando la lista ingrese 1 caso contrario aprete cualquier numero "))

lista_nueva = eliminar_lista(lista_1,lista_2)
print("Lista_nueva:",lista_nueva)
