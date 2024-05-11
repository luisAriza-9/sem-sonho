from menu import opc, randint
import string

def generar_codigo_unico():
    """Genera un código único para cada cliente."""
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(randint(0, len(caracteres) - 1) for _ in range(10))
    return codigo

def registrar_cliente(datos):
    """Registra la información de un cliente."""
    cliente = {}
    cliente["nombre"] = input("Ingresa el nombre del cliente: ")
    cliente["codigo"] = generar_codigo_unico()
    cliente["email"] = input("Ingresa un email válido del cliente: ")
    
    while True:
        telefono = input("Ingresa el teléfono del cliente (10 dígitos): ")
        if len(telefono) == 10 and telefono.isdigit():
            break
        print("Número de teléfono inválido. Debe tener 10 dígitos.")

    cliente["telefono"] = telefono
    cliente["ciudad"] = input("Ingresa la ciudad donde vive el cliente: ")
    cliente["direccion"] = input("Ingresa la dirección del cliente: ")
    cliente["compras"] = 0
    cliente["adquiridos"] = []
    cliente["publicidad"] = []

    datos["clientes"].append(cliente)
    print("Cliente registrado correctamente. Cierra el programa para ver los cambios.")

    return datos




def eliminar_usuario(datos):
    datos = dict(datos)
    print("🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰")
    usuario = input("Ingresa el código del cliente a eliminar: ")
    
    # Verificar si el código existe en la lista de clientes
    if usuario in (cliente["codigo"] for cliente in datos["clientes"]):
        # Eliminar el cliente
        datos["clientes"] = [cliente for cliente in datos["clientes"] if cliente["codigo"] != usuario]
        print("Usuario eliminado exitosamente.")
    else:
        print("El código de cliente no existe en la lista.")
    
    return datos

def listar_usuarios(datos):
    datos = dict(datos)
    indice = 1
    print("🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰")
    print("Lista de clientes\n")
    for cliente in datos["clientes"]:
        print(f"{indice}. Nombre: {cliente['nombre']} - Código: {cliente['codigo']}\n")
        indice += 1

def actualizar_servicios(datos):
    datos = dict(datos)
    print("🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰")
    codigo_serv = input("Ingresa el código del servicio a cambiar: ")
    for i in range(len(datos["servicios"])):
        if codigo_serv == datos["servicios"][i]["codigo"]:
            while True:
                print("¿Qué datos quieres actualizar?\n1. Nombre\n2. Código\n3. Categoría\n4. Descripción\n5. Precio\n6. Salir")
                opcion = opc()
                while opcion not in [1, 2, 3, 4, 5, 6]:
                    print("Ingresa una opción válida\n")
                    opcion = opc()
                if opcion == 1:
                    datos["servicios"][i]["nombre_serv"] = input("Ingrese el nuevo nombre del servicio: ")
                    print("¡Guardado!")
                elif opcion == 2:
                    codigo_nuevo = datos["servicios"][i]["codigo"] = generar_codigo_unico()
                    print("¡Guardado!")
                    print("El código nuevo del servicio es " + codigo_nuevo)
                elif opcion == 3:
                    datos["servicios"][i]["categoria"] = input("Ingrese la nueva categoría del servicio: ")
                    print("¡Guardado!")
                elif opcion == 4:
                    datos["servicios"][i]["descripcion"] = input("Ingrese la nueva descripción del servicio: ")
                    print("¡Guardado!")
                elif opcion == 5:
                    datos["servicios"][i]["precio"] = input("Ingrese el precio actualizado del servicio: ")
                    print("¡Guardado!")
                else:
                    print("¡Saliste de actualizar servicios!")
                    break
    return datos

def actualizar_clientes(datos):
    """
    Actualiza los datos de los clientes en el diccionario 'datos'.
    """
    while True:
        usuario = input("Ingresa el código del cliente a cambiar (o 'salir' para salir): ")
        if usuario.lower() == "salir":
            break

        # Buscar el cliente por código
        for cliente in datos["clientes"]:
            if cliente["codigo"] == usuario:
                print(f"Cliente encontrado: {cliente['nombre']} ({cliente['codigo']})")
                while True:
                    print("\n¿Qué dato deseas actualizar?")
                    print("1. Nombre")
                    print("2. Email")
                    print("3. Teléfono")
                    print("4. Ciudad")
                    print("5. Dirección")
                    print("6. Salir")
                    opcion = input("Selecciona una opción: ")

                    if opcion == "1":
                        nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
                        cliente["nombre"] = nuevo_nombre
                        print("¡Nombre actualizado!")

                    elif opcion == "2":
                        nuevo_email = input("Ingrese el nuevo email del cliente: ")
                        cliente["email"] = nuevo_email
                        print("¡Email actualizado!")

                    elif opcion == "3":
                        nuevo_telefono = input("Ingrese el nuevo teléfono del cliente: ")
                        while len(nuevo_telefono) != 10:
                            print("Número de teléfono inválido. Debe tener 10 dígitos.")
                            nuevo_telefono = input("Ingrese el nuevo teléfono del cliente: ")
                        cliente["telefono"] = nuevo_telefono
                        print("¡Teléfono actualizado!")

                    elif opcion == "4":
                        nueva_ciudad = input("Ingrese la nueva ciudad del cliente: ")
                        cliente["ciudad"] = nueva_ciudad
                        print("¡Ciudad actualizada!")

                    elif opcion == "5":
                        nueva_direccion = input("Ingrese la nueva dirección del cliente: ")
                        cliente["direccion"] = nueva_direccion
                        print("¡Dirección actualizada!")

                    elif opcion == "6":
                        print("Saliendo de la actualización de datos del cliente.")
                        break

                    else:
                        print("Opción inválida. Inténtalo nuevamente.")

                break
        else:
            print("Cliente no encontrado. Inténtalo nuevamente.")

    return datos


def listar_servicios(datos):
    datos = dict(datos)
    indice = 1
    print("🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰")
    print("Lista de servicios\n")
    for i in range(len(datos["servicios"])):
        print(f"{indice}. Nombre: {datos['servicios'][i]['nombre_serv']} - Código: {datos['servicios'][i]['codigo']}")
        print("")
        indice += 1
        
def eliminar_servicio(datos):
  """
  Elimina un servicio del diccionario de datos proporcionado.

  Args:
    datos (dict): Diccionario que contiene la información de clientes y servicios.

  Returns:
    bool: `True` si se eliminó el servicio, `False` en caso contrario.
  """

  datos = dict(datos)  # Convertir a diccionario mutable

  codigo_servicio = input("Ingrese el código del servicio a eliminar: ")

  servicio_encontrado = False
  for i, servicio in enumerate(datos["servicios"]):
    if servicio["codigo"] == codigo_servicio:
      datos["servicios"].pop(i)
      servicio_encontrado = True
      break

  if servicio_encontrado:
    print("Servicio eliminado!")
    return True
  else:
    print("No se encontró el servicio con el código especificado.")
    return False




def registrar_productos(datos):
  """
  Registra un nuevo producto en el diccionario de datos proporcionado.

  Args:
    datos (dict): Diccionario que contiene la información de productos.

  Returns:
    dict: Diccionario con el producto registrado. Si no se pudo registrar,
          devuelve `None`.
  """

  datos = dict(datos)  # Convertir a diccionario mutable

  producto = {}

  # Solicitar datos del producto
  producto["nombre"] = input("Ingresa el nombre del producto: ")
  producto["codigo"] = generar_codigo_unico(datos["productos"])  # Función para generar código único
  print("El código único del producto es:", producto["codigo"])
  producto["categoria"] = input("Ingresa la categoría del producto: ")
  producto["marca"] = input("Ingresa la marca del producto: ")
  producto["caracteristicas"] = input("Ingresa las características del producto: ")
  producto["garantia"] = input("Ingresa la duración de garantía del producto: ")
  try:
    producto["precio"] = float(input("Ingresa el precio del producto: "))
  except ValueError:
    print("Error: El precio debe ser un número válido.")
    return None

  # Agregar producto a la lista
  datos["productos"].append(producto)

  print("¡Producto registrado!")
  return datos

