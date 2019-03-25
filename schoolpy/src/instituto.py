# coding: utf-8

from aula import Aula

class Instituto():
    
    
    def __init__(self, nombre=None, direccion=None, telefono = None, codigo = None, codigoPostal=None, fax=None, email=None, web=None, aulas=None):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.codigo = codigo
        self.codigoPostal = codigoPostal
        self.fax = fax
        self.email = email
        self.web = web
        self.aulas = aulas
    
    def clasesOcupadas(self):
        numeroClasesOcupadas = 0
        for aulaIndividual in self.aulas:
            numeroClasesOcupadas = numeroClasesOcupadas+1 if aulaIndividual.getOcupada() else numeroClasesOcupadas
        return numeroClasesOcupadas




