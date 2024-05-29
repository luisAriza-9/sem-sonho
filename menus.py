from datetime import datetime

def menu_principal():
    print("🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪")
    print("¡Bienvenido a Claro Colombia, la red que nos une!\n".center(100))
    print("🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪")
    print("Por favor, ingresa tu tipo de usuario:\n1. Cliente\n2. Administrador\n3. Salir del sistema\n")

def menu_cliente():
    print("🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪")
    print("¡Bienvenido al Portal de Usuarios de Claro Colombia!\n".center(100))
    print("🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪")
    print("A continuacion ingrese la opcion que quieres realizar:\n1. Llena encuesta Claro!\n2. Hecho especialmente para ti!\n3. Adquiere los productos claro!\n4. Servicio al cliente\n5. Reclamaciones\n6. Sugerencias\n7. Salir\n")

def opc():
    try:
        opc= int(input("Ingresa el numero de opcion correspondiente: "))
        return opc
    except Exception:
        error= "Valor invalido"
        print (error)
        registrar_txt(error)
        return -1
            #marca en txt

def menu_admin():
    print("🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪")
    print("¡Bienvenido al Sistema de Gestion y Ventas de Claro Colombia!\n".center(100))
    print("🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪🟥⚪")
    print("A continuacion ingresa la opcion con la que vas a trabajar:\n1. Usuarios\n2. Productos y Servicios\n3. Reportes\n4. Ventas\n5. Salir")

def admin_usuarios():
    print("¿Que quieres hacer?\n1. Registrar nuevo cliente\n2. Actualizar cliente\n3. Eliminar cliente\n4. Listar clientes\n5. Categoria de Clientes Claro\n6. Historial interacciones de Clientes Claro\n7. Salir")

def productos_servicios():
    print("¿Que quieres hacer?\n1. Servicios\n2. Productos\n3. Manipular categorias\n4. Salir")

def reportes(): 
    print("¿Que quieres hacer?\n1. Productos y servicios populares de claro\n2. Informe de productos y servicios Claro\n3. Informe producto comprado clientes y cantidad\n4. Salir")

def ventas():
    print("¿Que quieres hacer?\n1. Acceder a catalogo de venta\n2. Registro venta\n3. Informe venta\n4. Salir")

def admin_servicios():
    print("¿Que quieres hacer?\n1. Registrar nuevo servicio\n2. Actualizar servicio\n3. Eliminar servicio\n4. Mostrar servicios\n5. Salir")

def admin_productos():
    print("¿Que quieres hacer?\n1. Registrar nuevo producto\n2. Actualizar producto\n3. Eliminar producto\n4. Mostrar productos\n5. Salir")

def registrar_txt(error):
    fecha= str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    with open("registro_errores.txt", "a") as registro_errores:
        registro_errores.write(f"{fecha} Error: {error}\n")

def manejar_categorias(datos):
    datos= dict(datos)
    print("¿Que quieres hacer?\n1. registrar categoria nueva\n2. Eliminar categoria\n3. Salir")
    opcion= opc()
    while opcion not in [1,2,3]:
        opcion =opc()
        print("Ingresa una opcion valida\n")
    if opcion==1:
        categoria= input("Ingresa el nombre de la categoria: ").lower()
        if not categoria in datos["categorias"]:
            datos["categorias"].append(categoria)
            print("Categoria guardada!")
        else:
            print("Categoria ya existente!")
    elif opcion==2:
        categoria= input("Ingresa el nombre de la categoria a eliminar: ")
        if categoria in datos["categorias"]:
            datos["categorias"].remove(categoria)
            print("Categoria eliminada!")
        else:
            print("La categoria no existe")
    else:
        print("Decidiste salir de Categorias!")
    return datos