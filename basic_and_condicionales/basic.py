#Importando la fecha
from datetime import date
#Importando sys para poder usar argumenos 
import sys

#Imprimiendo mi primer hola mundo en python
print("hello, world")

#Suma
sum = 1 +1 
print (sum)

#Imprimiendo la fecha de hoy con una importación de fecha
print(date.today())

#Proceso de parseo con -> str
parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

#Argumentos de la linea de comandos
# -> Al nosotros pasarle argumentos al momento de ejecutar un archivo .py podemos pasarle argumentos los cuales podemos usar el la 
#    aplicación. Asi podemos pasarle datos al programa
print (sys.argv) #imprime el array completo
print (sys.argv[0]) #nombre del programa
print (sys.argv[1]) #primer parámetro

#Otra forma de obtener datos del usuario -> input
print("Bienvenido al Sistema")
name = input("Ingresa tu nombre: ")
print ("Bienvenido: " + name)

#NOTA: La función input devuelve cadenas si nosotors queremos sumar números tenemos que convertirlo a enteros -> (int)
#      de esta forma ya podemos sumar 2 números.
