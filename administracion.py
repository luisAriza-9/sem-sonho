from menus import*
import uuid
from datetime import datetime
from menus import*

def codigo_unico():
    codigo= str(uuid.uuid4())
    return codigo
#usuarios
def registrar_clientes(datos):
    datos= dict(datos)
    cliente ={}
    print("-------------------------------------------------------------------------")
    cliente["nombre"]= input("Ingresa el nombre del cliente: ")
    cliente["codigo"]= codigo_unico()
    print("El codigo unico del cliente es "+cliente["codigo"])
    cliente["email"]= input("Ingresa un email valido del cliente: ")
    try:
        telefono= int(input("Ingresa el telefono del cliente: "))
        while not len(str(telefono)) == 10:
            print("Numero de telefono invalido")
            telefono= int(input("Ingresa el telefono del cliente: "))
    except Exception:
        Error= "Numero de telefono invalido!"
        print (Error)
        registrar_txt(Error)
        telefono= 0
    
    cliente["telefono"]= telefono
    cliente["ciudad"]= input("Ingresa la ciudad donde vive: ")
    cliente["direccion"]= input("Ingresa la direccion del cliente: ")
    cliente["compras"]= 0
    cliente["adquiridos"]= []
    cliente["publicidad"]= []
    cliente["servicio_al_cliente"]= []

    datos["clientes"].append(cliente)
    print ("Cliente cargado!, cierra el programa para ver los cambios")
    return datos

def actualizar_clientes(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    usuario= input("Ingresa el codigo del cliente a cambiar: ")
    encontrado= False
    for cliente in datos["clientes"]:
        if usuario== cliente["codigo"]:
            encontrado= True
            while True: 
                print("Que datos quieres actualizar\n1.Nombre\n2.Codigo\n3.Email\n4.Telefono\n5.Ciudad\n6.Direccion\n7.Salir")
                opcion= opc()
                while opcion not in [1,2,3,4,5,6,7]:
                    print("Ingresa una opcion valida\n")
                    opcion =opc()
                if opcion==1:
                    cliente["nombre"]= input("Ingrese el nuevo nombre del cliente: ")
                    print("guardado!")
                elif opcion==2:
                        codigo_nuevo= cliente["codigo"]= codigo_unico()
                        print("guardado!")
                        print("El codigo nuevo del cliente "+codigo_nuevo)
                elif opcion==3:
                        cliente["email"]= input("Ingrese el nuevo email del cliente: ")
                        print("guardado!")
                elif opcion==4: 
                    try:
                        telefono= int(input("Ingresa el telefono del cliente: "))
                        while not len(str(telefono)) == 10:
                            print("Numero de telefono incompleto, revisalo de nuevo!")
                            telefono= int(input("Ingresa el telefono del cliente: "))
                    except Exception:
                        Error= "Numero de telefono invalido!"
                        print (Error)
                        registrar_txt(Error)
                    cliente["telefono"]=telefono
                    print("guardado!")
                elif opcion==5:
                    cliente["ciudad"]= input("Ingrese la nueva ciudad del cliente: ")
                    print("guardado!")
                elif opcion==6:
                    cliente["direccion"]= input("Ingrese la nueva direccion del cliente: ")
                    print("guardado!")
                else:
                    print("Saliste de actualizar clientes!")
                    break
    if encontrado== False:
        print("Codigo de usuario no encontrado")
    return datos

def eliminar_usuario(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    usuario= input("Ingresa el codigo del cliente a eliminar: ")
    encontrado= False
    for i in range (len(datos["clientes"])):
        if usuario== datos["clientes"][i]["codigo"]:
            encontrado= True
            datos["clientes"].pop(i)
            print("Usuario eliminado!")
            return datos
    if encontrado== False:
        print("Codigo de usuario no encontrado")
    return datos

def listar_usuarios(datos):
    datos= dict(datos)
    indice= 1
    print("-------------------------------------------------------------------------")
    print("Lista de clientes\n")
    for cliente in datos["clientes"]:
        print(str(indice)+"."+" Nombre: " + cliente["nombre"]+ " - "+ "Codigo: "+ cliente["codigo"])
        print("")
        indice+=1

def categoria_clientes_claro(datos):
    datos= dict(datos)
    clientes_nuevos=[]
    clientes_leales= []
    clientes_regulares=[]

    for cliente in datos["clientes"]:
        cliente_completo= cliente['nombre']+ " - " + cliente['codigo'] + " - " +"compras: "+ str(cliente['compras'])
        if cliente["compras"] >= 0 and cliente["compras"] < 12:
            clientes_nuevos.append(cliente_completo)
        elif cliente["compras"] >=  12 and cliente["compras"] < 20:
            clientes_regulares.append(cliente_completo)
        else:
            clientes_leales.append(cliente_completo)
    
    print("Bienvenido a las categorias de Clientes Claro!, ¿Que quieres ver?:\n1. Clientes Nuevos\n2. Clientes Regulares\n3. Clientes Leales\n4. Salir\n")
    opcion= opc()
    while opcion not in [1,2,3,4]:
        print("Ingresa una opcion valida\n")
        opcion =opc()
    if opcion==1:
        print("")    
        print("Estos son los nuevos clientes Claro!: \n")
        cont=1
        for i in clientes_nuevos:
            print(str(cont)+". "+i)
            cont+=1
    elif opcion==2:
        contr=1
        print("")
        print("Estos son los clientes regulares de Claro!: \n")
        for i in clientes_regulares:
            print(str(contr)+". "+i)
            contr+=1
    elif opcion==3: 
        contl=1
        print("")
        print("Estos son los clientes leales a Claro!: \n")
        for i in clientes_leales:
            print(str(contl)+". "+i)
            contl+=1
    else:
        print("Decidiste salir de categorias de Claro!")

def interacciones_usuarios(datos):
    datos=dict(datos)

    codigo_cliente= input("Ingresa el codigo del cliente: ")
    encontrado= False
    for cliente in datos["clientes"]:
        if codigo_cliente == cliente["codigo"]:
            encontrado= True
            print("Bienvenido al historial de interacciones de Clientes Claro!, ¿Que quieres ver?:\n1. Interacciones con Servicio al Cliente\n2. Interacciones con Reclamaciones\n3. Interacciones con Sugerencias\n4. Salir")
            print(f"Accediste al Historial de {cliente['nombre']}")
            print("")
            opcion= opc()
            while not opcion in [1,2,3,4]:
                print("Ingresa una opcion valida\n")
                opcion =opc()
            if opcion==1:
                print("Interacciones con servicio al cliente: ")
                for i in cliente["servicio_al_cliente"]:
                    print(i)
                    print("")
            elif opcion==2:
                print("Interacciones con Reclamaciones:")
                for i in cliente["reclamaciones"]:
                    print(i)
                    print("")
            elif opcion==3:
                print("Interacciones con Sugerencias:")
                for i in cliente["sugerencias"]:
                    print(i)
                    print("")
            else:
                print("Decidiste salir de Historial de interacciones de Clientes Claro!")
    if encontrado== False:
        print("Codigo de usuario no encontrado")
    return datos

#servicios
def registrar_servicios(datos):
    datos= dict(datos)
    categorias= datos["categorias"]
    servicio ={}
    print("-------------------------------------------------------------------------")
    servicio["nombre_serv"]= input("Ingresa el nombre del servicio: ")
   

    servicio["codigo"]= codigo_unico()
    print("El codigo unico del servicio es "+ servicio["codigo"])
    categoria= input(f"Ingresa la categoria del servicio, recuerda que las categorias disponibles son {','.join(categorias)}:  ").lower()
    while categoria not in categorias:
        print("No esta en las categorias disponibles!")
        categoria= input("Ingresa la categoria del producto: ").lower()
    servicio["categoria"]= categoria
    servicio["descripcion"]= input("Ingresa la descripcion del servicio: ")
    servicio["precio"]= input("El precio del servicio: ")
    servicio["cantidad_vendida"]=0


    datos["servicios"].append(servicio)
    print ("Servicio listo!, cierra el programa para ver los cambios")
    return datos

def actualizar_servicios(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    codigo_serv= input("Ingresa el codigo del servicio a cambiar: ")
    encontrado= False
    for servicio in datos["servicios"]:
        if codigo_serv== servicio["codigo"]:
            encontrado= True
            while True: 
                print("Que datos quieres actualizar\n1.Nombre\n2.Codigo\n3.Categoria\n4.Descripcion\n5.Precio\n6.Salir")
                opcion= opc()
                while opcion not in [1,2,3,4,5,6]:
                    print("Ingresa una opcion valida\n")
                    opcion =opc()
                if opcion==1:
                    servicio["nombre_serv"]= input("Ingrese el nuevo nombre del servicio: ")
                    print("guardado!")
                elif opcion==2:
                        codigo_nuevo= servicio["codigo"]= codigo_unico()
                        print("guardado!")
                        print("El codigo nuevo del servicio es "+codigo_nuevo)
                elif opcion==3:
                        categoria= input("Ingrese la nueva categoria del servicio: ").lower()
                        while not categoria in datos["categorias"]:
                            print("No esta en las categorias disponibles!")
                            categoria= input("Ingrese la nueva categoria del servicio: ").lower()
                        servicio["categoria"]= categoria
                        print("guardado!")
                elif opcion==4:
                    servicio["descripcion"]= input("Ingrese la nueva descripcion del servicio: ")
                    print("guardado!")
                elif opcion==5:
                    servicio["precio"]= input("Ingrese el precio actualizado del servicio: ")
                    print("guardado!")
                else:
                    print("Saliste de actualizar servicios!")
                    break
    if encontrado== False:
        print("Codigo de servicio no encontrado")
    return datos

def eliminar_servicio(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    servicio_codigo= input("Ingresa el codigo del servicio a eliminar: ")
    encontrado= False
    for i in range (len(datos["servicios"])):
        if servicio_codigo== datos["servicios"][i]["codigo"]:
            encontrado= True
            datos["servicios"].pop(servicio_codigo)
            print("Servicio eliminado!")
            return datos
    if encontrado== False:
        print("Codigo de servicio no encontrado")
    return datos

def listar_servicios(datos):
    datos= dict(datos)
    indice= 1
    print("-------------------------------------------------------------------------")
    print("Lista de servicios\n")
    for servicio in datos["servicios"]:
        print(str(indice)+"."+" Nombre: " + servicio["nombre_serv"]+ " - "+ "Codigo: "+servicio["codigo"])
        print("")
        indice+=1

#productos 
def registrar_productos(datos):
    datos= dict(datos)
    categorias= datos["categorias"]
    producto ={}
    print("-------------------------------------------------------------------------")
    producto["nombre"]= input("Ingresa el nombre del producto: ")
    producto["codigo"]= codigo_unico()
    print("El codigo unico del producto es "+producto["codigo"])
    categoria= input(f"Ingresa la categoria del producto, recuerda que las categorias disponibles son {','.join(categorias)}:  ").lower()
    while categoria not in categorias:
        print("No esta en las categorias disponibles!")
        categoria= input("Ingresa la categoria del producto: ").lower()
    producto["categoria"]= categoria 
    producto["marca"]= input("Ingresa la marca del producto: ")
    producto["caracteristicas"]= input("Ingresa las caracteristicas del producto: ")
    producto["garantia"]= input("Ingresa la duracion de garantia del producto: ")
    producto["precio"]= input("Ingresa el precio del producto: ")
    producto["cantidad_vendida"]=0


    datos["productos"].append(producto)
    print ("Producto listo!, cierra el programa para ver los cambios")
    return datos

def actualizar_productos(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    codigo_producto= input("Ingresa el codigo del producto a cambiar: ")
    encontrado= False
    for producto in datos["productos"]:
        if codigo_producto== producto["codigo"]:
            encontrado= True
            while True: 
                print("Que datos quieres actualizar\n1.Nombre\n2.Codigo\n3.Marca\n4.Categoria\n5.Caracteristicas\n6.Garantia\n7.Precio\n8.Salir")
                opcion= opc()
                while opcion not in [1,2,3,4,5,6,7,8]:
                    print("Ingresa una opcion valida\n")
                    opcion =opc()
                if opcion==1:
                    producto["nombre"]= input("Ingrese el nuevo nombre del producto: ")
                    print("guardado!")
                elif opcion==2:
                    codigo_nuevo= producto["codigo"]= codigo_unico()
                    print("guardado!")
                    print("El codigo nuevo del producto es "+codigo_nuevo)
                elif opcion==3:
                        producto["marca"]= input("Ingrese la nueva marca del producto: ")
                        print("guardado!")
                elif opcion==4:
                    categoria= input("Ingrese la nueva categoria del producto: ").lower()
                    while not categoria in datos["categorias"]:
                        print("No esta en las categorias disponibles!")
                        categoria= input("Ingrese la nueva categoria del producto: ").lower()
                    producto["categoria"]= categoria
                    print("guardado!")
                elif opcion==5:
                    producto["caracteristicas"]= input("Ingrese las caracteristicas actualizadas del producto: ")
                    print("guardado!")
                elif opcion==6:
                    producto["garantia"]= input("Ingrese la nueva garantia del producto: ")
                    print("guardado!")
                elif opcion==7:
                    producto["precio"]= input("Ingrese el precio actualizado del producto: ")
                    print("guardado!")
                else:
                    print("Saliste de actualizar productos!")
                    break
    if encontrado== False:
        print("Codigo de producto no encontrado")
    return datos
    
def eliminar_producto(datos):
    datos= dict(datos)
    print("-------------------------------------------------------------------------")
    producto= input("Ingresa el codigo del producto a eliminar: ")
    encontrado= False
    for i in range (len(datos["productos"])):
        if producto== datos["productos"][i]["codigo"]:
            encontrado= True
            datos["productos"].pop(i)
            print("Producto eliminado!")
            return datos
    if encontrado== False:
        print("Codigo de producto no encontrado")
    return datos

def listar_productos(datos):
    datos= dict(datos)
    indice= 1
    print("-------------------------------------------------------------------------")
    print("Lista de productos\n")
    for producto in datos["productos"]:
        print(str(indice)+"."+" Nombre: " + producto["nombre"]+ " - "+ "Codigo: "+ producto["codigo"])
        print("")
        indice+=1

#clientes
def registrar_compra(datos):
    datos= dict(datos)
    codigo= input("Ingresa tu codigo personal de cliente Claro: ")
    encontrado= False
    servicio_encontrado= False
    producto_encontrado= False
    for cliente in datos["clientes"]:
        if codigo == cliente["codigo"]:
            encontrado= True
            print("¿Que deseas adquirir?:\n1.Servicios\n2.Productos\n3.Salir")
            opcion=opc()
            while not opcion in [1,2,3]:
                opcion =opc()
                print("Escoge una opcion valida\n")
            if opcion==1:
                try:
                    cantidad_compra= int(input("Ingresa la cantidad del servicio que vas a adquirir: "))
                except Exception:
                    error= "Cantidad no valida"
                    print(error)
                    registrar_txt(error)
                    cantidad_compra= 0
                if cantidad_compra==0:
                    break
                codigo_servicio= input("Ingresa el codigo del servicio que vas a adquirir: ")
                for servicio in datos["servicios"]:
                    if codigo_servicio== servicio["codigo"]:
                        servicio_encontrado= True
                        compras_anteriores= cliente["compras"]
                        compras_totales= cantidad_compra + compras_anteriores
                        servicio_comprado= (servicio["nombre_serv"]+ " Cantidad: "+ str(cantidad_compra))
                        cliente["compras"]= compras_totales
                        cliente["adquiridos"].append(servicio_comprado)
                        print("Gracias!, tu compra fue realizada")
                if servicio_encontrado== False:
                    print("Codigo de servicio no encontrado")
                    
            elif opcion==2:
                try:
                    cantidad_compra= int(input("Ingresa la cantidad del producto que vas a adquirir: "))
                except Exception:
                    error= "Cantidad no valida"
                    print(error)
                    registrar_txt(error)
                    cantidad_compra= 0
                if cantidad_compra==0:
                    break
                codigo_producto= input("Ingresa el codigo del producto que vas a adquirir: ")
                for producto in datos["productos"]:
                    if codigo_producto== producto["codigo"]:
                        producto_encontrado= True
                        compras_anteriores= cliente["compras"]
                        compras_totales= cantidad_compra + compras_anteriores
                        producto_comprado= (producto["nombre"]+ " Cantidad: " + str(cantidad_compra))
                        producto_vendido= producto["cantidad_vendida"]
                        total_producto_ahora= producto_vendido+ cantidad_compra
                        producto["cantidad_vendida"]= total_producto_ahora
                        cliente["compras"]= compras_totales
                        cliente["adquiridos"].append(producto_comprado)
                        print("Gracias!, tu compra fue realizada")
                if producto_encontrado== False:
                    print("Codigo de producto no encontrado")
            else:
                print("Saliste de Adquiere los productos Claro!")
    if encontrado== False:
        print("Codigo de cliente no encontrado")

    return datos

def encuesta_publicidad(datos):
    datos= dict(datos)
    publicidad_eleccion=[]
    codigo= input("Ingresa tu codigo usuario Claro!: ")
    encontrado= False
    for cliente in datos["clientes"]:
        if codigo== cliente["codigo"]:
            encontrado= True
            celulares= 0
            hogar= 0
            computadores=0
            streaming=0
            servicio_movil=0

            print(" ")
            print(f" {datos['clientes'][i]['nombre']}, Bienvenido a la encuesta de preferencias Claro!\n".center(60)) 
            print("En Claro nos esforzamos por brindarte servicios y productos que se adapten perfectamente a tus necesidades y preferencias. Para asegurarnos de que recibas la mejor experiencia posible, nos gustaría conocer más sobre ti y tus intereses, debes terminar la encuesta hasta el final ¡Empecemos!\n")
            print("1. ¿Que edad tienes?\n1. 18-25 años\n2. 26-35 años\n3. 36-45 años \n4. Mayor de 45 años\n")
            opcion= opc()
            while not opcion in [1,2,3,4]:
                print("Opcion incorrecta, elige una valida!")
                opcion=opc()

            if opcion==1:
                celulares+=2
                computadores+=2
                servicio_movil+=2
            elif opcion==2 or opcion==3:
                celulares+=2
                computadores+=2
                servicio_movil+=2
                hogar+=2
            else:
                celulares+=1
                computadores+=1
                servicio_movil+=2
                hogar+=2

            print(" ")
            print("2.¿Con qué frecuencia usas servicios de streaming de video?\n1. Diariamente\n2. Una vez por semana\n3. Varias veces al mes  \n4. Casi nunca\n")
            opcion= opc()
            while not opcion in [1,2,3,4]:
                print("Opcion incorrecta, elige una valida!")
                opcion= opc()

            if opcion==1:
                streaming+=3
            elif opcion==2: 
                streaming+=2
            elif opcion==3:
                streaming+=1   
            else:
                streaming=streaming

            print(" ")
            print("3. ¿Cuánto tiempo pasas en tus dispositivos móviles al día?\n1. Menos de 1 hora\n2. 1-2 horas\n3. 2-4 horas\n4. Más de 6 horas\n")
            opcion= opc()
            while not opcion in [1,2,3,4]:
                print("Opcion incorrecta, elige una valida!")
                opcion= opc()

            if opcion==1:
                servicio_movil+=1
            elif opcion==2: 
                servicio_movil+=2
            elif opcion==3:
                servicio_movil+=3
            else:
                servicio_movil+=4

            print(" ")
            print("4. ¿Con qué frecuencia sueles renovar tu teléfono celular?\n1. Menos de 1 año\n2. 1-2 años\n3. 3 años\n4. No suelo cambiar mi telefono a menudo\n")
            opcion= opc()
            while not opcion in [1,2,3,4]:
                print("Opcion incorrecta, elige una valida!")
                opcion= opc()

            if opcion==1:
                celulares+=4
            elif opcion==2: 
                celulares+=3
            elif opcion==3:
                celulares+=2
            else:
                celulares=celulares

            print(" ")
            print("5. ¿Qué tan importante es para ti la velocidad de internet en casa?\n1. Demasiado importante\n2. Considerablemente importante\n3.Poco importante \n4. Nada importante\n")
            opcion= opc()
            while not opcion in [1,2,3,4]:
                print("Opcion incorrecta, elige una valida!")
                opcion=opc()

            if opcion==1:
                hogar+=4
            elif opcion==2: 
                hogar+=3
            elif opcion==3:
                hogar+=2
            else:
                hogar=hogar

            print(" ")
            print("6. ¿Qué tipo de actividades realizas principalmente en tu computadora portátil?\n1. Trabajo/Estudios\n2. Juegos\n3. Oscio\n4. No uso coputadora\n")
            opcion= opc()
            while not opcion in [1,2,3,4]:
                print("Opcion incorrecta, elige una valida!")
                opcion=opc()

            if opcion==1:
                computadores+=4
            elif opcion==2: 
                computadores+=4
            elif opcion==3:
                computadores+=2
            else:
                computadores=computadores
            
            categorias= {"computadores":computadores,"hogar":hogar,"servicio_movil":servicio_movil,"streaming":streaming,"celulares":celulares}
            
            max_puntuacion= max(categorias.values())
            categorias_maximas= [categoria for categoria,puntuacion in categorias.items() if puntuacion== max_puntuacion]
            publicidad_eleccion.append(categorias_maximas)
            cliente["publicidad"]= publicidad_eleccion
            print("Gracias por responder! tus resultados se veran reflejados en 'Hechos especialmente para ti'")
    if encontrado== False:
        print("Codigo de cliente no encontrado")
    return datos

def publicidad(datos): 
    datos= dict(datos)
    codigo= input("Ingresa tu codigo personal de cliente Claro: ")
    encontrado= False
    print(" ")
    print ("Tenemos estos servicios solo para ti!\n")
    for cliente in datos["clientes"]:
        if codigo== cliente["codigo"]:
            encontrado= True
            categoria_mostrar= cliente["publicidad"][0]
            for servicio in datos["servicios"]:
                if servicio["categoria"] in categoria_mostrar:
                    print(servicio["nombre_serv"])
                    print(servicio["descripcion"])
                    print("$"+servicio["precio"])
                    print(" ")
            print("Mira estos productos!\n")
            for producto in datos["productos"]:
                if producto["categoria"] in categoria_mostrar:
                    print(producto["nombre"])
                    print(producto["caracteristicas"])
                    print("$"+producto["precio"])
                    print(" ")
    if encontrado== False:
        print("Codigo de cliente no encontrado")
    return datos

def servicio_al_cliente(datos):
    datos=dict(datos)
    codigo= input("Ingresa tu codigo personal de cliente Claro: ")
    encontrado= False
    print(" ")
    for cliente in datos["clientes"]:
        if codigo== cliente["codigo"]:
            encontrado= True 
            print(f"Hola {cliente['nombre']}, recuerda que estamos aqui para ayudarte en todo lo que necesites. Si tienes alguna pregunta o requerimiento, no dudes en contactarnos. Estamos disponibles para brindarte el mejor servicio posible.")
            comentario= input("Por favor ingresa tu comentario o problema, un tecnico te respondera en momentos: ")
            cliente["servicio_al_cliente"].append(comentario)
            print("Analizaremos tu comentario detalladamente, cierra el programa para cargarlo!")
            print("Gracias por ser parte de la familia Claro Colombia!")
    if encontrado== False:
        print("Codigo de cliente no encontrado")
    return datos 

def reclamaciones(datos):
    datos=dict(datos)
    codigo= input("Ingresa tu codigo personal de cliente Claro: ")
    encontrado= False
    print(" ")
    for cliente in datos["clientes"]:
        if codigo== cliente["codigo"]:
            encontrado= True
            print(f"Hola {cliente['nombre']}, entendemos lo importante que es tener un servicio confiable y de calidad, por lo que estamos comprometidos a resolver cualquier problema que hayas experimentado lo antes posible.")
            problema = input("Por favor, proporciona más detalles sobre tu reclamación, incluyendo cualquier numero de referencia o detalle especifico que pueda ayudarnos a entender mejor la situacion. Nuestro equipo esta aqui para escucharte y trabajar contigo para encontrar una solución satisfactoria: ")
            cliente["reclamaciones"].append(problema)
            print("Cargado! cierra el programa correctamente para actualizarlo en nuestra base de datos\n")
            print("Agradecemos tu paciencia y colaboración mientras trabajamos en esta situación. Tu opinión es fundamental para nosotros y queremos asegurarnos de brindarte el mejor servicio posible.")
    if encontrado== False:
        print("Codigo de cliente no encontrado")
    return datos 

def sugerencias(datos):
    datos=dict(datos)
    codigo= input("Ingresa tu codigo personal de cliente Claro: ")
    encontrado= False
    print(" ")
    for cliente in datos["clientes"]:
        if codigo== cliente["codigo"]:
            encontrado= True
            print(f"Hola {cliente['nombre']}, queremos agradecerte por tomarte el tiempo para compartir tus sugerencias con nosotros. Cada comentario que recibimos nos permite entender mejor tus necesidades y expectativas, y nos impulsa a buscar nuevas formas de superarlas.")
            sugerencia = input("Si tienes alguna idea, comentario o sugerencia adicional que te gustaría compartir con nosotros por favor escribela: ")
            cliente["sugerencias"].append(sugerencia)
            print("Cargado! cierra el programa correctamente para actualizarlo en nuestra base de datos\n")
            print("Gracias nuevamente por tu apoyo continuo y por ser parte de la familia Claro. Esperamos seguir siendo tu proveedor de confianza por muchos años más.")
    if encontrado== False:
        print("Codigo de cliente no encontrado")
    return datos 

#reportes
def servicios_productos_catalogo(datos):
    datos= dict(datos)
    print("La cantidad de servicios ofrecidos son: "+ str(len(datos["servicios"])))
    print("")
    for servicio in datos["servicios"]:
        print (f"""Servicio: {servicio["nombre_serv"]}\nCodigo: {servicio["codigo"]}\nCategoria: {servicio["categoria"]}\nDescripcion: {servicio["descripcion"]}\nPrecio: {servicio["precio"]}\n""")

    print("La cantidad de productos ofrecidos son: "+ str(len(datos["productos"])))
    print("")
    for producto in datos["productos"]:
        print (f"""Producto: {producto["nombre"]}\nCodigo: {producto["codigo"]}\nMarca: {producto["marca"]}\nCategoria: {producto["categoria"]}\Caracteristicas: {producto["caracteristicas"]}\nPrecio: {producto["precio"]}\nGarantia: {producto["garantia"]}""")

    print("La totalidad de productos y servicios de Claro es de: " + str((len(datos['servicios']))+(len(datos['productos']))))

def registro_compras(datos):
    datos= dict (datos)
    for cliente in datos["clientes"]:
        if cliente["adquiridos"] != []:
            print("Cliente :" + cliente["nombre"])
            print("Codigo: " + cliente["codigo"])
            print("Compro: " + ", ".join((cliente['adquiridos'])))
            print("")
    return datos

def servicios_productos_populares(datos):
    venta= {}
    for servicio in datos["servicios"]:
        cantidad_vendida= servicio["cantidad_vendida"]
        servicio_nombre= servicio["nombre_serv"]
        venta[servicio_nombre]= cantidad_vendida
    maxima_venta= max(venta.values())
    categoria_maxima= [categoria for categoria,cantidad in venta.items() if cantidad==maxima_venta]

    print(f"Los servicios mas populares en Claro Colombia por el momento son {','.join(categoria_maxima)} con ventas de {maxima_venta}")
    venta_productos={}
    for producto in datos["productos"]:
        cantidad_vendida_productos= producto["cantidad_vendida"]
        producto_nombre= producto["nombre"]
        venta_productos[producto_nombre]= cantidad_vendida_productos
    maxima_venta= max(venta_productos.values())
    categoria_maxima= [categoria for categoria,cantidad in venta_productos.items() if cantidad==maxima_venta]
    print(f"Los productos mas vendidos en Claro Colombia por el momento son {','.join(categoria_maxima)} con ventas de {maxima_venta}")

#ventas
def catalogo_venta(datos):
    datos= dict(datos)
    print("¿A que quieres acceder?\n1. Servicios\n2. Productos\n3. Salir")
    opcion= opc()
    while opcion not in [1,2,3]:
        opcion =opc()
        print("Ingresa una opcion valida\n")
    if opcion==1:
        print("Excelente! aqui estan los servicios")
        print("En Claro, entendemos que eres un/a profesional dedicado/a a ofrecer soluciones de alta calidad a tus clientes. Por eso, estamos emocionados de presentarte nuestra amplia gama de productos y servicios diseñados para satisfacer las necesidades de tus clientes y ayudarte a alcanzar tus objetivos de ventas.\n ¿Que categoria quieres revisar?\n1. Hogar\n2. Celulares\n3. Servicios Moviles\n4. Computadores\n5. Streaming\n6. Accesorios Tecnologicos\n7. Seguridad Digital\n8.Salir\n")
        opcion= opc()
        while opcion not in [1,2,3,4,5,6,7,8]:
            opcion =opc()
            print("Ingresa una opcion valida\n")
        for servicio in datos["servicios"]:
            if opcion==1:
                if servicio["categoria"]== "hogar":
                    print (f"""Servicio: {servicio["nombre_serv"]}\nCodigo: {servicio["codigo"]}\nDescripcion: {servicio["descripcion"]}\nPrecio: {servicio["precio"]}\n""")
            elif opcion==2:
                if servicio["categoria"]== "celulares":
                    print (f"""Servicio: {servicio["nombre_serv"]}\nCodigo: {servicio["codigo"]}\nDescripcion: {servicio["descripcion"]}\nPrecio: {servicio["precio"]}\n""")
            elif opcion==3:
                if servicio["categoria"]== "servicios moviles":
                    print (f"""Servicio: {servicio["nombre_serv"]}\nCodigo: {servicio["codigo"]}\nDescripcion: {servicio["descripcion"]}\nPrecio: {servicio["precio"]}\n""") 
            elif opcion==4:
                if servicio["categoria"]== "computadores":
                    print (f"""Servicio: {servicio["nombre_serv"]}\nCodigo: {servicio["codigo"]}\nDescripcion: {servicio["descripcion"]}\nPrecio: {servicio["precio"]}\n""")
            elif opcion==5:
                if servicio["categoria"]== "streaming":
                    print (f"""Servicio: {servicio["nombre_serv"]}\nCodigo: {servicio["codigo"]}\nDescripcion: {servicio["descripcion"]}\nPrecio: {servicio["precio"]}\n""")
            elif opcion==6:
                if servicio["categoria"]== "accesorios tecnologicos":
                    print (f"""Servicio: {servicio["nombre_serv"]}\nCodigo: {servicio["codigo"]}\nDescripcion: {servicio["descripcion"]}\nPrecio: {servicio["precio"]}\n""") 
            elif opcion==7:
                if servicio["categoria"]== "seguridad digital":
                    print (f"""Servicio: {servicio["nombre_serv"]}\nCodigo: {servicio["codigo"]}\nDescripcion: {servicio["descripcion"]}\nPrecio: {servicio["precio"]}\n""")
            else:
                print("Decidiste salir del catalogo de servicios Claro!")
    elif opcion==2: 
        print("Excelente! aqui estan los productos")
        print("En Claro, entendemos que eres un/a profesional dedicado/a a ofrecer soluciones de alta calidad a tus clientes. Por eso, estamos emocionados de presentarte nuestra amplia gama de productos y servicios diseñados para satisfacer las necesidades de tus clientes y ayudarte a alcanzar tus objetivos de ventas.\n ¿Que categoria quieres revisar?\n1. Hogar\n2. Celulares\n3. Servicios Moviles\n4. Computadores\n5. Streaming\n6. Accesorios Tecnologicos\n7. Seguridad Digital\n8.Salir\n")
        opcion= opc()
        while opcion not in [1,2,3,4,5,6,7,8]:
            opcion =opc()
            print("Ingresa una opcion valida\n")
        for producto in datos["productos"]:
            if opcion==1:
                if producto["categoria"]== "hogar":
                    print (f"""Producto: {producto["nombre"]}\nCodigo: {producto["codigo"]}\nMarca: {producto["marca"]}\n\Caracteristicas: {producto["caracteristicas"]}\nPrecio: {producto["precio"]}\nGarantia: {producto["garantia"]}""")

            elif opcion==2:
                if producto["categoria"]== "celulares":
                    print (f"""Producto: {producto["nombre"]}\nCodigo: {producto["codigo"]}\nMarca: {producto["marca"]}\n\Caracteristicas: {producto["caracteristicas"]}\nPrecio: {producto["precio"]}\nGarantia: {producto["garantia"]}""")
            elif opcion==3:
                if producto["categoria"]== "servicios moviles":
                    print (f"""Producto: {producto["nombre"]}\nCodigo: {producto["codigo"]}\nMarca: {producto["marca"]}\n\Caracteristicas: {producto["caracteristicas"]}\nPrecio: {producto["precio"]}\nGarantia: {producto["garantia"]}""")
            elif opcion==4:
                if producto["categoria"]== "computadores":
                    print (f"""Producto: {producto["nombre"]}\nCodigo: {producto["codigo"]}\nMarca: {producto["marca"]}\n\Caracteristicas: {producto["caracteristicas"]}\nPrecio: {producto["precio"]}\nGarantia: {producto["garantia"]}""")
            elif opcion==5:
                if producto["categoria"]== "streaming":
                    print (f"""Producto: {producto["nombre"]}\nCodigo: {producto["codigo"]}\nMarca: {producto["marca"]}\n\Caracteristicas: {producto["caracteristicas"]}\nPrecio: {producto["precio"]}\nGarantia: {producto["garantia"]}""")
            elif opcion==6:
                if producto["categoria"]== "accesorios tecnologicos":
                    print (f"""Producto: {producto["nombre"]}\nCodigo: {producto["codigo"]}\nMarca: {producto["marca"]}\n\Caracteristicas: {producto["caracteristicas"]}\nPrecio: {producto["precio"]}\nGarantia: {producto["garantia"]}""")
            elif opcion==7:
                if producto["categoria"]== "seguridad digital":
                    print (f"""Producto: {producto["nombre"]}\nCodigo: {producto["codigo"]}\nMarca: {producto["marca"]}\n\Caracteristicas: {producto["caracteristicas"]}\nPrecio: {producto["precio"]}\nGarantia: {producto["garantia"]}""")
            else:
                print("Decidiste salir del catalogo de productos Claro!")
    else:
        print("Decidiste salir del catalogo de ventas de Claro!")
    
def registrar_venta(datos):
    datos= dict(datos)
    venta= {}
    encontrado= True
    print("¿Quieres registrar la venta de:\n1. Servicios\n2. Productos\n3. Salir" )
    opcion= opc()
    while not opcion in [1,2,3]:
        print("Opcion invalida!")
        opcion=opc()
    if opcion==1:
        venta["codigo"]= input("Ingresa el codigo del servicio: ")
        for servicio in datos["servicios"]:
            if venta["codigo"]== servicio["codigo"]:
                encontrado= True
                venta["nombre"]= servicio["nombre_serv"]
                print("Nombre del servicio: ", venta["nombre"])
                venta["fecha"]= str(datetime.now())
                print("Fecha de venta: ", venta["fecha"])
                try: 
                    cantidad= int(input("Ingresa la cantidad del servicio vendida: "))
                except Exception:
                    error= "Cantidad invalida!"
                    print(error)
                    registrar_txt(error)
                    break
                venta["cantidad"]= cantidad 
                cantidad_anterior= servicio["cantidad_vendida"]
                total_actual= cantidad_anterior+cantidad
                servicio["cantidad_vendida"]= total_actual
                estado = input("Ingresa el estado de la venta (pagado, deuda): ").lower()
                while estado not in ["pagado", "deuda"]:
                    print("Estado de venta no valido!")
                    estado = input("Ingresa el estado de la venta (pagado, deuda): ").lower()
                venta["estado"]= estado
                datos["ventas"].append(venta)
                print("Venta cargada!\nCierra el programa para cargar correctamente la base de datos")
        if encontrado== False:
            print("No se encontro el codigo del servicio")
        return datos
    elif opcion==2:
        venta["codigo"]= input("Ingresa el codigo del producto: ")
        for producto in datos["productos"]:
            if venta["codigo"]== producto["codigo"]:
                encontrado= True
                venta["nombre"]= producto["nombre"]
                print("Nombre del producto: ", venta["nombre"])
                venta["fecha"]= str(datetime.now())
                print("Fecha de venta: ", venta["fecha"])
                try: 
                    cantidad= int(input("Ingresa la cantidad del producto vendida: "))
                except Exception:
                    error= "Cantidad invalida!"
                    print(error)
                    registrar_txt(error)
                    break
                venta["cantidad"]= str(cantidad)
                cantidad_anterior= producto["cantidad_vendida"]
                total_actual= cantidad_anterior+cantidad
                producto["cantidad_vendida"]= total_actual
                estado = input("Ingresa el estado de la venta (pagado, deuda): ").lower()
                while estado not in ["pagado", "deuda"]:
                    print("Estado de venta no valido!")
                    estado = input("Ingresa el estado de la venta (pagado, deuda): ").lower()
                venta["estado"]= estado
                datos["ventas"].append(venta)
                print("Venta cargada!\nCierra el programa para cargar correctamente la base de datos")
        if encontrado== False:
            print("No se encontro el codigo del producto")
    else:
        print("Decidiste salir del registro de ventas de Claro!")

    return datos

def listar_ventas(datos):
    datos= dict(datos)
    for venta in datos["ventas"]:
        print("Vendido:" + venta["nombre"])
        print("Codigo: " + venta["codigo"])
        print("Cantidad: "+ str(venta['cantidad']))
        print("Fecha: "+ venta["fecha"])
        print("Estado: "+ venta["estado"])
        print("")
    return datos