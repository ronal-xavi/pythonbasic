# Cadenas en Python
# INMUTABLES
# -> Las cadenas en python son inmutables, el valor de una cadena en python no canbia.
fact = "The Moon has no atmosphere."
fact + "No sound can be heard on the Moon."
print(fact)

# -> Para poder obtener el nuevo valor de la cadena tenenos que asignarla a otra variable.
two_fact = fact + "No sound can be heard on the Moon."
print(two_fact)

# => Las operaciones con cadenas siempre "devuelven cadenas neuvas".

# COMILLAS -> simples - dobles - triples
# -> Comillas dobles
moon_radius = "The Moon has a radius of 1,080 miles"
print(moon_radius)

# -> Comillas dobles dentro de comillas simples
text = 'The "near side" is the part of the Moon that faces the Earth'
print(text)

# -> Una comilla simple dentro de comillas dobles
text2 = "We only see about 60% of the Moon's surface"
print(text2)

# -> Comillas dobles dentro de comillas simples y dobles dentro de comillas triples
text3 = """We only see about 60% of the Moon's surface, this is known as the "near side"."""
print(text3)

# MULTILINEAS
# -> \n
textoMultilinea1 = "Hola este es un texto multilinea \n este es el salto de linea"
print(textoMultilinea1)

# -> """
textoMultilinea2 = """ Hola este es el segundo texto multilinea
este es el salto de linea"""
print(textoMultilinea2)

# =================================================================================================================================

# TITLE
# Escribe la primera letra de cada palabra en mayúsculas
titulo = "Este es un titulo desde python"
print(titulo.title())

# SPLIT
# Separa la cadena en un array cuando encuentre un espacio
textSplit = "Este es un texto ejemplo"
print(textSplit.split())

# IN
# Busqueda de cadenas
"perro" in "El perro se fue de su casa"  # true
"gato" in "El perro se fue de su casa"  # false

# FIND
# Busca la posicion de una palabra en especifica,
# Si no encuentra la palabra devuelve -1
textFind = "Este es un texto de prueba"
print(textFind.find("es"))

# COUNT
# Devuelve en número de veces que se repite esa palabra en una cadena
textCount = "Este es un texto de prueba prueba"
print(textCount.count("prueba"))

#############################################################
# NOTA: Python diferencia las mayusculas de las minusculas. #
#############################################################

# LOWER
# Para convertir toda la cadena en minusculas
textLower = "Este es un texto"
print(textLower.lower())

# UPPER
# Para convertir toda la cadena a mayusculas
textUpper = "Este es un texto"
print(textUpper.upper())

# EJEMPLOS
# Obtener lo que vengas despues de los " : ".
textoEjemplo = "La temperatura en la luna es de: -60 C"
print(textoEjemplo.split(":"))
arrayEjemplo = textoEjemplo.split(":")
print(arrayEjemplo[-1])

# Recorrer el texto y obtener lo que sea un número
textoEjemplo2 = "La temperatura en marte es de 60 grados"
for item in textoEjemplo2.split():
    if item.isnumeric():  # tambien se puede usar el .isdecimal()
        print(item)
    else:
        print("nada")

# STARTSWITH
# Al inicio de una palabra
numero1 = "-60"
if numero1.startswith("-"):
    print("Es un múmero negativo => " + numero1)

# ENDSWITH
# Al final de una palabra
numero2 = "60 C"
if numero2.endswith("C"):
    print("temina con la => C")

# TRANSFORMAR TEXTOS
# Replace
textoReplace = "Este texto es para reemplazar"
print(textoReplace.replace("texto", "ronal"))

# JOIN
# -> Asi como el split separa el Join une.
# textoJoin = ['Este', 'es', 'un', 'texto', 'ejemplo']
# print(textoJoin.join(textoJoin))

# %
# IMPORTANTE : NO SE PUEDE USAR MÁS DE 9
porcentaje = "1/6"
print("En este texto tiene que ir el porcentaje al final:: %s" % porcentaje)

# Para pasar varios valores es necesario utilizar los parentesis
one = "one"
two = "two"
print("Números en english uno = %s, dos = %s" % (one, two))

# FORMAT
# Usa llaves como marcador de posicionamiento de una cadena
textoFormat = "En este texto {} que eso dice.".format("gil")
print(textoFormat)

# Tambien podemos usar dentro de las llaves números que hacen referncia al parametro del format.
textoFormat2 = "Este es un texto {0}, este es otro texto {1}".format(
    "one", "two")
print(textoFormat2)

# Tambien podemos usar letras dentro de las llaves que hacer referencia al parámetro del formal
textoFormat3 = "Este es un texto {one}, este es otro texto {two}".format(
    one="ONE", two="TWO")
print(textoFormat3)

# F- STRING
# Desde python 3.6 podemos usar nombres de varibles dentro de cadenas String
variableIngresar = "NO PASA NADA XD"
textoFstring = f"Este es un texto veamos que pasa: {variableIngresar}"
print(textoFstring)

nombre = 5
print(nombre + "hola")
