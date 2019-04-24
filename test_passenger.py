import unittest

from passenger import Passenger


class TestPassener(unittest.TestCase):

    def test_get_name_male(self):
        male = Passenger('Tom', 'male')
        self.assertEqual('Mr Tom', male.get_name())