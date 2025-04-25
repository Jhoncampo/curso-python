# Listas conjunto de 
import os

os.system("cls")

print("Crear lista")
lista1 = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = ["manzana", "pera", "naranja"] # Lista de cadenas
lista3 = [1, "manzana", 3.14, True] # Lista de diferentes tipos de datos

lista_vacia = [] # Lista vacía
lista_de_listas = [[1, 2], [3, 4], [5, "vaca de prueba"]] # Lista de listas
matrix = [[1,2], [3,4], [5,6]] # Matriz 3x2

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)  
print(lista_de_listas)
print(matrix)

# Acceso a elementos por indice
print("Acceso a elementos por indice")
print(lista2[0]) # manzana
print(lista2[1]) # pera
print(lista2[-1]) # naranja

print(lista_de_listas[2][1])

# slicing (rebanado) listas
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[2:]) # [3, 4, 5]
print(lista1[:]) # [1, 2, 3, 4, 5]


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista1[::2]) # [1, 3, 5, 7, 9] # Cada segundo elemento
print(lista1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # Invertir lista