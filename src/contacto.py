# coding: utf-8


class Contacto():

    def __init__(self, localidad=None, provincia=None, direccion=None, codigo_postal=None, telefono=None):
        self.localidad = localidad
        self.provincia = provincia
        self.direccion = direccion
        self.codido_postal = codigo_postal
        self.telefono = telefono
    
    def getFullContactInfo(self):
        return self.direccion + " - Localidad: " + self.localidad + " "+ self.codido_postal+ " - Provincia: "+ self.provincia+" - Teléfono: "+self.telefono