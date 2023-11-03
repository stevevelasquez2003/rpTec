#while itera o ejecuta una instruccion hasta que esta sea falsa 

"""
sintaxis 

while condicion ;
 bloque de codigo 
 bloque fuera del ciclo 
"""

# imprimir los numero del 1 al 10
"""
numeros = 1



while numeros <= 10 :

    print(numeros)
    numeros += 1 #numero = numero +1
"""


# sumar los numero pares menores que 20

"""
totalPares = 0
valor = 0

while valor < 20:

    if valor % 2 == 0:
        totalPares += 0 
    valor += 1 
print(totalPares)
"""

#solicitar al usuario confirmar  un pin ya predeterminado , si el pin y la confirmacion son iguales mostrar tiene acceso al dispositivo de lo comtrario acceso denegado
pin = 4548
confirmacion = int(input("Porfavor ingrese el pin"))
contador = 0 
limite = 3

while pin != confirmacion and contador < limite:
    limite -= 1
    print(f"tienes {limite -1} intentos")
    confirmacion = int(input("Porfavor confirme nuevamente el pin"))
    contador += 1 

if pin == confirmacion:
    print("Tienes acceso al dispositivo")
else:
    print("acceso denegado")

    #Solicitar al usuario que escoja DE UN MENU el ares de la figura que sea geometrica ( rectangulo cuadrado triangulo y circulo )

import math

eleccion = int(input("por favor elija una de estas figuras con su numero 1.rectangulo, 2.cuadrado, 3.triangulo y 4.circulo  "))



while eleccion :
  print(""" Calcular: \n
       \t1.area del triangulo\n
       \t2.area ciadrado\n
       \t3.area rectangulo\n
       \t4.area circulo\n
       \t5.area cubo\n
        \t6.salir\n
        """)

    if eleccion == 1:
        lado = int(input("Por favor ingrese el lado del rectangulo"))
        altura = int(input("Por favor ingrese la altura del rectangulo"))
        calculoRec = lado * altura
        print(calculoRec)
    
    elif eleccion == 2:

        ladocuadro = int(input("Por favor ingrese el lado del cuadrado"))
        calculoCuad = ladocuadro * ladocuadro
        print(calculoCuad)
    
    elif eleccion == 3: 
        basetrian = int(input("Por favor ingrese la base del triangulo"))
        alturatrian = int(input("Por favor ingrese la altura del triangunlo"))
        calculoTri = basetrian * alturatrian / 2
        print(calculoTri)
    
    elif eleccion == 4:

        radio = int(input("por favor ingrese el radio del circulo"))
        calculocir = math.pi * radio * radio
        print(calculocir)

# break romper ciclos 
d= 0 
while d < 10 :
     print(d)
     d += 1
     if d == 5:
        break