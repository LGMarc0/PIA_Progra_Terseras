class Calificaciones:
    def __init__(self, id_estudiante, nomb_estudiante, semestre, grupo, carrera, nota1, nota2, nota3, nota4, nota5, promedio=None):
        self.id_estudiante = id_estudiante
        self.nomb_estudiante = nomb_estudiante
        self.semestre = semestre
        self.grupo = grupo
        self.carrera = carrera
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5
        self.promedio = promedio 
        if promedio is None:
            self.promedio = self.calcular_promedio_ajustado()
        else:
            self.promedio = promedio

    def calcular_promedio_ajustado(self):
        notas = [self.nota1, self.nota2, self.nota3, self.nota4, self.nota5]
        notas.remove(min(notas))
        promedio = sum(notas) / len(notas)
        return round(promedio, 2)

    def obtener_mensaje_promedio(self):
        return f"El promedio ajustado del estudiante {self.id_estudiante} es: {self.promedio}"

    def __str__(self):
        return f"ID: {self.id_estudiante}, Nombre: {self.nomb_estudiante}, Promedio: {self.promedio}"


estudiantes = []


def solicitar_nota(prompt):
    valor = float(input(prompt))
    if valor < 0 or valor > 5:
        print("Error: Las notas deben estar entre 0 y 5.")
        return solicitar_nota(prompt)
    return valor


def agregar_estudiante():
    print("\n--- AGREGAR ESTUDIANTE ---")
    id_estudiante = input("Ingrese el código del estudiante: ")
    for est in estudiantes:
        if est.id_estudiante == id_estudiante:
            print("Error: Ya existe un estudiante con ese código.")
            return
    nomb_estudiante = input("Ingrese el nombre del estudiante: ")
    semestre = input("Ingrese el semestre: ")
    grupo = input("Ingrese el grupo: ")
    carrera = input("Ingrese la carrera: ")
    nota1 = solicitar_nota("Ingrese la nota 1 (0-5): ")
    nota2 = solicitar_nota("Ingrese la nota 2 (0-5): ")
    nota3 = solicitar_nota("Ingrese la nota 3 (0-5): ")
    nota4 = solicitar_nota("Ingrese la nota 4 (0-5): ")
    nota5 = solicitar_nota("Ingrese la nota 5 (0-5): ")
    estudiante = Calificaciones(id_estudiante, nomb_estudiante, semestre, grupo,
                               carrera, nota1, nota2, nota3, nota4, nota5)
    estudiantes.append(estudiante)
    print("Estudiante agregado exitosamente.")
    print(estudiante.obtener_mensaje_promedio())


def ver_promedio_estudiante():
    print("\n--- VER PROMEDIO DE ESTUDIANTE ---")
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    id_estudiante = input("Ingrese el código del estudiante: ")
    for est in estudiantes:
        if est.id_estudiante == id_estudiante:
            print(f"Nombre: {est.nomb_estudiante}")
            print(f"Notas: {est.nota1}, {est.nota2}, {est.nota3}, {est.nota4}, {est.nota5}")
            print(est.obtener_mensaje_promedio())
            return
    print("Estudiante no encontrado.")


def ver_todos_los_promedios():
    print("\n--- TODOS LOS PROMEDIOS ---")
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print(f"{'ID':<10} {'Nombre':<20} {'Semestre':<10} {'Grupo':<8} {'Promedio':<10}")
    print("-" * 70)
    for est in estudiantes:
        print(f"{est.id_estudiante:<10} {est.nomb_estudiante:<20} {est.semestre:<10} {est.grupo:<8} {est.promedio:<10}")


def eliminar_estudiante():
    print("\n--- ELIMINAR ESTUDIANTE ---")
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    id_estudiante = input("Ingrese el código del estudiante a eliminar: ")
    for i, est in enumerate(estudiantes):
        if est.id_estudiante == id_estudiante:
            confirmacion = input(f"¿Está seguro de eliminar al estudiante {est.nomb_estudiante}? (s/n): ")
            if confirmacion.lower() == 's':
                estudiantes.pop(i)
                print("Estudiante eliminado exitosamente.")
            return
    print("Estudiante no encontrado.")


def modificar_calificaciones():
    print("\n--- MODIFICAR CALIFICACIONES ---")
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    id_estudiante = input("Ingrese el código del estudiante: ")
    for est in estudiantes:
        if est.id_estudiante == id_estudiante:
            print(f"Notas actuales: {est.nota1}, {est.nota2}, {est.nota3}, {est.nota4}, {est.nota5}")
            est.nota1 = solicitar_nota(f"Nueva nota 1 (actual: {est.nota1}): ")
            est.nota2 = solicitar_nota(f"Nueva nota 2 (actual: {est.nota2}): ")
            est.nota3 = solicitar_nota(f"Nueva nota 3 (actual: {est.nota3}): ")
            est.nota4 = solicitar_nota(f"Nueva nota 4 (actual: {est.nota4}): ")
            est.nota5 = solicitar_nota(f"Nueva nota 5 (actual: {est.nota5}): ")
            est.promedio = est.calcular_promedio_ajustado()
            print("Calificaciones actualizadas exitosamente.")
            print(est.obtener_mensaje_promedio())
            return
    print("Estudiante no encontrado.")


if __name__ == "__main__":
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar un Estudiante")
        print("2. Ver promedio de un Estudiante")
        print("3. Ver todos los promedios de los Estudiantes")
        print("4. Eliminar Estudiante")
        print("5. Modificar calificaciones de un Estudiante")
        print("6. Salir")
        opcion = int(input("Seleccione una opción (1-6): "))
        if opcion == 1:
            agregar_estudiante()
        elif opcion == 2:
            ver_promedio_estudiante()
        elif opcion == 3:
            ver_todos_los_promedios()
        elif opcion == 4:
            eliminar_estudiante()
        elif opcion == 5:
            modificar_calificaciones()
        elif opcion == 6:
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 6.")