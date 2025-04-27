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

# num1 = input("\n Ingresa número 1:\n")
# num2 = input("\n Ingresa número 2:\n")
# print("/: División")
# print("*: Multiplicación")
# print("+: Suma")
# print("-: Resta")
# operacion = input("\n Ingresa operador matematico \n")

# format_num1 = int(num1)
# format_num2 = int(num2)

# if int(format_num1) == 0 or int(format_num2) == 0 and operacion == "/":
#     print("No se puede dividir por 0")
# elif operacion == "/":
#     print(f"El resultado de la división es: {format_num1 / format_num2}")
# elif operacion == "*":
#     print(f"El resultado de la multiplicación es: {format_num1 * format_num2}")
# elif operacion == "+":
#     print(f"El resultado de la suma es: {format_num1 + format_num2}")
# elif operacion == "-":
#     print(f"El resultado de la resta es: {format_num1 - format_num2}")

    

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

# print("Validación de edades")
# age = input("Ingresa la edad:\n")

# format_age = int(age)

# if format_age >= 0 and format_age <= 2:
#     print("Tú eres un bebe")
# elif format_age >= 3 and format_age <= 12:
#     print("Tú eres un niño")
# elif format_age >= 13 and format_age <= 17:
#     print("Tú eres un adolecente")
# elif format_age >= 18 and format_age <= 64:
#     print("Tú eres un adulto")
# elif format_age >= 65:
#     print("Tú eres un adulto mayor")


###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

mensaje_secreto = mensaje[7:]
print(mensaje_secreto)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

hamburguesa = pan + ingredientes + pan_abajo
print(hamburguesa)


# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista = [1, 2, 3]
new_lista = lista + lista
print(new_lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])


# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

lista = [100, 250, 380, 454, 578, 654, 987, 621, 357]
mitad = len(lista) // 2
revertir = lista[:mitad][::-1] + lista[mitad:]
print(revertir)

