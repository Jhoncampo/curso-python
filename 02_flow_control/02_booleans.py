import os
os.system("cls")
# Operadores de comparación: devuelve un valor boooleano
print("5 < 3:", 5 < 3) # false
print("5 > 3:", 5 > 3) # true
print("5 == 5:", 5 == 5) # true igualdad
print("5 != 3:", 5 != 3) # false desigualdad
print("5 >= 3:", 5 >= 3) # true
print("5 <= 3:", 5 <= 3) # false


# Comparación de cadenas: 
print("manzana < pera", "manazana" < "pera") # true: es verdadero porque la m está antes que la p
print("Hola == hola", "Hola" == "hola") # false: Aunque son la misma palabra python es sensible a las mayúsculas


print("\n La condición ternaria:")

edad = 17
print("Es mayor de edad" if edad >= 18 else "Es menor de edad")