# coding: utf-8


class Curso():

    def __init__(self, nombre=None, comienzo_de_curso=None, fin_de_curso=None, asignaturas=None, tutor=None):
        self.nombre = nombre
        self.comienzo_de_curso = comienzo_de_curso
        self.fin_de_curso = fin_de_curso
        self.codido_postal = asignaturas
        self.tutor = tutor

    def porcentaje_curso_terminado(self):

        return 0