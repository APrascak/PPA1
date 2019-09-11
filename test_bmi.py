# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak

import unittest
from ppa1 import bmi

class TestBMI(unittest.TestCase):

    def test_bmi(self):
        # Makes sure example calculations are correct.
        self.assertEqual(bmi(125, 63), 22.7)

    def test_negative_bmi(self):
        self.assertEqual(bmi(125,-5), 0)
