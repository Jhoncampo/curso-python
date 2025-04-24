# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
import os
os.system("cls")

# num1 = input("\n Ingresa número 1:\n")
# num2 = input("\n Ingresa número 2:\n")
# if num1 > num2:
#     print(f"El número {num1} es que {num2}")
# elif num2 > num1:
#     print(f"El número {num2} es que {num1}")
# elif num1 == num2:
#     print("Ambos números son iguales")
    

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num1 = input("\n Ingresa número 1:\n")
num2 = input("\n Ingresa número 2:\n")
print("/: División")
print("*: Multiplicación")
print("+: Suma")
print("-: Resta")
operacion = input("\n Ingresa operador matematico")


if int(num1) == 0 or int(num2) == 0 and operacion == "/":
    print("No se puede dividir por 0")
    

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)