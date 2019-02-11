# coding: utf-8

class Persona():
    
    def __init__(self, nombre=None, apellidos=None):
        self.nombre = nombre
        self.apellidos = apellidos

    def toString(self):
        return self.nombre + " " + self.apellidos