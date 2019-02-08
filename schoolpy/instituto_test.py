# coding: utf-8

import unittest
from instituto import Instituto
from aula import Aula

class Instituto_test(unittest.TestCase):
    
    def setUp(self):
        
        aulasA=[]*10
        for i in range(10):
            aulasA.append(Aula('Aula '+ str(i)))   
        self.institutoA = Instituto('Al-Ándalus','Finca Santa Isabel, Paseo de la Caridad, s/n, 04008 Almería',aulasA)

        aulasB=[]*10
        for i in range(10):
            aulasB.append(Aula('Aula '+ str(i), True if i<4 else False))   
        self.institutoB = Instituto('Sol de Portocarrero','Carretera Níjar, Km 7, 04120 Almería',aulasB)

    def test_instituto_name(self):
        self.assertEqual(self.institutoA.nombre, 'Al-Ándalus')
        self.assertNotEqual(self.institutoB.nombre, 'Al-Ándalus')

    def test_instituto_clases_ocupadas(self):
        self.assertEqual(self.institutoA.clasesOcupadas(), 0)
        self.assertEqual(self.institutoB.clasesOcupadas(), 4)

if __name__ == '__main__':
    unittest.main()