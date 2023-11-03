#son arreglos que no se pueden modificar
"""
tuplas = ()
tambien se puede representar con los elementos separados por comas
tuplas = elemento1 , elemento2 , elemento3, .....
auque tenga solo un elelmento tiene que acabar con coma
tuplas = elemento,


"""

# tupla = 3,
# print(type(tupla))
# dias_semana = "lunes","martes","miercoles","jueves","viernes"
# print(type(dias_semana))

# #como acceder a una tupla
# meses = ("enero","marzo","abril","mayo","junio","julio","agosto","octubre","noviembre","diciembre")
# #si quiero saber la posicion de algo ago lo siquiente utilizo el index():
# posicion = meses.index("octubre")
# print(posicion)
# #longirtud de la tupla

# print(len(meses))

# numeros = (1,2,3,4,5,6,6,6,9,10,1,1,2)

# #repeticiones tiene el 6
# contar = numeros.count(6)
# print(contar)

# #concatenar tuplas :

# pares:(2,4,6,8,10)
# impares:(1,3,5,7,9) #+ pares
# #print(impares)

# # concatenar_tuplas = pares + impares

# # print(concatenar_tuplas)
# # list_comb = list(impares)+list(pares)
# # list_comb.sort()

# conca = list(pares + impares)#pasar una tupla a lista 
# conca.sort()
# tupla_o=tupla(conca)# pasar una lista a tupla
# print(tupla_o)

#DICCIONARIOS
"""
Diccionarios = {}
son dinamicos porque pueden crecer y decrecer , en los diccionarios se trabaja en funccion a la clave y esta tiene que ser unica

diccionario ={clave: valor}
"""
datosPersonales = {"Nombre":"Steven",
                   "Apellidos":"Arango",
                   "edad":38,
                   "sexo":"Masculino"}
print(type(datosPersonales))

#otra forma de crear diccionarios
DatosP = dict(Nombre = "Nayrobi",
              Apellidor = "Jimenez",
              edad = 45,
              sexo = "femenino")
print(type(DatosP))

#Acceder a un elemento
print(datosPersonales["edad"])
#Aceder con el metodo get()
print(datosPersonales.get("Nombre"))

#Modificar un elemento del diccionario
datosPersonales["Apellidos"] = "valencia"
print(datosPersonales)
#modificar un datodo
datosPersonales["mes"] = "marzo"
print(datosPersonales)
#acceder solo a las claves
for clave in datosPersonales :
    print(clave)

#acceder a los valores sin el metodo values

for valor in datosPersonales:
    print(datosPersonales[valor])

#obtener clave y valor con el metodo item()

for i,x in datosPersonales.items():
    print(f"{i} = {x}")
    print(datosPersonales)

    #pop()el argumento del pop es la clave,popitem():elimina el ultimo elemento del diccionario,clear():eliinar todos los elementos del diccionario

    print(datosPersonales.pop("steven"))

    #claves : keys()

    for v in datosPersonales.keys():
        print(v)

    #valores : values()
    for m in datosPersonales.values():
        print(m)