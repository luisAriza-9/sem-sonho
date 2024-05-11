def menu_principal():
    
    
    
    print("🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜")
    print("🟥                                                                                                            ⬜")           
    print("")                                                                                             
    print("               🔴𝗕𝗜𝗘𝗡𝗩𝗘𝗡𝗜𝗗𝗢 𝗔 𝗠𝗜 𝗖𝗟𝗔𝗥𝗢 𝗖𝗢𝗟𝗢𝗠𝗕𝗜𝗔, 𝗟𝗔 𝗥𝗘𝗗 𝗤𝗨𝗘 𝗡𝗢𝗦 𝗨𝗡𝗘 𝗔 𝗧𝗢𝗗𝗢𝗦🔴 \n".center(100))
    print("🟥                                                                                                            ⬜")
    print("🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜")
    print("  ")
    print("Por favor, ingresa tu tipo de usuario:\n1. Cliente\n2. Administrativo\n3. Salir del menu\n")




def menu_cliente():
    print("⭕Bienvenido al Bot de Usuarios de Mi Claro Colombia⭕\n".center(100))
    print("A continuacion ingrese la opcion que deseas realizar:\n1. Quieres ser claro\n2. Opciones rapidas\n3. Servicio al cliente\n4. Reclamaciones\n5. Sugerencias\n6. Salir\n")

def opc():
    try:
        opc= int(input("Ingresa el numero de opcion correspondiente: "))
        return opc
    except Exception:
        print ("🚫Valor invalido🚫")
        return -1
            #marca en txt

def menu_administrativo():
    print("⬜ Bienvenido al Sistema de Gestion y Ventas de  Mi Claro Colombia 🟥 \n".center(100))
    print("A continuacion ingresa la opcion con la que vas a trabajar:\n1. Usuarios\n2. Productos y Servicios\n3. Reportes\n4. Ventas\n5. Salir")

def admin_usuarios():
    print("¿Que quieres hacer?\n1. Registrar nuevo cliente\n2. Actualizar cliente\n3. Eliminar cliente\n4. Listar clientes\n5. Categoria de Clientes  Mi Claro\n6. Servicios activos Clientes  Mi Claro\n7. Historial interacciones de Clientes Claro\n8. Salir")

def productos_servicios():
    print("¿ Quieres adquirir algo ?\n1. Servicios\n2. Productos\n3.Salir")

def reportes_fallas(): 
    print("¿Tienes fallas?\n1. Productos y servicios populares de claro\n2. Informe de productos y servicios  Mi Claro\n3. Informe producto comprado clientes y cantidad\n4. Salir")

def ventas():
    print("¿ Deseas algun producto?\n1. Acceder a catalogo de venta\n2. Registro venta\n3. Informe venta\n4. Salir")

def productos():
    print ("¿Deseas algun producto?\n1. Acceder a catalogo de venta\n2. Registro venta\n3. Informe venta\n4. Salir")
    
    
    print("******************************************************************************************************************")