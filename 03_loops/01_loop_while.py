# import os
# os.system("cls")

# print("\n Bucle while")
# # El bucle while se ejecuta mientras la condicion sea verdadera

# contador = 0
# while contador <= 5:
#     print("Contador:", contador)
#     contador += 1 # contador = contador + 1 es importarte para que el bucle no sea infinito


# # utilizando el bucle while con el break
# print("\n Bucle while con break")

# contador = 0
# while True:
#     print("Contador:", contador)
#     contador += 1 # contador = contador + 1 es importarte para que el bucle no sea infinito
#     if contador == 5:
#         break # se sale del bucle cuando el contador es mayor o igual a 5

# print("\n bluce con continue")
# # El continue se utiliza para saltar una iteracion del bucle
# contador = 0
# while contador < 10:
#     contador += 1
#     if contador % 2 == 0:
#         continue
#     print("Contador:", contador) # imprime solo los numeros impares

# # else
# print("\n Bucle while con else")
# contador = 0
# while contador < 5:
#     print("Contador:", contador)
#     contador += 1
# else:
#     print("El contador ha llegado a 5")


# # Pedirle al usuario que ingrese un número
# numero = -1
# while  numero < 0:
#     numero = int(input("Ingrese un número positivo: "))
#     if numero < 0:
#         print("El número ingresado no es positivo. Intente nuevamente.")
# print("El número ingresado es:", numero)

numero = -1
while  numero < 0:
    try:
        numero = int(input("Ingrese un número positivo: "))
        if numero < 0:
            print("El número ingresado no es positivo. Intente nuevamente.")
    except:
        print("El valor ingresado no es un número. Intente nuevamente.")
    
print("El número ingresado es:", numero)