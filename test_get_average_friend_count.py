import unittest
import network_functions

class TestGetAverageFriendCount(unittest.TestCase):

    def test_get_average_empty(self):
        param = {}
        actual = network_functions.get_average_friend_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_get_average_one_person_one_friend(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    
    def test_get_average_one_person_two_friend(self):
        param = {'Mit Kapadia': ['Jay Patel', 'John Ventura']}
        actual = network_functions.get_average_friend_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)        
        self.assertEqual(actual, expected, msg)
       
        
    def test_get_average_multiple_people_one_friend(self):
        param = {'Mit Kapadia': ['Jay Patel'], 'John Ventura': \
                 ['Gamila Jonckers']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)        
        self.assertEqual(actual, expected, msg)
    
    
    def test_get_average_multiple_people_multiple_friends(self):
        param = {'Mit Kapadia': ['Alexander Jonckers', 'Jacob Brown', \
                                 'Jay Kapadia', 'John Ventura'], \
                 'John Ventura': ['Gamila Jonckers', 'Rachel Lawerenz']}
        actual = network_functions.get_average_friend_count(param)
        expected = 3.0
        msg = "Expected {}, but returned {}".format(expected, actual)        
        self.assertEqual(actual, expected, msg)    

if __name__ == '__main__':
    unittest.main(exit=False)