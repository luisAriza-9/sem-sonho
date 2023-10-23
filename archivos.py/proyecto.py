import json

with open("GANADORES.json","w") as GANADORES:
    ganadores = {}

import random
import os




def iniciarJuego():
    """Función que incializa los valores del juego"""
    juegoenProceso = True
    jugadores = [[input("Jugador 1: "),"X"], [input("Jugador 2: "),"O"]]
    jugador_actual = random.randint(0, 1)
    tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]
    return juegoenProceso, jugadores, jugador_actual, tablero

def actualizar_tablero(jugador, coordenada_fila, coordenada_columna, tablero_actual):
    """Actualiza el tablero con la acción del jugador actual"""
    tablero_actual[coordenada_fila - 1][coordenada_columna - 1] = jugador[1]
    return tablero_actual

def tablero_completo(tablero_actual):
    """Comprueba si el tablero está completo, devuelve True o False"""
    for linea in tablero_actual:
        for celda in linea:
            if celda == '-':
                return False
    return True

def comprobar_ganador(jugador, tablero_actual):
    """Comprueba si ha ganado el jugador actual, devuelve True o False"""
    #Comprobar por filas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[i][x] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador

    #Comprobar por columnas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[x][i] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador

    #Comprobar por diagonales
    ganador = True
    for i in range(3):
        if tablero_actual[i][i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador

    ganador = True
    for i in range(3):
        if tablero_actual[i][3 - 1 - i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador
    
    return False

juegoenProceso, jugadores, jugador_actual, tablero = iniciarJuego()

while juegoenProceso:
    if tablero_completo(tablero):
        juego_en_curso = False
        os.system("clear")
        print("Fin del juego, no hay ganador")
        break

    os.system("clear")
    #Nuevo turno
    print("Turno de: " + jugadores[jugador_actual][0])

    #Dibujar tablero
    print("0 1 2 3")
    coordenadas_vertical = 1
    for linea in tablero:
        print(coordenadas_vertical, linea[0], linea[1], linea[2])
        coordenadas_vertical += 1

    #Selección de casilla
    coordenada_fila, coordenada_columna = list(map(int, input("Elige coordenadas: ")))
    #Actuaizar tablero
    tablero = actualizar_tablero(jugadores[jugador_actual], coordenada_fila, coordenada_columna, tablero)

    #Comprobamos si ha ganado
    if comprobar_ganador(jugadores[jugador_actual], tablero):
        juego_en_curso = False

        #Dibujar tablero
        os.system("clear")
        print("0 1 2 3")
        coordenadas_vertical = 1
        for linea in tablero:
            print(coordenadas_vertical, linea[0], linea[1], linea[2])
            coordenadas_vertical += 1

        print("Ganador: ",jugadores[jugador_actual][0])

    #Cambio de jugador
    jugador_actual = 1 if jugador_actual == 0 else 0
    
    
    
    # # MENU DEL JUEGO
    # def   MENU ():  
    #     print ("\n++++++++++++++++++++++++")
    #     print("      MENU PRINCIPAL "      )
    #     print("+++++++++++++++++++++++++++")
    #     print("1.         JUGAR           ")
    #     print("2.   MOSTRAR GANADORES     ")
    #     print("3.        SALIR            ")
    #     print("+++++++++++++++++++++++++++")
    
    
#     Se crea una función que inicialice el juego (inicializar_juego):
# Esta función da valor True a la variable juego_en_curso, encargada de ser un flag para terminar el juego.
# Crea una lista de dos elementos, cada elemento es un jugador, cada jugador es una lista de otros dos elementos que son su nombre y su valor representado en el tablero (X y O).
# Elige de forma aleatoria el jugador actual.
# Crea el tablero, es una lista con tres elementos, cada elemento es una línea del tablero.
# Devuelve los valores incializados.
# Se crea una función para actualizar el tablero (actualizar_tablero):
# Recibe como parámetros el jugador del turno actual, las coordenadas que a elegido el jugador y el estado del tablero actualmente.
# Actualiza la casilla que a seleccionado el jugador, colocando en su lugar una X o una O, dependiendo del jugador actual. A la coordenada se resta 1 para seleccionar la ubicación correcta a marcar (las listas comienzan por 0).
# Devuelve el tablero actual.
# Se crea una función para comprobar si el tablero está completo (tablero_completo):
# Recibe como parámetro el tablero actual.
# Devuelve True si no quedan huecos en el tablero, en caso contrario False.
# Se crea una función para comprobar si el jugador a ganado (comprobar_ganador):
# Recibe como parámetros el jugador actual y el tablero actual.
# Realiza comprobaciones por filas, columnas y diagonales para ver si el jugador actual ha ganado el juego, en caso de ganar devuelve True si no devuelve False.
# Ahora se inicializa el juego llamando a la función inicializar_juego y guardando los valores que devuelve en variables.
# A continuación se crea un bucle controlado por la variable juego_en_curso.
# Lo primero que hacemos en el bucle es comprobar si el tablero esta completo, llamando a la función tablero_completo, si está lleno damos valor False a la variable juego_en_curso, rompemos el bucle principal e informamos al usuario de que no hay ganador.
# Limpiamos siempre la pantalla con os.system(«cls»).
# Imprime un mensaje con el nombre del jugador actual.
# Dibujamos el tablero, con las coordenadas horizontales y verticales.
# Imprime un mensaje indicando que seleccione coordenadas, se deben introducir dos números consecutivos, sin espacios, que serán las coordenadas elegidas por el jugador.
# Se actualiza el tablero mediante la función actualizar_tablero.
# Comprobamos si el jugador a ganado mediante la función comprobar_ganador, si el jugador a ganado damos valor False a la variable juego_en_curso, se imprime el tablero con el resultado final y un mensaje indicando el nombre del ganador.
# Cambiamos de un jugador a otro, para ello damos valor 0 a la variable jugador_actual cuando tenga valor 1 y viceversa.
# Seguro que con este resumen del código entendáis el funcionamiento del proyecto en Python, pero este código tiene mucho margen de mejora, te reto a que modifiques el juego implementando lo siguiente:

# El juego no controla que valores se introducen por consola al seleccionar coordenadas, debería de controlarse para impedir que se introduzcan valores o formatos no validos.
# El juego permite introducir coordenadas ya utilizadas y sobre escribir huecos, debería de controlarse que no lo permita.
# Se repite código en varios lugares, deberían de crearse funciones para evitarlo, por ejemplo para imprimir el tablero.
# Se puede eliminar el uso de funciones y crear el juego en una clase, para que funcione mediante programación orientada a objetos, pensad que cada nuevo juego podría ser un objeto.
# ¿Qué más mejorarías de este juego? Prueba a crear tus modificaciones, añade casillas al tablero, que solicite el número de casillas que tendrá, el número de jugadores … todo lo que te imagines, intenta plasmarlo y practicar.

