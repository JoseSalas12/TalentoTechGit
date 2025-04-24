# Crear un script que pida al usuario un número y determine si es par o impar utilizando condicionales (if, else).
print("----Crear un script que pida al usuario un número y determine si es par o impar utilizando condicionales (if, else).----")
Numero = int(input("Ingrese un número: "))
if Numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

#Implementar un bucle for para iterar sobre una lista de números e imprimir sus cuadrados.
print("----Implementar un bucle for para iterar sobre una lista de números e imprimir sus cuadrados.----")
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}.")

# Usar un bucle while para solicitar repetidamente la entrada del usuario hasta que se cumpla una condición específica
print("----Usar un bucle while para solicitar repetidamente la entrada del usuario hasta que se cumpla una condición específica----")
salida = 12
numero = 0
while(numero != salida):
    numero = int(input("Ingrese un número: "))
    print(f"Número ingresado: {numero}")



