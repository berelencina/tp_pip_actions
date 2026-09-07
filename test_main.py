import unittest
from main import obtener_dato

class TestMiCodigo(unittest.TestCase):
    def test_deberia_devolver_algo(self):
        resultado = obtener_dato()
        self.assertIsNotNone(resultado)
        self.assertGreater(len(resultado), 0)

if __name__ == "__main__":
    unittest.main()