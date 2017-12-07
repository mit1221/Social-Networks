import unittest
import network_functions

class TestLoadProfiles(unittest.TestCase):

    def test_load_profiles(self):
        profiles = open('profiles.txt')
        p = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], 'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']}
        n = {'Claire Dunphy': ['Parent Teacher Association'], 'Manny Delgado': ['Chess Club'], 'Mitchell Pritchett': ['Law Association'], 'Alex Dunphy': ['Chess Club', 'Orchestra'], 'Cameron Tucker': ['Clown School', 'Wizard of Oz Fan Club'], 'Phil Dunphy': ['Real Estate Association'], 'Gloria Pritchett': ['Parent Teacher Association']}
        ip = {}
        inn = {}
        actual = network_functions.load_profiles(profiles, ip, inn)
        self.assertEqual(ip, p)
        self.assertEqual(inn, n)
        profiles.close()


if __name__ == '__main__':
    unittest.main(exit=False)