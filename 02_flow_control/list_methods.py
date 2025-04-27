import os
os.system("cls")


# añadir o insertar elementos a una lista
lista = [1,2,3,4,5]
lista.append(6) # Agrega un elemento al final de la lista
print(lista) # [1, 2, 3, 4, 5, 6]

lista.insert(0, 2) # Agrega un elemento en la posicion 0 de la lista
print(lista) # [2, 1, 2, 3, 4, 5, 6]

lista.extend([7,8,9]) # Agrega una lista al final de la lista
print(lista) # [2, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# eliminar elementos de una lista
lista.remove(2) # Elimina el primer elemento que coincide con el valor 2
print(lista) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

ultimo = lista.pop() # Elimina el ultimo elemento de la lista
print(ultimo) # 9
print(lista) # [1, 2, 3, 4, 5, 6, 7, 8]

lista.pop(1) # Elimina el elemento en la posicion 1 de la lista
print(lista) # [1, 3, 4, 5, 6, 7, 8]

# otra que se puede usar para eliminar
del lista[-1] # elimina el ultimo elemento de la lista
print(lista) # [1, 3, 4, 5, 6, 7]

lista.clear() # Elimina todos los elementos de la lista
print(lista) # []

# eliminar un rango de elementos de una lista
lista = ["a", "b", "c", "d", "e", "f", "g"]
del lista[1:4] # Elimina los elementos de la posicion 1 a la 4 (sin incluir la 4)
print(lista) # ['a', 'f', 'g']

# Ordenar una lista modificando la original
lista = [5, 2, 3, 1, 4] # Lista desordenada
print(lista) # [5, 2, 3, 1, 4]
lista.sort() # Ordena la lista de menor a mayor
print(lista) # [1, 2, 3, 4, 5]

# Ordernar la lista creando una nueva lista
lista = [5, 2, 3, 1, 4] # Lista desordenada
print(lista) # [5, 2, 3, 1, 4]
copia_lista = sorted(lista) # Ordena la lista de menor a mayor y crea una nueva lista
print(copia_lista) # [1, 2, 3, 4, 5]

# Ordernar lista de cadenas de texto todas en minusculas
frutas = ["manzana", "pera", "banana", "kiwi"]
sorted_frutas = sorted(frutas) # Ordena la lista de menor a mayor y crea una nueva lista
print(sorted_frutas) # ['banana', 'kiwi', 'manzana', 'pera']

# Ordernar lista de cadenas de texto que tienen mayusculas y minusculas
frutas = ["Manzana", "pera", "banana", "kiwi"]
sorted_frutas = sorted(frutas) # Ordena la lista de menor a mayor y crea una nueva lista    
print(sorted_frutas) # ['Manzana', 'banana', 'kiwi', 'pera']
frutas.sort(key=str.lower) # con el lower se ordena sin importar si es mayuscula o minuscula
print(frutas) # ['banana', 'kiwi', 'Manzana', 'pera']

# Más metodos o cosas utilies de listas
animales = ["perro", "gato", "loro", "pez", "gato"]
print(len(animales)) # 5
print(animales.count("gato")) # 2
print("gato" in animales) # comprueba si existe el elemento en la lista # True
