###################################################################
#=========== PRIMERA FORMA DE RESOLVER LA ACTIVIDAD ==============
###################################################################

import pandas as pd

#Leer el archivo CSV con datos de notas
archivo = pd.read_csv("datos_csv.csv")

#Agregar la columna promedio
archivo["PROMEDIO"] = (archivo["NOTA1"] + archivo["NOTA2"] + archivo["NOTA3"]) / 3
#Agregamos columas de aprobado y reprobado
archivo.loc[archivo["PROMEDIO"]>10,"RESULTADO"] = "APROBADO"
archivo.loc[archivo["PROMEDIO"]<=10,"RESULTADO"] = "REPROBADO"


#Inprimir
print(archivo)

#Separando aprobados de reprobados
aprobados = archivo[archivo["PROMEDIO"]>10]
reprobados = archivo[archivo["PROMEDIO"]<=10]

#Inprimir
print(aprobados)
print(reprobados)

#Guardando en archivos separados
aprobados.to_csv("aprobados.csv")
reprobados.to_csv("reprobados.csv")



###################################################################
#=========== SEGUNDA FORMA DE RESOLVER LA ACTIVIDAD ==============
#CON UN BUCLE EN BASE A LA COLUMNA RESULTADO
###################################################################

salida = archivo.RESULTADO.unique()
print(salida)

for i in archivo.RESULTADO.unique():
    archivo2 = archivo[archivo["RESULTADO"]==i]
    print(archivo2)
    archivo2.to_csv(f"{i}.csv")