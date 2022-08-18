#Para pagar impuestos el usuario debe:
#Cobrar más de 20000 pesos Y tener más de 18 años
#O
#Tener más de 30 años
#Datos que debe ingresar el usuario:
#sueldo = IN;
#edad = INT;

sueldo= int(input("Ingrese su sueldo: "))
edad= int(input("Ingrese su edad: "))

if (sueldo > 20000 and edad > 18) or edad > 30:
    print("Usted puede pagar impuestos ")
else: 
    print("Usted no puede pagar impuestos ")