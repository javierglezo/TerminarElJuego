"""
Módulo que agrupa las funciones que describen la lógica del juego
"""


import random

def adivina_el_numero(dificultad):
    """
    Función para jugar una persona manualmente
    """
    if dificultad == 1:
        numero_secreto = random.randint(0, 100)
        min_valor, max_valor = 0, 100
    elif dificultad == 2:
        numero_secreto = random.randint(0, 1000)
        min_valor, max_valor = 0, 1000
    elif dificultad == 3:
        numero_secreto = random.randint(0, 1000000)
        min_valor, max_valor = 0, 1000000
    elif dificultad == 4:
        numero_secreto = random.randint(0, 1000000000000)
        min_valor, max_valor = 0, 1000000000000
    else:
        print("Opción de dificultad no válida")
        return

    intentos = 0
    maxintentos = int(input("Elige el maximo numero de intentos:"))
    ayuda = input("¿Quieres recibir ayuda? (si/no): ").lower()
    while True:
        if ayuda == "si":
            print(f"Número mínimo: {min_valor}, Número máximo: {max_valor}")

        intento = int(input("Adivina el número: "))
        intentos += 1
        if intentos == maxintentos:
            print("Has superado el numero de intentos maximo")
            break

        if intento == numero_secreto:
            print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
            nombre=input("Ingrese su nombre para la tabla de mejores puntuaciones:")
            guardar_puntuacion(nombre,intentos,dificultad)
            break
        elif intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
            min_valor = max(min_valor, intento) + 1
        else:
            print("Demasiado alto. Intenta de nuevo.")
            max_valor = min(max_valor, intento) - 1

def guardar_puntuacion(nombre, intentos, dificultad):
    """
    Función que guarda en un fichero txt los mejores resultados
    """
    with open("mejores_puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre}: Dificultad {dificultad}, Intentos {intentos}\n")

def mostrar_mejores_puntuaciones():
    """
    Función para mostrar el archivo de mejores resultados
    """
    try:
        with open("mejores_puntuaciones.txt", "r") as archivo:
            print("\nMejores Puntuaciones:")
            print(archivo.read())
    except FileNotFoundError:
        print("Aún no hay mejores puntuaciones.")

def IA_adivinar():
    """
    Función para que juegue la IA 
    """
    menuIA()
    dificultad = int(input("Tu elección: "))
    if dificultad == 1:
        numero_secreto = random.randint(0, 100)
        min_valor, max_valor = 0, 100
    elif dificultad == 2:
        numero_secreto = random.randint(0, 1000)
        min_valor, max_valor = 0, 1000
    elif dificultad == 3:
        numero_secreto = random.randint(0, 1000000)
        min_valor, max_valor = 0, 1000000
    elif dificultad == 4:
        numero_secreto = random.randint(0, 1000000000000)
        min_valor, max_valor = 0, 1000000000000
    else:
        print("Opción de dificultad no válida")
        return

    intentos = 0
    #maxintentos = int(input("Elige el maximo numero de intentos:"))
    #ayuda = input("¿Quieres recibir ayuda? (si/no): ").lower()
    while True:
        #if ayuda == "si":
            #print(f"Número mínimo: {min_valor}, Número máximo: {max_valor}")

        intento = int(random.randint(min_valor,max_valor))
        intentos += 1
 #       if intentos == maxintentos:
  #          print("Has superado el numero de intentos maximo")
   #         break

        if intento == numero_secreto:
            print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
            #nombre=input("Ingrese su nombre para la tabla de mejores puntuaciones:")
            #guardar_puntuacion(nombre,intentos,dificultad)
            break
        elif intento < numero_secreto:
            print(f"IA escoge: {intento} - Demasiado bajo. Intenta de nuevo.")

            min_valor = max(min_valor, intento) + 1
        else:
            print(f"IA escoge: {intento} - Demasiado alto. Intenta de nuevo.")
            max_valor = min(max_valor, intento) - 1


def menu():
    """
    Función que muestra el menú predeterminado
    """
    print("\nSelecciona la dificultad:")
    print("1. Nivel simple (entre 0 y 100)")
    print("2. Nivel intermedio (entre 0 y 1.000)")
    print("3. Nivel avanzado (entre 0 y 1.000.000)")
    print("4. Nivel experto (entre 0 y 1.000.000.000.000)")
    print("5. Mostrar Mejores Puntuaciones")
    print("6. IA")
    print("7. Salir")

def menuIA():
    """
    Función que muestra el menú de opciones para la IA
    """
    print("\nSelecciona la dificultad:")
    print("1. Nivel simple (entre 0 y 100)")
    print("2. Nivel intermedio (entre 0 y 1.000)")
    print("3. Nivel avanzado (entre 0 y 1.000.000)")
    print("4. Nivel experto (entre 0 y 1.000.000.000.000)")
    print("7. Salir")



def jugar():
    """
    Función llamada desde el launcher para iniciar el juego
    """
    print("Bienvenido al juego de adivinar el número")
    
    while True:
        menu()
        opcion = int(input("Tu elección: "))

        if opcion == 7:
            print("Gracias por jugar. ¡Hasta luego!")
            break
        elif opcion == 5:
            mostrar_mejores_puntuaciones()
        elif opcion == 6:
            IA_adivinar()
        else:
            adivina_el_numero(opcion)



        