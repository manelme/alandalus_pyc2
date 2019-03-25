import unittest
from contacto import Contacto

class Contacto_test(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando test de la clase Instituto")
        
        self.contactoA = Contacto("Almería", "Almería", "Finca Santa Isabel, Paseo de la Caridad, s/n", "04008", "950156936")
        self.contactoB = Contacto("La Cañada","Almería", "Carretera Níjar, Km 7", "04120", "950156950")

    def test_getFullContactInfo(self):

        self.assertEqual(self.contactoA.getFullContactInfo(), "Finca Santa Isabel, Paseo de la Caridad, s/n - Localidad: Almería 04008 - Provincia: Almería - Teléfono: 950156936")


if __name__ == '__main__':
    unittest.main()