import json

def cargar(archivo):
    datos={}
    with open (archivo,"r") as entrada:
        datos= json.load(entrada)
    return datos

def guardar(datos,archivo):
    datos= dict(datos)

    diccionario_actualizado= json.dumps(datos, indent=4)
    salida= open(archivo,"w")
    salida.write(diccionario_actualizado)
    salida.close()
