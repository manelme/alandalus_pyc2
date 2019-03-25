# coding: utf-8

from curso import Curso
from contacto import Contacto

class Instituto():
    
    
    def __init__(self, id=None, nombre=None, codigo = None, fax=None, web=None, info_contacto=None, cursos=None):
        self.id = id
        self.nombre = nombre
        self.codigo = codigo
        self.fax = fax
        self.web = web
        self.info_contacto = info_contacto
        self.cursos = cursos
        
        if not isinstance(self.info_contacto, Contacto) and not isinstance(self.info_contacto, type(None)):
            raise TypeError('info_contacto no es de tipo Contacto')
        if not isinstance(self.cursos, list) and not isinstance(self.cursos, type(None)):
            raise TypeError('cursos, no es una lista de cursos')
            for curso in self.cursos:
                if not isinstance(curso, Curso) and not isinstance(curso, type(None)):
                    raise TypeError('cursos no contiene una lista de cursos.')
    
    def direccion_textual(self):
        return "El centro "+self.nombre+" está ubicado en "+self.info_contacto.getFullContactInfo() + ". La página web del centro es "+ self.web+". Fax - "+self.fax 




