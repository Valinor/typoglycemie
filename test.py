# test_typoglycemie.py

import random
import re
import unittest

# On importe le module que l’on veut tester.
# Typiquement, si test_typoglycemie.py est dans le même dossier que typoglycemie.py :
import typoglycemie

class TestTypoglycemieModule(unittest.TestCase):
    def setUp(self):
        # Pour que la partie aléatoire soit reproductible à chaque test
        random.seed(0)

    def test_mot_trop_court(self):
        """
        Les mots de longueur < 4 ne doivent pas être modifiés.
        Exemple : 'un', 'deux', 'six'.
        """
        entrée = "un deux six"
        sortie = typoglycemie.typoglycemie(entrée)
        self.assertEqual(sortie, "un deux six",
                         msg=f"«{entrée}» → «{sortie}» (les mots <4 ne doivent pas changer)")

    def test_mot_exactement_4(self):
        """
        Les mots de longueur 4 (ex. "test", "four") doivent être mélangés,
        la première et la dernière lettre restent identiques.
        """
        entrée = "test four cinq"
        sortie = typoglycemie.typoglycemie(entrée)

        # «test» devient par exemple «tset» : t en 1ère et 4ᵉ position inchangés.
        # On vérifie que le premier et le dernier caractère sont toujours 't'.
        mot_test = sortie.split()[0]
        self.assertEqual(mot_test[0], 't', msg=f"1ᵉᵉ lettre de «test» modifiée inopinément : {mot_test}")
        self.assertEqual(mot_test[-1], 't', msg=f"Lettre finale de «test» modifiée : {mot_test}")

        # Vérifions aussi «four» (premier f, dernier r)
        mot_four = sortie.split()[1]
        self.assertEqual(mot_four[0], 'f', msg=f"1ᵉᵉ lettre de «four» modifiée : {mot_four}")
        self.assertEqual(mot_four[-1], 'r', msg=f"Dernière lettre de «four» modifiée : {mot_four}")

    def test_ponctuation_preservee(self):
        """
        On s'assure que la ponctuation reste à sa place et n'est pas perdue.
        """
        entrée = 'Hello, world! Test.'
        sortie = typoglycemie.typoglycemie(entrée)
        # On vérifie que la virgule, le point d'exclamation et le point final sont toujours là
        # et que chaque mot de ≥4 lettres a ses lettres intérieures mélangées.
        # Exemple de regex permissive : H\w*o,␣w\w*d!␣T\w*t\.
        pattern = r'^H\w*o,\s+w\w*d!\s+T\w*t\.$'
        self.assertRegex(sortie, pattern,
                         msg=f"La sortie «{sortie}» ne correspond pas au pattern attendu {pattern}")

    def test_espaces_multiples(self):
        """
        Si la phrase possède plusieurs espaces consécutifs, ils restent intacts.
        """
        entrée = "She  said,   \"Hi!\""
        sortie = typoglycemie.typoglycemie(entrée)

        # Vérifier que les deux premiers espaces après "She" sont toujours là
        # «She» occupe 3 caractères ⇒ on vérifie sortie[3:5] == "  "
        self.assertEqual(sortie[3:5], "  ",
                         msg=f"Les deux espaces après 'She' ont disparu ou changé dans «{sortie}»")

        # Vérifier que la virgule après "said" est bien à la bonne position
        # Dans l’entrée, "said," est de 5 caractères (s a i d ,) ⇒ on s'attend à ce que
        # ce ',' soit à l’index 3+2+4 = 9 (3 pour 'She', 2 pour "  ", 4 pour "said")
        self.assertEqual(sortie[3+2+4], ",",
                         msg=f"La virgule après 'said' a bougé ou disparu : «{sortie}»")

    def test_chaine_vide_et_mots_courts(self):
        """
        Chaîne vide, mot d'un seul caractère, mots de deux ou trois caractères ne bougent pas.
        """
        self.assertEqual(typoglycemie.typoglycemie(""), "")
        self.assertEqual(typoglycemie.typoglycemie("A"), "A")
        self.assertEqual(typoglycemie.typoglycemie("!"), "!")
        self.assertEqual(typoglycemie.typoglycemie("un oui ? et"), "un oui ? et")

    def test_unicode_et_accents(self):
        """
        Vérifie que les accents ne sont pas perdus et que l’apostrophe est préservée.
        """
        entrée = "L'école d'élève est fermée."
        sortie = typoglycemie.typoglycemie(entrée)

        # 1) L’apostrophe ne doit pas disparaître
        self.assertIn("'", sortie, msg=f"Apostrophe perdue dans «{sortie}»")

        # 2) Le mot "école" (longueur ≥4) doit garder son 'é' en 1ʳᵉ et 'e' en dernière position
        #    On recherche un pattern «é…e» quelque part, éventuellement mélangé à l’intérieur,
        #    mais avec «é» en début et «e» en fin, sans ôter l’accent.
        self.assertRegex(sortie, r"é\w*e",
                         msg=f"Le mot «école» n’a pas préservé ses extrémités accentuées dans «{sortie}»")

    def test_change_number_influence(self):
        """
        Vérifie que la valeur de change_number influe sur l'intensité du mélange.
        """
        random.seed(1)
        mot = "permutation"
        # Mélange avec 10 permutations
        peu_melange = typoglycemie.randomize(mot, change_number=10)

        random.seed(1)
        # Mélange avec 1000 permutations
        beaucoup_melange = typoglycemie.randomize(mot, change_number=1000)

        self.assertNotEqual(peu_melange, beaucoup_melange,
                            msg=f"Résultat identique pour 10 et 1000 permutations : {peu_melange}")

if __name__ == "__main__":
    unittest.main()
