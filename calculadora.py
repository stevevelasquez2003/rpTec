
import math


seleccion = int(input(""" Calculadora: por favor ingrese una opcion 4 \n
       \t1.Sumas\n
       \t2.Resta\n
       \t3.Multiplicacion\n
       \t4.Division\n
       \t5.Potenciacion\n
       \t6.factorial\n
       \t7.raiz\n
    \t8.Salir\n
        """))


while seleccion:
     
     

     if seleccion == 1 :
        
        num1 = int(input("Por favor ingrese el primer numero"))
        num2 = int(input("Por favor ingrese el segundo numero"))
        sumar = num1 + num2
        print(sumar)
        break
     elif seleccion == 2 :
         num1 = int(input("Por favor ingrese el primer numero"))
         num2 = int(input("Por favor ingrese el segundo numero"))
         resta = num1 - num2
         print(resta)
         break
     elif seleccion == 3  :
         
         num1 = int(input("Por favor ingrese el primer numero,"))
         num2 = int(input("Por favor ingrese el segundo numero"))
         multiplicacion = num1 * num2
         print(multiplicacion)
         break
            
           
     elif seleccion == 4 :
         num1 = int(input("Por favor ingrese el primer numero,"))
         num2 = int(input("Por favor ingrese el segundo numero"))
         
         
         if num1 and num2 == 0:
          print("recuerde no poner 0 en la division")
          
         else:
             division = num1 / num2
             print(division)
             break
     
     elif seleccion == 5:
         num1 = int(input("Por favor ingrese el primer numero,"))
         num2 = int(input("Por favor ingrese el segundo numero"))
         potencia = pow(num1, num2)   
         print(potencia)
         break

     elif seleccion == 6:
         num1 = int(input("Por favor ingrese un numero para sacar el factorial,"))
         facto = math.factorial(num1)
         print(facto)
         break
     elif seleccion == 7:
         num1 = int(input("Por favor ingrese un numero positivo,"))
         if num1 <= 0:
            print("El numero no es positivo")
            
         else:
            siete = math.sqrt(num1)
            print(siete)
            break
     elif seleccion > 8 and seleccion < 0 :
         print("El numero seleccionado es incorrecto")
         break
     elif seleccion == 8:
         print("Ha salido de calculadora")
         break
         

         

         
    
    
         

        