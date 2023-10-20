


# INSRUCCUINES ESTE SERA EL TABLERO





#  0     1    2
#  --------------
#  0   |    |
#   -------------
#  1   |    | 
#   -------------
#  2   |    |
#   -------------    









# Función para imprimir el tablero actual
def imprimirEltablero(tablero):
    for fila in tablero:
        print(' | '.join(fila))
        print('---' * len(fila))

# Función para verificar si hay un ganador
def verificarElganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True
    # Verificar columnas
    for col in range(len(tablero[0])):
        if all(tablero[fila][col] == jugador for fila in range(len(tablero))):
            return True
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(len(tablero))) or \
            all(tablero[i][len(tablero) - 1 - i] == jugador for i in range(len(tablero))):
        return True
    return False

# Función principal para el juego
def jugar_tic_tac_toe():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador =   'X'
    
    while True:
        imprimirEltablero(tablero)
        fila = int(input(f'Jugador {jugador}, elige una fila (0, 1, 2): '))
        col = int(input(f'Jugador {jugador}, elige una columna (0, 1, 2): '))

        
        
        
        if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == ' ':
            tablero[fila][col] = jugador
            if verificarElganador(tablero, jugador):
                imprimirEltablero(tablero)
                print(f'¡Jugador {jugador} ha ganado!')
                break
            elif ' ' not in [casilla for fila in tablero for casilla in fila]:
                imprimirEltablero(tablero)
                print('El juego ha terminado en empate.')
                break
            jugador = 'X' if jugador == 'O' else 'O'
        else:
            print('Movimiento no válido. Por favor, intenta de nuevo.')

# Iniciar el juego
jugar_tic_tac_toe()


# jugadores = [[input("Jugador 1: "),"X"], [input("Jugador 2: "),"O"]]


# # MENU DEL JUEGO
# def MENU ():  
#         while True:
#             try:
#                 print ("\n++++++++++++++++++++++++")
#                 print("      MENU PRINCIPAL "      )
#                 print("+++++++++++++++++++++++++++")
#                 print("1.         JUGAR           ")
#                 print("2.   MOSTRAR GANADORES     ")
#                 print("3.        SALIR            ")
#                 print("+++++++++++++++++++++++++++")
#                 op = int(input(">>> Opción (1-3)? "))
#                 if op < 1 or op > 3:
#                 print("Opción no válida. Escoja de 1 a 3.")
#                 input("Presione cualquier tecla para continuar...")
#                 continue
#             return op
#         except ValueError:
#             print("Opción no válida. Escoja de 1 a 3.")
#             input("Presione cualquier tecla para continuar...")





