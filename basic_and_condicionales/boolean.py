#ESTRUCTURA DE INSTRUCIONES -> IF   

a = 97
b = 55

# -> if
if a < b:
    print(b)
if a > b:
    print (a)

# -> else
if a < b:
    print(b)
else:
    print (a)

# -> elif
if a < b:
    print(b)
elif a > b:
    print (a)
else:
    print("no soportado")

#Uso de la logica condicional anidada
a = 32
b = 31
c = 27
if a > b:
    if b > c:
        print ("C es el número menor")
    else: 
        print ("B es el número menor")
elif a == b:
    print ("a es igual a b")
else:
    print ("a es menor a b")

#Uso de Operadores and -> or
if a == 32 and b == 55:
    print("Los 2 tienen que ser verdadero")

if a == 32 or b == 55:
    print("Uno tiene que ser verdadero")
