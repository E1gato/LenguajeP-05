"""Diseñe algoritmo donde un usuario ingrese un Nombre y un Apellido y el programa
indique cuantas vocales contiene su nombre y apellido (Ejemplo, si ingreso Rodrigo Soto
mostrar 3 vocales en el apellido y 2 vocales en el nombre)"""

def contar_vocales(cadena):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    for caracter in cadena:
        if caracter.lower() in vocales:
            contador += 1
    
    return contador

nombre = input("Ingrese su Nombre: ")
apellido = input("Ingrese su Apellido: ")

vocales_nombre = contar_vocales(nombre)
vocales_apellido = contar_vocales(apellido)

print(f"El nombre '{nombre}' tiene {vocales_nombre} vocales.")
print(f"El apellido '{apellido}' tiene {vocales_apellido} vocales.")
