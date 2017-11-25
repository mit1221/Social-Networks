import unittest
import network_functions

class TestGetFamilies(unittest.TestCase):

    def test_get_families_empty(self):
        param = {}
        actual = network_functions.get_families(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_families_one_person_one_friend_diff_family(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_one_person_one_friend_same_family(self):
        param = {'Jay Pritchett': ['Claire Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Claire', 'Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_one_person_multiple_friends_diff_families(self):
        param = {'Jay Pritchett': ['Claire Dunphy', 'Manny Delgado']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire'], 'Delgado': \
                    ['Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_one_person_multiple_friends_same_families(self):
        param = {'Jay Pritchett': ['Claire Pritchett', 'Manny Delgado']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Claire', 'Jay'], 'Delgado': ['Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_multiple_people_one_friend_diff_families(self):
        param = {'Jay Pritchett': ['Claire Dunphy'], 'Manny Delgado': \
                 ['Jay Pritchett'], 'McDuck Scrooge': ['Cameron Tucker']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire'], 'Delgado': \
                    ['Manny'], 'Scrooge': ['McDuck'], 'Tucker': ['Cameron']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_multiple_people_one_friend_same_families(self):
        param = {'Jay Pritchett': ['Claire Dunphy'], 'McDuck Pritchett': \
                 ['Jay Pritchett'], 'Manny Pritchett': ['Cameron Tucker']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay', 'Manny', 'McDuck'], 'Dunphy': \
                    ['Claire'], 'Tucker': ['Cameron']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


if __name__ == '__main__':
    unittest.main(exit=False)