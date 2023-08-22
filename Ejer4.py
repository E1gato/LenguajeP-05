"""Crear un algoritmo que al ingresar un número del 1 al 7, muestre un día de la semana
hasta que se ingrese un numero diferente y terminaría el algoritmo (Ejemplo, si ingreso
2 debe mostrar MARTES)"""

numero_elegido = int(input("Ingresa tu Numero: "))

if numero_elegido == 1:
    print("Lunes")
    
elif numero_elegido == 2:
    print("Martes")
    
elif numero_elegido == 3:
    print("Miercoles")
    
elif numero_elegido == 4:
    print("Jueves")
    
elif numero_elegido == 5:
    print("Viernes")
    
elif numero_elegido == 6:
    print("Sabado")
    
elif numero_elegido == 7:
    print("Domingo")
    
else:
    print("El numero ingresado no es valido")
    