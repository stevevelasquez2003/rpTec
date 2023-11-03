#COLECCIONES:
"""
Variable que almacena multiples elementos
"""

fruta1 = "Manzana"
fruta2 = "Pera"
fruta3 = "Fresa"

Frutas = ["Manzana", "Pera", "Fresa"]

#listas, tuplas, diccionarios.
#LISTAS
"""
LISTAS = []
Son mutables: pueden  modificarse.
Son indexadas: posicion de cada elemento de la lista, los indices van de 0 en adelante.
Pueden contener cualquier tipo de datos.
METODOS:
insertar:
append(), insert(indice, elemento).
eliminar:
pop(), remove()
organizar:
sort(), sort(reverse=True)
posicion:
index()
count(): contar elementos.
len(): longitud o cantidad de elementos que contiene la lista.
"""
Submodulos = ["Bases de datos", "Nuevas Tecnologias", "Web II", "Metodologias Agiles", "Logica de programación", "Web I", "Moviles"]
#longitud de la lista submodulos
print("La lista contiene",len(Submodulos), "elementos")
#Acceder a un elemento de la lista. se accede teniendo en cuenta la posicion.
print(Submodulos[-1])
#Modificar un submodulo
Submodulos[5] = "Catedra de emprendimiento"
print(Submodulos)
#Insertar elementos:
#Append(elemento): inserta en la ultima posicion de la lista
Submodulos.append("web I")
print(Submodulos)
#insert(posicion, elemento):
Submodulos.insert(4, "Introducción a la programacion")
print(Submodulos)
print(len(Submodulos))
#recorrer lista submodulos:
for elemento in Submodulos:
    print(elemento)
#Recorrer teniendo en cuenta el indice:
for indice in range(len(Submodulos)):
    print(Submodulos[indice], "Esta en la posisicion", indice)

#Eliminar elementos por su posicion o indice : pop(),remove(),clear()
# Submodulos.pop(Submodulos)
# print(Submodulos)

# Submodulos.remove("web II")
# print(Submodulos)

# Submodulos.clear()
# print(Submodulos)

numeros = [1,2,3,4,5,6,7,8,9,-10,11,-12,13,-14,15]

ng =[]
for  i in range(len(numeros)):
  if numeros[i]< 0 or numeros [i] %2 != 0 :
    ng.append(numeros[1])
    print(ng)
        
#index(): para conocer la posicion de un elemento
numeros = [1,2,3,4,5,6,7,8,9,-10,11,-12,13,-14,15]
#cono cer la posicion del numero 2
print(numeros.index(2))
#count() cuenta las repiticiones de un elemento
print("el numero 6 esta repetido :" ,numeros.count(6),"veces")

deportes= ["futbol","tenis de mesa","baloncesto","voleibol","tenis"]
#ordenar la lista de forma ascendente : short()

deportes.sort()
print(deportes)
#ordenar de forma decentente

deportes.sort(reverse=True)
print(deportes)

#recorrer dos o mas listas al tiempo: zip

animales =["perro","pajaro","tiburon"]
tipo_animales =["terrestres","voladores","acuaticos"]
for A, T in zip(animales,tipo_animales):
   print(f"El {A} es un animal {T}")