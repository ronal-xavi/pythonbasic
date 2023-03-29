# Def -> para crear una función
from datetime import timedelta, datetime


def hola_mundo():
    print("hola mundo")


# La función holamundo, no devuelve nada, pero si ejecuta un comando es como un void en java.
salida = hola_mundo()
print(salida is None)  # True

# Funcion que de acuerdo al parámetro enviado realiza una acción


def saludo(saludo):
    if saludo == "saludo":
        return "Hola Mundo"
    elif saludo == "despedida":
        return "adios mundo"
    else:
        return "error no se comprende"


print(saludo("despedida"))  # Se imprime la respuesta de la función en consola.

# Funciones como argumentos
print("#####  Funciones con varios Argumentos  #####")
saludo1 = saludo("saludo")  # Función asignada a una variable
print(saludo1)

# Uso de argumentos de palabras clave en Python
print(" ##### Usode argumentos de plabras clave en Python #####")


def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours) # timedalta permite hacer una suma de 2 horas
    return arrival.strftime("Arrival: %A %H:%M")


print(arrival_time())

print("HORA ACTUAL DEL SISTEMA")
hora_actual_del_sistema = datetime.now()
print(hora_actual_del_sistema)

print(hora_actual_del_sistema.strftime('%A %H:%M:%S'))



