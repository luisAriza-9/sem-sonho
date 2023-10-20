


jugadores = [[input("Jugador 1: "),"X"], [input("Jugador 2: "),"O"]]


# MENU DEL JUEGO
def MENU ():  
        while True:
            try:
                print ("\n++++++++++++++++++++++++")
                print("      MENU PRINCIPAL "      )
                print("+++++++++++++++++++++++++++")
                print("1.         JUGAR           ")
                print("2.   MOSTRAR GANADORES     ")
                print("3.        SALIR            ")
                print("+++++++++++++++++++++++++++")
                op = int(input(">>> Opción (1-3)? "))
                if op < 1 or op > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione cualquier tecla para continuar...")



# Bucle principal del juego
while True:
menu()
opcion = input("Seleccione una opción (1/2/3): ").strip()
if opcion == "1":
matriz = [" "]*9
ganadores = cargar_ganadores()
jugador1, jugador1_ficha, jugador2, jugador2_ficha, jugador_inicia = inicio_juego(ganadores)
partida = True


# Cambio en la lógica para decidir quién inicia
if jugador_inicia == jugador2:
jugador1, jugador2 = jugador2, jugador1
jugador1_ficha, jugador2_ficha = jugador2_ficha, jugador1_ficha
tablero(matriz) # Mostrar el tablero al comienzo del juego
while partida:
movimiento_jugador(jugador1, jugador1_ficha, matriz)
tablero(matriz) # Actualizar el tablero después del movimiento


if victoria(matriz):
print(f"💎💎 {jugador1} ({jugador1_ficha})({time.strftime('%Y-%m-%d %H:%M:%S')}) gana la partida 💎💎")
ganadores.append(f"{jugador1} ({jugador1_ficha})({time.strftime('%Y-%m-%d %H:%M:%S')})")
print("💎💎 Fin del juego 💎💎")
# Dentro del bucle de partida, después de una partida terminada:
while True:
jugar_de_nuevo = input("¿Desean jugar de nuevo con los mismos jugadores? (S/N): ").strip().upper()
if jugar_de_nuevo == "S":
matriz = [" "]*9
partida = True # Inicia una nueva partida con los mismos jugadores
if jugador1_ficha == "X":
jugador1_ficha = "O"
jugador2_ficha = "X"
jugador_inicia = jugador2
else:
jugador1_ficha = "X"
jugador2_ficha = "O"
jugador_inicia = jugador1
tablero(matriz) # Mostrar el tablero al comienzo de la nueva partida
break
elif jugar_de_nuevo == "N":
partida = False
break # Salir al menú principal
else:
print("Por favor, ingrese 'S' para jugar de nuevo o 'N' para salir.")


elif empate(matriz):
print("💎💎 Empate")
print("💎💎 Fin del juego 💎💎")
# Dentro del bucle de partida empatada
while True:
jugar_de_nuevo = input("¿Desean jugar de nuevo con los mismos jugadores? (S/N): ").strip().upper()
if jugar_de_nuevo == "S":
matriz = [" "]*9
partida = True # Inicia una nueva partida con los mismos jugadores
if jugador1_ficha == "X":
jugador1_ficha = "O"
jugador2_ficha = "X"
jugador_inicia = jugador2
else:
jugador1_ficha = "X"
jugador2_ficha = "O"
jugador_inicia = jugador1
tablero(matriz) # Mostrar el tablero al comienzo de la nueva partida
break
elif jugar_de_nuevo == "N":
partida = False
break
# Salir al menú principal
else:
print("Por favor, ingrese 'S' para jugar de nuevo o 'N' para salir.")
break


if not partida:
break


movimiento_jugador(jugador2, jugador2_ficha, matriz)
tablero(matriz) # Actualizar el tablero después del movimiento


guardar_ganadores(ganadores) # Guardar la lista de ganadores
elif opcion == "2":
ganadores = cargar_ganadores()
mostrar_ganadores(ganadores)
time.sleep(4)
elif opcion == "3": # salir del programa
print("Gracias por usar el programa")
break
