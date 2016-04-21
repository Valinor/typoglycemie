import unittest
import typoglycemiet

class TestRandomizeMethods(unittest.TestCase):
    def test_shortword_01(self):
        self.assertEqual(typoglycemiet.typoglycemie("aze"),"aze")


if __name__== '__main__':
    unittest.main()