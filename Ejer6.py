"""Crea un juego en el que generes un número aleatorio y el usuario debe adivinarlo, debe
brindarles pistas al usuario sobre cuál podría ser el numero como indicar si es un
número mayor o menor y no terminar hasta que el usuario adivine el numero"""

import random

numero_aleatorio = random.randint(1, 100)
intentos = 0

print(numero_aleatorio)
print("Adivina el número")
print("El numero es entre 1 y 100")
    
while True:
    intentos += 1
    numero_elegido = int(input("Ingresa tu Numero: "))
        
    if numero_elegido == numero_aleatorio:
        print(f"Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
        break
    elif numero_elegido < numero_aleatorio:
        print("El número es mayor.")
    else:
        print("El número es menor.")