tablero=(" " * 9)#Nuestro tablero inicialmente sera nueve casillas vacias


#Colocar ficha en el tablero
def colocarficha():
    while True:
        fila=input("fila:") 
        columna=input("columna":)
    
    #Como mi tablero es  3x3
    casilla=fila*3+columna
    if(tablero[casilla]!=""):
        #Esa casilla ya esta cubierta 
    else:
        tablero[casilla]="OX"
        return

    



jugador1=input("Nombre del jugador o alias 1:")
jugador2=input("Nombre del jugador o alias 2 :")


#Iniciamos el juego


continuar=True 
fichasEneltablero=0
while continuar:
    #pedimos posicion de la ficha 
    colocarficha()
    fichasEneltablero+=1
    if (fichasEneltablero==9):
        continuar= False