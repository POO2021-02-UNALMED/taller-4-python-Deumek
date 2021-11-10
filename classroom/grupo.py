from classroom.asignatura import Asignatura

class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        if self._asignaturas == None:
            self._asignaturas = []
        if self.listadoAlumnos == None:
            self.listadoAlumnos = []

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            self.listadoAlumnos += [alumno]
        else:
            self.listadoAlumnos += lista + [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
