#validar legajo numero entero
import csv, os

CAMPOS = ["Legajo", "Apellido", "Nombre"]

def main(campos):
    print("----------SISTEMA DE VIÁTICOS----------")

    while True:
        print("\nElija una opcion:\n\t1. Ingresar Legajo\n\t2. Ver gastos y datos de un empleado\n\t3. Salir")

        opcion = input("")

        if opcion == "3":
            exit()
        elif opcion == "1":
            cargar_datos(campos)
        elif opcion == "2":
            informar_gastos(campos)
        else:
            print("Opcion inválida. Intente nuevamente.")

def cargar_datos(campos):

    nombre_archivo = input("\nIngrese el nombre del archivo: ")

    lista_empleados = ingresar_empleado(campos)

    try:
        existe_archivo = os.path.isfile(nombre_archivo)
        
        if existe_archivo:
            sobreescribir = input(f"\n El archivo {nombre_archivo} existe. Desea sobreescribir? si/no: ")

            if sobreescribir == "si":
                modo_archivo = "w"
            else:
                modo_archivo = "a"

            with open(nombre_archivo, modo_archivo, newline="") as file:
                planilla = csv.writer(file)
                if modo_archivo == "w":
                    planilla.writerow(campos)
                planilla.writerows(lista_empleados)
                print(f"\nEl archivo {nombre_archivo} se guardó correctamente.")
        else:
            with open(nombre_archivo, "w", newline="") as file:
                planilla = csv.writer(file)
                planilla.writerow(campos)
                planilla.writerows(lista_empleados)
                print(f"\nEl archivo {nombre_archivo} se guardó correctamente.")

    except IOError:
        print("\nOcurrió un error con el archivo.")

#Funcion para ingresar empleado, utilizada en la opcion 1. Ingresar Legajo
def ingresar_empleado(campos):

    print("\n----------INGRESO DE LEGAJO----------\n")

    lista_empleados = []

    salir = ""

    while salir != "si":

        empleado = []

        for campo in campos:
            if campo == "Legajo":
                numero_legajo = validar_entero(campos[0])
                empleado.append(numero_legajo)
            else:
                empleado.append(input(f"Ingrese el {campo} del empleado: "))
        lista_empleados.append(empleado)
    
        salir = input("Desea salir de la carga de empleados? si/no: ")
    
    return lista_empleados

#Funcion para validar
def validar_entero(campo):

    numero_entero = False

    while not numero_entero:
        try:
            numero_legajo = int(input(f"Ingrese el número de {campo} del empleado: "))
            numero_entero = True
        except:
            print("Debe ingresar un número entero. Intente nuevamente.")

    return numero_legajo

#LOGICA PRINCIPAL OPCION 2. Ver gastos y datos del empleado
def informar_gastos(campos):
    print("\n----------INFORME DE GASTOS----------\n")

    numero_legajo = validar_entero(campos[0])
    
    nombre_archivo_legajos = input("Ingrese el nombre del archivo de Legajos: ")

    nombre_archivo_viaticos = input("Ingrese el nombre del archivo de Viáticos: ")

    presupuesto = 5000
    empleado = []
    gastos = 0
    gasto_linea = 0

    try:
        with open(nombre_archivo_viaticos, "r", newline="") as file_viatico:

            planilla_viaticos = csv.reader(file_viatico)
            next(planilla_viaticos)

            for linea in planilla_viaticos:
                if int(linea[0]) == numero_legajo:
                    gastos = gastos + int(linea[1]) # ACUMULO LOS GASTOS

        with open(nombre_archivo_legajos, "r", newline="") as file_legajos:

            planilla_legajos = csv.reader(file_legajos)
            next(planilla_legajos)

            for legajo in planilla_legajos:
                if int(legajo[0]) == numero_legajo:
                    empleado = legajo # GUARDO DATOS DEL EMPLEADO PARA LUEGO INFORMARLOS

        if gastos > presupuesto:
            print(f"\nLegajo {empleado[0]} : {empleado[2]} {empleado[1]}, gastó ${gastos} y se ha pasado del presupuesto por ${gastos - presupuesto}")
        else:
            print(f"\nLegajo {empleado[0]} : {empleado[2]} {empleado[1]}, gastó ${gastos}")
    except IOError:
        print("\nOcurrió un error con el archivo. Revise los nombres del archivos ingresados antes de continuar.")

main(CAMPOS)
