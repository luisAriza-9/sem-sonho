def crearMatrices(fil,col):
    m = []

    for i in range(fil):
        fila = [0] * col
        m.append(fila)
    return m

def imprimirMatrices(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j] ,end=" ")
        print("")

def imprimirMatrices(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j] ,end=" ")
        print("")







matriz =    crearMatrices(4,5)
imprimirMatrices(matriz)