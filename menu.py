def menu_principal():
    print("")
    print("¡Bienvenido a Claro Colombia, la red que nos une!\n".center(60))
    print("Por favor, ingresa tu tipo de usuario:\n1. Cliente\n2. Administrador\n3. Salir del sistema\n")

def menu_cliente():
    print("¡Bienvenido al Portal de Usuarios de Claro Colombia!\n".center(60))
    print("A continuacion ingrese la opcion que quieres realizar:\n1. Llena encuesta Claro!\n2. Hecho especialmente para ti!\n3. Servicio al cliente\n4. Reclamaciones\n5. Sugerencias\n6. Salir\n")

def opc():
    try:
        opc= int(input("Ingresa el numero de opcion correspondiente: "))
        return opc
    except Exception:
        print ("Valor invalido")
        return -1
            #marca en txt

def menu_admin():
    print("¡Bienvenido al Sistema de Gestion y Ventas de Claro Colombia!\n".center(60))
    print("A continuacion ingresa la opcion con la que vas a trabajar:\n1. Usuarios\n2. Productos y Servicios\n3. Reportes\n4. Ventas\n5. Salir")

def admin_usuarios():
    print("¿Que quieres hacer?\n1. Registrar nuevo cliente\n2. Actualizar cliente\n3. Eliminar cliente\n4. Listar clientes\n5. Categoria de Clientes Claro\n6. Servicios activos Clientes Claro\n7. Historial interacciones de Clientes Claro\n8. Salir")

def productos_servicios():
    print("¿Que quieres hacer?\n1. Servicios\n2. Productos\n3.Salir")

def reportes(): 
    print("¿Que quieres hacer?\n1. Productos y servicios populares de claro\n2. Informe de productos y servicios Claro\n3. Informe producto comprado clientes y cantidad\n4. Salir")

def ventas():
    print("¿Que quieres hacer?\n1. Acceder a catalogo de venta\n2. Registro venta\n3. Informe venta\n4. Salir")