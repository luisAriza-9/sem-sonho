

archivo = open ("Temas de Clase/archivos/nombres.txt","r")
texto = archivo.read()
print(texto)
archivo.close()
#print (texto)



archivo.seek(0)
texto2 = archivo. readline()
print (texto2)
archivo.close()


texto3 = archivo.readlines()
print(texto3)
archivo.close()