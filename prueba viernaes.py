fd = open("PRUEBA VIERNES\\ Downloads  \\mbox-short.txt", "r")


contador=0
acomulativo=0
lstEmails = []
for linea in fd:
    if linea.startswith("From:"):
        email = linea.split()[1]
        if email not in lstEmails:
            lstEmails.append(email)

for i in range(len(lstEmails)-1, -1, -1):
    # Enviar el correo
    msj = f"{lstEmails[i]} enviado [ok]"
    print(msj)
    fd2.write(msj+"\n")

# calcule el spam en el servidor de correo


del = ubicacion
import io


cont = 0
for linea in fd:
    if linea.lower().find("from") > -1:
        cont += 1
    
fd.close()

print("Cantidad de lineas que empiezan con From:", cont)
def fname(arg):
    pass
    def leerFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n 
                print("Ingrese los datos.")
                input(" ...")
                continue
            return n
        except ValueError:
            print("Error!. Ingrese una dato válida.")

lstDATOS = []
for est in range(1, 11):
    nota = leerFloat(f"Ingrese nota estudiante #{est}: ")
    lstDATOS.append(nota)
    
notMen = min(lstDATOS)
print("La nota menor es: ", notMen)
notMay = max(lstDATOS)
print("La nota mayor es: ", notMay)

promNotas = sum(lsDATOS / 10
print("El promedio de las notas es: ", promNotas)

# lstDATOS.sort(reverse=True)
# SPAM = lstNotas[0:3]
# SPAM= ""
# for SPAM in  DATOS:
#     strDATOS += str(SPAM) + ", "
    
# print("LA SUMA DE LOS DATOS SON: ", SPAM)



try: 
        fd = open(ruta , "w") # Abre el archivo
    except Exception as e: 
        print("Error al abrir el archivo para guardar el SPAM\n" , e) 
        return NonelstDATOS.sort(reverse=True)
print("La SUAMA DE LOS ESPAM ES: ", ", ".join([f"{SPAM:.2f}" for DATO in lstESPAM[0:3]]))
ef cargarInfo(lstSPAM , ruta): 
    try: 
        fd = open(ruta, "r") #Fd es la apertura del archivo
    except Exception as e:  

        try: 
            fd = open(ruta , "w")  
        except Exception as d:  
            print("Error al intentar abrir el archivo\n" , d) 
            return None 
    try:
        linea = fd.readline()
        if linea.strip() != "": # Si tiene el archivo algo de contenido cargará los datos, sino creará una lista vacia.
            fd.seek(0) # Posiciona el puntero en 0
            lstPersonal = json.load(fd) # json.load() --> carga el archivo
        else: 
            lstPersonal = []
    except Exception as e: 
        print("Error al cargar la informacion\n" , e) 
        return None 
        tx = open("mbox-short.txt", "r")
emails = set()

fd = open("prueba_2.txt", "w")
lst = ["Primera linea\n", "Segunda linea\n"]
fd.writelines(lst)
fd.close()

for i in tx:
    if i.startswith("From: "):
        i = i[6:]
        emails.add(i)

send = list(emails)
for i in range(len(send)-1, 0, -1):
    i = send[i]
    print("Enviado OK\t", i.rstrip())
tx.close