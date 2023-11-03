# for iteraa o ejecuta la instruccion hasta llegar al  limite  de un rango 

texto = "bienvenido"

for letra in texto: 
    print(letra)

#conar la cantidad de letras e 
cantidadE= 0
for indice in range(len(texto)):
    if texto[indice] == "e":
        cantidadE += 1

    print("La palabra cantidad tiene ", cantidadE, "letras e")
