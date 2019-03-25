# coding: utf-8

from aula import Aula

class Instituto():
    
    
    def __init__(self, id=None, nombre=None, codigo = None, fax=None, web=None, aulas=None):
        self.id = id
        self.nombre = nombre
        self.codigo = codigo
        self.fax = fax
        self.web = web
        self.aulas = aulas
    
    def clasesOcupadas(self):
        numeroClasesOcupadas = 0
        for aulaIndividual in self.aulas:
            numeroClasesOcupadas = numeroClasesOcupadas+1 if aulaIndividual.getOcupada() else numeroClasesOcupadas
        return numeroClasesOcupadas




