#Desarrollar un programa que simule una calculadora básica, permitiendo al usuario realizar sumas, restas, multiplicaciones y divisiones.
print("----Desarrollar un programa que simule una calculadora básica, permitiendo al usuario realizar sumas, restas, multiplicaciones y divisiones.----")

entrada = input("Ingresa una operación (por ejemplo 2 + 3): ")

num1_str, operador, num2_str = entrada.split()

num1 = float(num1_str)
num2 = float(num2_str)

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Error: división por cero.")
        exit()
else:
    print("Operador no válido.")
    exit()

print(f"Resultado: {resultado}")

# Crear un juego de adivinanza donde el programa genere un número aleatorio y el usuario deba adivinarlo, recibiendo pistas de "mayor" o "menor" en cada intento
print("----Crear un juego de adivinanza donde el programa genere un número aleatorio y el usuario deba adivinarlo, recibiendo pistas de 'mayor' o 'menor' en cada intento----")

import random

numero_secreto = random.randint(1, 100)
print("¡Bienvenido al juego de adivinanza!")
print("Estoy pensando en un número entre 1 y 100.")

while True:
    try:
        intento = int(input("Ingresa tu intento: "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        continue

    if intento < numero_secreto:
        print("Demasiado bajo. ¡Intenta un número mayor!")
    elif intento > numero_secreto:
        print("Demasiado alto. ¡Intenta un número menor!")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")
        break



