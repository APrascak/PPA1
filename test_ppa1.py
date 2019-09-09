# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak

import unittest
from ppa1 import making_bmi

class TestBMI(unittest.TestCase):

    def test_bmi(self):
        # Makes sure example calculations are correct.
        self.assertEqual(making_bmi(125, 63), 22.7)

    