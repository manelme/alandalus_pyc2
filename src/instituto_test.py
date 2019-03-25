# coding: utf-8

import unittest
from instituto import Instituto
from curso import Curso
from contacto import Contacto

class Instituto_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando test de la clase Instituto")
        
        self.contactoA = Contacto("Almería", "Almería", "Finca Santa Isabel, Paseo de la Caridad, s/n", "04008", "950156936")
        self.contactoB = Contacto("La Cañada","Almería", "Carretera Níjar, Km 7", "04120", "950156950")
        self.cursosA = [Curso()]
        self.cursosB = [Curso()]

        self.institutoNone = Instituto('10000','Al-Ándalus','001','666666666', 'http://alandalus.com')
        self.institutoA = Instituto('9999','Al-Ándalus','001','666666666', 'http://alandalus.com', self.contactoA, self.cursosA)
        self.institutoB = Instituto('9998','Sol de Portocarrero','002','666666667', 'http://soldeportocarrero.com', self.contactoB, self.cursosB)
        
    def test_instituto_name(self):
        self.assertEqual(self.institutoA.nombre, 'Al-Ándalus')
        self.assertNotEqual(self.institutoB.nombre, 'Al-Ándalus')

    def test_direccion_textual(self):
        self.assertEqual(self.institutoA.direccion_textual(), "El centro Al-Ándalus está ubicado en Finca Santa Isabel, Paseo de la Caridad, s/n - Localidad: Almería 04008 - Provincia: Almería - Teléfono: 950156936. La página web del centro es http://alandalus.com. Fax - 666666666")

if __name__ == '__main__':
    unittest.main()