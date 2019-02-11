# coding: utf-8

class Aula():
    
    def __init__(self, nombre=None, ocupada=False):
        self.nombre = nombre
        self.ocupada = ocupada
    
    def ocuparClase(self):
        self.ocupada = True
    
    def desocuparClase(self):
        self.ocupada = False
    
    def getOcupada(self):
        return self.ocupada