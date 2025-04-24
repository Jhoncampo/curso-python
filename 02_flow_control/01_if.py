# sentencias condicionales if else elif
import os
os.system("cls")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 20:
    print("Tienes 20")
else:
    print("Eres menor de edad")

tiene_carnet = True

if edad>= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("Policia...")

fin_de_semana = True

if not fin_de_semana:
    print("Toca trabajar")

if edad >= 18:
    if fin_de_semana:
        print("Trabajar")
    else:
        print("Quédate en casa")
else:
    print("No trabajar")

