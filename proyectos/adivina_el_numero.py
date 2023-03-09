import random


def adivina_el_numero(x):
    print("======================")
    print(" BIENVENIDO AL JUEGO  ")
    print("======================")
    print("Tu meta es adivinar el número aleatorio por la computadora.")

    numero_aleatorio = random.randint(1, x)
    prediccion = 0
    while prediccion != numero_aleatorio:
        # El usuario ingresa un número
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("Intenta otra vez este número es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez este número es muy grande.")
    print(f"Felicitaciones adivinaste el número correctamente")


adivina_el_numero(10)
