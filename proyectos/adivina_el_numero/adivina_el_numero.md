# Adivina el número

Este proyecto es un juego realizado en Python. El juego consiste en adividar el número aleatorio que dará la computadora. Nosotros pasaremos un parametro para definir el rango del número dado por la computadora.

Para el desarrollo de este proyecto se uso la libreria `randon` de python.

El código es el siguiente.

```python
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

```
