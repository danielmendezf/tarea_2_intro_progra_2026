# Autores: Trinidad González (22.141.114-5) - Daniel Méndez (17.673.909-6)

# Listas paralelas
nombres = []
ruts = []
fechas = []
origenes = []
destinos = []
asientos = []
pagos = []


# Función para registrar reserva
def registrar_reserva():
    print("\n--- REGISTRAR RESERVA ---")

    nombre = input("Ingrese nombre completo: ")
    rut = input("Ingrese rut: ")
    fecha = input("Ingrese fecha de viaje: ")

    origen = input("Ciudad origen: ")
    destino = input("Ciudad destino: ")

    # Validar que origen y destino sean distintos
    while origen.lower() == destino.lower():
        print("Origen y destino no pueden ser iguales")
        destino = input("Ingrese otra ciudad destino: ")

    tipo = input("Tipo de asiento (Semi-cama / Salón-cama): ")
    # Conjunto de valores permitidos
    permitidos = ["Semi-cama", "Salón-cama"]

    # Validaciones
    while tipo not in permitidos:
        print("Error: Tipo de asiento no válido. ")
        print("Debe ser 'Semi-cama' o 'Salón-cama'.")
        tipo = input("Tipo de asiento (Semi-cama / Salón-cama): ")

    # Determinar pago según asiento
    if tipo.lower() == "semi-cama":
        pago = 10000
    else:
        pago = 18000

    # Guardar datos
    nombres.append(nombre)
    ruts.append(rut)
    fechas.append(fecha)
    origenes.append(origen)
    destinos.append(destino)
    asientos.append(tipo)
    pagos.append(pago)

    print("Reserva registrada correctamente")
    print()


# Función para mostrar reservas
def listar_reservas():

    print("\n--- LISTADO DE RESERVAS ---")

    for i in range(len(nombres)):
        print("\nReserva", i + 1)
        print("Nombre:", nombres[i])
        print("Rut:", ruts[i])
        print("Fecha:", fechas[i])
        print("Origen:", origenes[i])
        print("Destino:", destinos[i])
        print("Asiento:", asientos[i])
        print("Pago:", pagos[i])


# Función para mostrar ingresos
def total_ingresos():

    print("\n--- TOTAL INGRESOS ---")

    total = sum(pagos)

    print("Total ingresos: $", total)
    print()


# Menú principal
opcion = 0

while opcion != 4:

    print("\n--- MENÚ ---")
    print("1. Registrar reservas")
    print("2. Listar reservas")
    print("3. Mostrar total de ingresos")
    print("4. Salir")

    opcion = int(input("Ingrese opción: "))
    if opcion == 1:
        registrar_reserva()

    elif opcion == 2:
        listar_reservas()

    elif opcion == 3:
        total_ingresos()

    elif opcion == 4:
        print("\nPrograma finalizado")
    else:
        print("\nOpción inválida")
