import datetime

class Empleado:
    def __init__(self, id_Empleado, Nom_Empleado, departamento, puesto, horas_lab, fechas_ingreso, salario, bono):
        self.id_Empleado = id_Empleado
        self.Nom_Empleado = Nom_Empleado
        self.departamento = departamento
        self.puesto = puesto
        self.horas_lab = horas_lab
        self.fecha_ingreso = fechas_ingreso
        self.salario = salario
        self.bono = bono

    def __str__(self):
        fecha_str = self.fecha_ingreso.strftime("%d/%m/%Y")
        return (f"ID: {self.id_Empleado}, Nombre: {self.Nom_Empleado}, Departamento: {self.departamento}, "
                f"Puesto: {self.puesto}, Horas: {self.horas_lab}, Fecha Ingreso: {fecha_str}, "
                f"Salario: ${self.salario}, Bono: ${self.bono}")

empleados = []

def pedir_fecha(prompt):
    while True:
        texto = input(prompt).strip()
        try:
            return datetime.datetime.strptime(texto, "%d/%m/%Y").date()
        except ValueError:
            print("Formato inválido. Use DD/MM/AAAA.")
    

def agregar_empleado():
    print("\n--- AGREGAR EMPLEADO ---")
    try:
        id_emp = int(input("ID del empleado: "))
        for emp in empleados:
            if emp.id_Empleado == id_emp:
                print("Error: Ya existe un empleado con ese ID.")
                return
        nombre = input("Nombre del empleado: ")
        departamento = input("Departamento: ")
        puesto = input("Puesto: ")
        horas = float(input("Horas laborales(A la semana): "))
        fecha = pedir_fecha("Fecha de ingreso (DD/MM/AAAA): ")
        salario = float(input("Salario(Mensual): "))
        bono = float(input("Bono(Semanal): "))
        empleados.append(Empleado(id_emp, nombre, departamento, puesto, horas, fecha, salario, bono))
        print("Empleado agregado exitosamente.")
    except ValueError:
        print("Error: Por favor ingrese valores válidos.")

def ver_empleado():
    print("\n--- VER INFORMACIÓN DE EMPLEADO ---")
    if not empleados:
        print("No hay empleados registrados.")
        return
    try:
        id_buscar = int(input("Ingrese el ID del empleado a buscar: "))
        for emp in empleados:
            if emp.id_Empleado == id_buscar:
                print("\nInformación del empleado:")
                print(emp)
                return
        print("Empleado no encontrado.")
    except ValueError:
        print("Error: Por favor ingrese un ID válido.")

def ver_todos_empleados():
    print("\n--- TODOS LOS EMPLEADOS ---")
    if not empleados:
        print("No hay empleados registrados.")
        return
    for i, emp in enumerate(empleados, 1):
        print(f"{i}. {emp}")

def eliminar_empleado():
    print("\n--- ELIMINAR EMPLEADO ---")
    if not empleados:
        print("No hay empleados registrados.")
        return
    try:
        id_eliminar = int(input("Ingrese el ID del empleado a eliminar: "))
        for i, emp in enumerate(empleados):
            if emp.id_Empleado == id_eliminar:
                empleados.pop(i)
                print("Empleado eliminado exitosamente.")
                return
        print("Empleado no encontrado.")
    except ValueError:
        print("Error: Por favor ingrese un ID válido.")

def modificar_empleado():
    print("\n--- MODIFICAR EMPLEADO ---")
    if not empleados:
        print("No hay empleados registrados.")
        return
    try:
        id_mod = int(input("Ingrese el ID del empleado a modificar: "))
        for emp in empleados:
            if emp.id_Empleado == id_mod:
                print(f"Empleado encontrado: {emp.Nom_Empleado}")
                print("Deje en blanco para mantener el valor actual.")
                nuevo_nombre = input(f"Nombre ({emp.Nom_Empleado}): ").strip()
                if nuevo_nombre:
                    emp.Nom_Empleado = nuevo_nombre
                nuevo_depto = input(f"Departamento ({emp.departamento}): ").strip()
                if nuevo_depto:
                    emp.departamento = nuevo_depto
                nuevo_puesto = input(f"Puesto ({emp.puesto}): ").strip()
                if nuevo_puesto:
                    emp.puesto = nuevo_puesto
                nuevas_horas = input(f"Horas laborales ({emp.horas_lab}): ").strip()
                if nuevas_horas:
                    emp.horas_lab = float(nuevas_horas)
                fecha_texto = input(f"Fecha de ingreso ({emp.fecha_ingreso.strftime('%d/%m/%Y')}): ").strip()
                if fecha_texto:
                    try:
                        emp.fecha_ingreso = datetime.datetime.strptime(fecha_texto, "%d/%m/%Y").date()
                    except ValueError:
                        print("Fecha no modificada: formato inválido.")
                nuevo_salario = input(f"Salario ({emp.salario}): ").strip()
                if nuevo_salario:
                    emp.salario = float(nuevo_salario)
                nuevo_bono = input(f"Bono ({emp.bono}): ").strip()
                if nuevo_bono:
                    emp.bono = float(nuevo_bono)
                print("Empleado modificado exitosamente.")
                return
        print("Empleado no encontrado.")
    except ValueError:
        print("Error: Por favor ingrese valores válidos.")
    


while True:
    print("\n--- MENÚ ---")
    print("1. Agregar un Empleado")
    print("2. Ver info. de un Empleado")
    print("3. Ver Todos los Empleados")
    print("4. Eliminar Empleado")
    print("5. Modificar info. de un Empleado")
    print("6. Salir")
    try:
        opcion = int(input("¿Qué opción desea elegir? "))
        if opcion == 1:
            agregar_empleado()
        elif opcion == 2:
            ver_empleado()
        elif opcion == 3:
            ver_todos_empleados()
        elif opcion == 4:
            eliminar_empleado()
        elif opcion == 5:
            modificar_empleado()
        elif opcion == 6:
            print("¡Gracias por usar el sistema de gestión de empleados!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 6.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
