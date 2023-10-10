

import random

numero = random.randint(1, 1000)
adivina = 0
intentos = 0

print("Bienvenido al juego de adivinanza de números. Tienes que adivinar el número secreto entre 1 y 1000")

while adivina != numero:
    adivina = int(input("Ingresa un número: "))
    intentos += 1

    if adivina < numero:
        print("El número es mayor.")
    elif adivina > numero:
        print("El número es menor.")

print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
