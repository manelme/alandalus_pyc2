# coding: utf-8

from aula import Aula

class Instituto():
    
    
    def __init__(self, nombre=None, direccion=None, aulas=None):
        self.nombre = nombre
        self.direccion = direccion
        self.aulas = aulas
    
    def clasesOcupadas(self):
        numeroClasesOcupadas = 0
        for aulaIndividual in self.aulas:
            numeroClasesOcupadas = numeroClasesOcupadas+1 if aulaIndividual.getOcupada() else numeroClasesOcupadas
        return numeroClasesOcupadas




