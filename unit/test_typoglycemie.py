import unittest
import typoglycemie

class TestRandomizeMethods(unittest.TestCase):
    def test_shortword_01(self):
        self.assertEqual(typoglycemie.typoglycemie("aze"),"aze")


if __name__== '__main__':
    unittest.main()