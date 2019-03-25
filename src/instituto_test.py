# coding: utf-8

import unittest
from instituto import Instituto
from flask import Flask, g

import shelve




app = Flask(__name__)


def get_db():
    with app.app_context():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = shelve.open("test_data/hs.db")
        return db


class Instituto_test(unittest.TestCase):
    
    def setUp(self):
        self.institutoA = Instituto('9999','Al-Ándalus','001',666666666, 'http://alandalus.com')
        self.institutoB = Instituto('9998','Sol de Portocarrero','002',666666667, 'http://soldeportocarrero.com')

        shelf = get_db()
        shelf[self.institutoA.id] = self.institutoA
        shelf[self.institutoB.id] = self.institutoB
        
    def test_instituto_name(self):
        self.assertEqual(self.institutoA.nombre, 'Al-Ándalus')
        self.assertNotEqual(self.institutoB.nombre, 'Al-Ándalus')
    
    def tearDown(self):
        shelf = get_db()
        del shelf[self.institutoA.id]
        del shelf[self.institutoB.id]
        with app.app_context():
            db = getattr(g, '_database', None)
            if db is not None:
                db.close()


if __name__ == '__main__':
    unittest.main()