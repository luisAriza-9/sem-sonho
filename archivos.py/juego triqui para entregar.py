import json

def guardarJuego(lstJugador, ruta):
    try:
        clasificacion = open(ruta, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar datos del jugador.\n", e)
        return None
    
    try:
        json.dump(lstJugador, clasificacion)
    except Exception as e:
        print("Error al guardar la información del jugador.\n", e)
        return None
    
    clasificacion.close()
    return True

def leerElnombre():
    while True:
        try:
            nombre = input("Ingrese el nombre del jugador: ")
            nombre = nombre.strip()
            if len(nombre) == 0 or not nombre.isalnum():
                print("Nombre inválido. Vuelva a digitarlo.")
                continue
            break
        except Exception as e:
            print("Error al ingresar el nombre.\n", e)
    return nombre

def leerFicha():
    while True:
        try:
            ficha = input("Ingrese ficha del jugador 1: (X - O) ")
            ficha = ficha.strip().upper()
            if len(ficha) == 0 or ficha not in ["X", "O"]:
                print("Ficha inválida. Vuelva a digitarla.")
                continue
            return ficha
        except Exception as e:
            print("Error al ingresar la ficha.\n", e)

def leerLarespuesta():
    while True:
        try:
            respuesta = int(input("Ingresa un número entero entre 1 - 9: "))
            if respuesta < 1 or respuesta > 9:
                print("El número está fuera del rango (1-9). Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Error. Número inválido.")
    return respuesta

def jugarLapartida():
    nombre1 = leerElnombre()
    ficha = leerFicha()
    nombre2 = leerElnombre()
    jugadores = [nombre1, nombre2]
    fichero = ["X", "O"] if ficha == "X" else ["O", "X"]
    tablero = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    movimientos = [0, 0]

    while True:
        for i in range(len(jugadores)):
            print(f"El jugador {jugadores[i]} usa la ficha {fichero[i]}")
            print(tablero[0])
            print(tablero[1])
            print(tablero[2])

            respuesta = leerLarespuesta()

            for fila in range(len(tablero)):
                for columna in range(len(tablero[0])):
                    if tablero[fila][columna] == respuesta:
                        tablero[fila][columna] = fichero[i]
                        movimientos[i] += 1

            # Verificar si algún jugador ha ganado
            for i in range(len(jugadores)):
                if (
                    (tablero[0][0] == fichero[i] and tablero[1][1] == fichero[i] and tablero[2][2] == fichero[i]) or
                    (tablero[0][0] == fichero[i] and tablero[1][0] == fichero[i] and tablero[2][0] == fichero[i]) or
                    (tablero[0][0] == fichero[i] and tablero[0][1] == fichero[i] and tablero[0][2] == fichero[i]) or
                    (tablero[0][1] == fichero[i] and tablero[1][1] == fichero[i] and tablero[2][1] == fichero[i]) or
                    (tablero[0][2] == fichero[i] and tablero[1][1] == fichero[i] and tablero[2][0] == fichero[i]) or
                    (tablero[0][2] == fichero[i] and tablero[1][2] == fichero[i] and tablero[2][2] == fichero[i]) or
                    (tablero[1][0] == fichero[i] and tablero[1][1] == fichero[i] and tablero[1][2] == fichero[i]) or
                    (tablero[2][0] == fichero[i] and tablero[2][1] == fichero[i] and tablero[2][2] == fichero[i])
                ):
                    print(f"El jugador {jugadores[i]} 💎💎es el 🥇 ganador💎💎")
                    print(f"Cantidad de movimientos: {movimientos[i]}")
                    return

            # Verificar empate
            if sum(movimientos) == 9:
                print("Empate. No hay movimientos disponibles.")
                return

def menu():
    while True:
        try:
            print("  +++++++ TIC TAC TOE +++++++")
            
            print("|===============================|")
            print("|===============================|")
            
            print("|++++++++ MENÚ PRINCIPAL +++++++|")

            
            print("|===============================|")
            print("|===============================|")
            
            print("1.  |  🎊INICIAR PARTIDA🎊    |    ")
            
            print("2.  | Tabla de clasificación  |    ")
            print("3.  |         Salir           |    ")

            opcion = int(input("    |Seleccione una opción:   |"))
            if opcion < 1 or opcion > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione cualquier tecla para continuar...")
                continue
            return opcion
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione cualquier tecla para continuar...")

while True:
    opcion = menu()

    if opcion == 1:
        jugarLapartida()
    elif opcion == 2:
        pass
    elif opcion == 3:
        print("Hasta Luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presione cualquier tecla para continuar...")
        continue