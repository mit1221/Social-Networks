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
        param = {'Jay Pritchett': ['Claire Pritchett', 'Manny Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Claire', 'Jay', 'Manny']}
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
        param = {'Jay Pritchett': ['Claire Pritchett'], 'McDuck Pritchett': \
                 ['Jay Pritchett'], 'Manny Pritchett': ['Cameron Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Cameron', 'Claire', 'Jay', 'Manny', 'McDuck']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
        
    def test_get_families_multiple_people_multiple_friends_diff_families(self):
        param = {'Jay Pritchett': ['Claire Dunphy', 'Chairman D-Cat'], \
                 'Cameron Tucker': ['Jay Pritchett', 'Haley Gwendolyn Dun'], \
                 'Manny Prit': ['Cameron Tucker', 'Manny Delgado']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': \
                    ['Claire'], 'D-Cat': ['Chairman'], \
                    'Tucker': ['Cameron'], 'Dun': ['Haley Gwendolyn'], 'Prit': \
                    ['Manny'], 'Delgado': ['Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    
    def test_get_families_multiple_people_multiple_friends_same_families(self):
        param = {'Jay Pritchett': ['Claire Pritchett', 'Chairman Pritchett'], \
                 'Cameron Pritchett': ['Jay Pritchett', \
                                       'Haley Gwendolyn Pritchett'], \
                 'Manny Pritchett': ['Cameron Pritchett', 'Michael Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Cameron', 'Chairman', 'Claire', \
                                  'Haley Gwendolyn', 'Jay', 'Manny', 'Michael']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    
    def test_get_families_multiple_people_multiple_friends_some_same_families\
        (self):
        param = {'Jay Pritchett': ['Claire Dunphy', 'Chairman Dunphy'], \
                 'Cameron Pritchett': ['Jay Pritchett', \
                                       'Haley Gwendolyn Dunphy'], \
                 'Manny Pritchett': ['Cameron Pritchett', 'Manny Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Cameron', 'Jay', 'Manny'], 'Dunphy': \
                    ['Chairman', 'Claire', 'Haley Gwendolyn', 'Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


if __name__ == '__main__':
    unittest.main(exit=False)