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
    

def ver_todos_empleados():
    

def eliminar_empleado():
    

def modificar_empleado():
    


while True:
    print("\n--- MENÚ ---")
    print("Elige una opcion")
    print("1. Agregar Un Empleado")
    print("2.- Ver info. de un Empleado")
    print("3.- Ver Todos los Empleados")
    print("4.- Eliminar Empleado") 
    print("5.- Modificar info. de un Empleado")
    print("6.- Salir")
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
