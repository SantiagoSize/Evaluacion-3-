viviendas_arrendadas = []
viviendas_publicadas = []

def solicitar_RUT():
    RUT = input("Ingrese su RUT (No usar guiones ni puntos): ")
    RUT = RUT.replace(".", "").replace("-", "")
    if RUT.endswith("K"):
        RUT = RUT[:-1] + "0"
    print(f"RUT creado: {RUT}")
    return RUT

def crear_contraseña():
    intentos = 3
    while intentos > 0:
        contraseña = input("Cree una contraseña de 8 caracteres utilizando únicamente números: ")
        caracteres = sum(1 for c in contraseña)  
        if caracteres != 8:
            intentos -= 1
            print(f"error, la contraseña no tiene 8 caracteres. (Te quedan {intentos} intentos)")
            continue
        if not contraseña.isdigit():
            intentos -= 1
            print(f"error, la contraseña solo permite caracteres de tipo numérico. (Te quedan {intentos} intentos)")
            continue
        print(f"Contraseña creada: {contraseña}")
        return contraseña
    print("Fallaste tus 3 intentos, el programa se cerrara.")
    return None

def mostrar_reglas():
    print("\nReglas del arriendo")
    reglas = """
    -Tener registro de las últimas tres liquidaciones de sueldo.
    -Pagar con un mes de anticipacion.
    -En caso de atraso de paga tienen una semana para desalojar.
    -Después de la 1 am ya no pueden haber ruidos fuertes y en caso de reclamos por ruidos deberá pagar una multa de 50.000.
    -En caso de daños a la infraestructura lo deberá de pagar el arrendatario.
    -En caso de reclamos excesivos se les dará a los culpables un mes para desalojar.
    -En los gastos comunes solo se cubre luz y agua, gastos como gas e internet los debe pagar el arrendatario.
    -En caso de pérdida de las llaves se le cobrará una nueva más el cambio de ranura.
    """
    print(reglas)

def solicitar_continuacion():
    while True:
        print("\n¿Desea continuar con el arriendo?")
        print("1. Sí")
        print("2. No")
        opcion = input("Seleccione una opcion (1/2): ").strip().lower()
        
        if opcion == "1":
            return True
        elif opcion == "2":
            return False
        
def solicitar_informacion_arriendo():
    personas = input("3. Cuantas personas seran en el lugar?: ")
    mascotas = input("4. Tienen mascotas? (Si/No): ")
    presupuesto = input("5. Cuanto dinero tienen para el arriendo?: ")
    return personas, mascotas, presupuesto

def solicitar_liquidaciones():
    liquidaciones = []
    for x in range(1, 4):
        liquidacion = input(f"Ingrese su sueldo #{x} de los últimos 3 meses: ")
        liquidaciones.append(liquidacion)
    return liquidaciones

def mostrar_informacion_arriendo(personas, mascotas, presupuesto, liquidaciones):
    print("\nInformacion del arriendo:")
    print(f"Numero de personas: {personas}")
    print(f"Tienen mascotas?: {mascotas}")
    print(f"Presupuesto: {presupuesto}")
    print(f"Sueldo de los últimos tres meses: {', '.join(liquidaciones)}")