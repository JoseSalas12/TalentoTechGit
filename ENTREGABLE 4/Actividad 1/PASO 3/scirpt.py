# Crear una lista de elementos, como nombres de estudiantes, y mostrar cada uno utilizando un bucle.
print("----Crear una lista de elementos, como nombres de estudiantes, y mostrar cada uno utilizando un bucle.----")
nombre_estudiantes = ["Juan", "María", "Pedro", "Ana", "Luis"]
for nombre in nombre_estudiantes:
    print(f"Estudiante: {nombre} ")

contacto = {
    "Nombre" : "Jose",
    "Correo" : "hola@gmail.com"
}

# Crear un diccionario simple que almacene información de contacto (nombre, correo) y mostrar sus claves y valores.
print("----Crear un diccionario simple que almacene información de contacto (nombre, correo) y mostrar sus claves y valores.----")
print(contacto.items())
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")


#Implementar un script que permita al usuario agregar elementos a una lista o actualizar valores en un diccionario
print("----Implementar un script que permita al usuario agregar elementos a una lista o actualizar valores en un diccionario----")
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar elemento a la lista")
    print("2. Crear o actualizar valor en el diccionario")
    print("3. Mostrar lista y diccionario")
    print("4. Salir")

def agregar_a_lista(mi_lista):
    elemento = input("Ingresa el elemento a agregar a la lista: ")
    mi_lista.append(elemento)
    print(f"El numero '{elemento}' ha sido agregado a la lista.")

def actualizar_diccionario(mi_dict):
    clave = input("Ingresa la clave: ")
    valor = input("Ingresa el valor: ")
    accion = "actualizado" if clave in mi_dict else "creado"
    mi_dict[clave] = valor
    print(f"Clave «{clave}» {accion} con el valor «{valor}».")

def mostrar_contenido(mi_lista, mi_dict):
    print("\nContenido de la lista:")
    if mi_lista:
        for i, elem in enumerate(mi_lista, 1):
            print(f"  {i}. {elem}")
    else:
        print("  (vacía)")

    print("\nContenido del diccionario:")
    if mi_dict:
        for clave, valor in mi_dict.items():
            print(f"  {clave!r}: {valor!r}")
    else:
        print("  (vacío)")


mi_lista = []
mi_dict = {}

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1 a 4): ").strip()

    if opcion == "1":
        agregar_a_lista(mi_lista)
    elif opcion == "2":
        actualizar_diccionario(mi_dict)
    elif opcion == "3":
        mostrar_contenido(mi_lista, mi_dict)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, por favor elige entre 1 y 4.")

