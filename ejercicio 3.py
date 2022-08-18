"""3)
Una profesora tiene un curso de 8 alumnos. Se deben poder cargar las notas de esos 8
alumnos y contar la cantidad de alumnos aprobados. Al finalizar se debe mostrar el
promedio de todo el curso.
Para conseguir el promedio, calculamos la nota de todos los alumnos divido la cantidad ingresada.
Datos que debe ingresar el usuario:
nota = INT""" 
curso=[]
cont=0
acum=0
alum_aprob=0
promedio=0

while cont  < 8:
     nota = int(input("Ingrese nota: ")) 
     curso.append(nota)
     acum+=nota
     cont+=1
     if nota >=6:
           alum_aprob+=1
    

promedio= acum/8
print("Notas: ", curso)
print("Promedio: ", promedio)
print("Cantidad de alumnos aprobados: ",alum_aprob )
