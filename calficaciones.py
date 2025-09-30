class calificaciones:
    def __init__(self, id_estudiante, nomb_estudiante, semestre, grupo, carrera, nota1, nota2, nota3, nota4, nota5, promedio):
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
        
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar un Estudiante")
    print("2. Ver promedio de un Estudiante")
    print("3. Ver todos los promedios de los Estudiantes")
    print("4. Eliminar Estudiante")
    print("5. Modificar calificaciones de un Estudiante")
    print("6. Salir")