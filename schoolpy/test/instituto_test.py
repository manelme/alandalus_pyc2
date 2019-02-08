import unittest
from ..instituto import Instituto

class Instituto_test(unittest.TestCase):
    
    def test_instituto_name(self):
        instituto = Instituto()
        self.assertEqual(instituto.name, "Al-Ándalus")
