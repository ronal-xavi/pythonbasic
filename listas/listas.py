# Listas
planets = ["Mercury", "Venus", "Earth", "Mars","Jupiter", "Saturn", "Uranus", "Neptune"]

# Acceso a elementos de listas por el indice
print(planets[1])
print(planets[2])
print(planets[5])

# Modificando elementos de una lista
planets[1] = "Modificado"
print(planets[1])

# Len
# Tamaño de una lista -> El tamaño empieza desde el número 1
tamano_de_ista = len(planets)
print(tamano_de_ista)

# Append -> para agregar elementos a una lista
planets.append("ronal")
print(planets)

#Pop -> Eliminar elementos de una lista
planets.pop()
print(planets)

##################################################################
# NOTA: Los indices comienzan en 0 y van en aumento, los indices #
# negativos empiezan al final y van hacia atras.                 #
##################################################################

#Index -> busca un valor en una lista
jupiter_index = planets.index("Jupiter")
print(jupiter_index)

# Números en listas
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

# Min
valor_menor = min(gravity_on_planets)
print(valor_menor)

# Max
valor_mayor = max(gravity_on_planets)
print(valor_mayor)

# Segmentación de listas
segmentacion = planets[0:2]
print(segmentacion)

# Unir listas con " + "
lista_cualquiera = ["valor", "valor", "valor"]
print(planets + lista_cualquiera)

# Sort -> para ordenas listas de forma alfabeticamente en cadenas y en orden número en números
# Para listar en inverso es .sort(reverse=True)

lista_para_ordenar = ["a","e","u","i","o"]
lista_ordenada = lista_para_ordenar.sort()

print(lista_ordenada)
