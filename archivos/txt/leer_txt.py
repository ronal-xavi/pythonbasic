
#archivo_sin_leer = open("archivos\\txt\\leer.txt", encoding="UTF-8")

#Leer todo el archivo
#archivo = archivo_sin_leer.read()

#leer linea por linea todas
#lineas = archivo_sin_leer.readlines()

#lineas = archivo_sin_leer.readline(2)
#archivo_sin_leer.close()


#print(lineas)



# LEER UN ARCHIVO CON WITCH

with open("archivos\\txt\\leer.txt", encoding="UTF-8") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    #mostraamos el contenido
    print(contenido)



