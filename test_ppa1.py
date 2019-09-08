# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak

import unittest
from ppa1 import making_bmi

class TestBMI(unittest.TestCase):
    def test_bmi(self):
        # Test to make sure equals true
        self.assertTrue(making_bmi(5,4))
        self.assertFalse(making_bmi(3,4))