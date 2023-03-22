# Diccionario de datos para almacenar los planetas y sus lunas -> clave valor como los objetos en Java

planet = {
    'name': 'Earth',
    'moons': 1
}
print(planet)

# Get -> para leer los valores de un diccionario de datos
# La diferencia entre las 2 formas de objetner valores de un diccionario seia que en:
# get cuando la clave no esta disponible retorna un "none"
# los [] devuelven un error una excepcion -> Throws KeyError

print(planet.get('name'))
print(planet['name'])  # -> más utilizado

# Update
# Forma1 -> podemos modificar varios de una solavez
planet.update({'name': 'Ronal'})
planet['name'] = "Mendoza"  # Forma2 -> solo podemos modificar de uno en uno

print(planet)

# Usando update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Usando brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

# Pop -> para eliminar una clave

planet.pop('name')
print(planet)

# Tipos datos complejos Diccionarios anidados

diccionario1 = {
    "name": "ronal",
    "apellido": "mendoza",
    "datos_medicos": {
        "dato1": "dato1"
    }
}

print(diccionario1)

# Recuperación de todas las claves y valores
print("----------------------------")
for key in diccionario1.keys():
    print(key)
    print(diccionario1[key])

# Values -> Devuelve la lista de todos los valores de un diccionario sin sus claves
print("----------------------------")
for key in diccionario1.values():
    print(key)

