class Empleado:
    def __init__(self, departamento, puesto, horas_lab, fechas_ingreso, salario, bono):
        self.departamento = departamento
        self.puesto = puesto
        self.horas_lab = horas_lab
        self.fecha_ingreso = fechas_ingreso
        self.salario = salario
        self.bono = bono

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
   except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
