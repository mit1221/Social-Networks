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


if __name__ == '__main__':
    unittest.main()