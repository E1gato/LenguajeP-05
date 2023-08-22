""""Crea un juego en el que el jugador debe adivinar una palabra oculta antes de que se
agoten los intentos, le deben indicar el tamaño de la palabra y cuantas letras son
correctas."""

import random

def elegir_palabra():
    palabras = ["gato", "perro", "lápiz", "jirafa", "manzana", "elefante", "python", "playa", "computadora"]
    return random.choice(palabras)

def mostrar_palabra(palabra, letras_adivinadas):
    display = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            display += letra
        else:
            display += "_"
    return display

def main():
    palabra = elegir_palabra()
    longitud_palabra = len(palabra)
    intentos_maximos = 6
    letras_adivinadas = []
    intentos = 0

    print("¡Bienvenido al juego de adivinar la palabra!")
    print("La palabra tiene", longitud_palabra, "letras.")

    while intentos < intentos_maximos:
        palabra_mostrada = mostrar_palabra(palabra, letras_adivinadas)
        print("\nPalabra actual:", palabra_mostrada)
        intento = input("Ingresa una letra: ").lower()

        if len(intento) != 1 or not intento.isalpha():
            print("Por favor, ingresa una sola letra.")
            continue

        if intento in letras_adivinadas:
            print("Ya has intentado con esta letra.")
            continue

        letras_adivinadas.append(intento)

        if intento in palabra:
            print("¡Correcto! La letra está en la palabra.")
        else:
            print("Incorrecto. La letra no está en la palabra.")
            intentos += 1

        if palabra_mostrada == palabra:
            print("\n¡Felicidades! Has adivinado la palabra:", palabra)
            break

    if palabra_mostrada != palabra:
        print("\nLo siento, has agotado tus intentos. La palabra era:", palabra)

if __name__ == "__main__":
    main()