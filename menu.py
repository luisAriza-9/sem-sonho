class Venta:
    def __init__(self, producto, cantidad, fecha):
        self.producto = producto
        self.cantidad = cantidad
        self.fecha = fecha

# Registrar una venta
venta1 = Venta(producto="Internet Fibra Óptica", cantidad=3, fecha="2024-05-09")
lista_ventas = [venta1]

# Consultar ventas por producto o fecha
def buscar_ventas(producto=None, fecha=None):
    resultados = []
    for venta in lista_ventas:
        if (not producto or venta.producto == producto) and (not fecha or venta.fecha == fecha):
            resultados.append(venta)
    return resultados

# Ejemplo de uso
ventas_hoy = buscar_ventas(fecha="2024-05-09")
for venta in ventas_hoy:
    print(f"Venta de {venta.cantidad} unidades de {venta.producto} el {venta.fecha}.")



class Servicio:
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

# Crear un servicio
servicio1 = Servicio(nombre="Internet Fibra Óptica", tipo="Internet", precio=50)

# Agregar más servicios a una lista
lista_servicios = [servicio1]

# Consultar un servicio por nombre
def buscar_servicio(nombre):
    for servicio in lista_servicios:
        if servicio.nombre == nombre:
            return servicio
    return None

# Modificar un servicio existente
def modificar_servicio(nombre, nuevo_precio):
    servicio = buscar_servicio(nombre)
    if servicio:
        servicio.precio = nuevo_precio
        print(f"El precio del servicio {nombre} se ha actualizado a {nuevo_precio}.")

# Eliminar un servicio
def eliminar_servicio(nombre):
    servicio = buscar_servicio(nombre)
    if servicio:
        lista_servicios.remove(servicio)
        print(f"El servicio {nombre} ha sido eliminado.")

# Ejemplo de uso
modificar_servicio("Internet Fibra Óptica", 55)
eliminar_servicio("Servicio X")

