# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak

import unittest
from ppa1 import retirement

class TestBMI(unittest.TestCase):

    def test_retirement_no_death(self):
        self.assertEqual(retirement(30,100000,10,100000), 37.4)

    def test_retirement_death(self):
        self.assertEqual(retirement(40,100000,.5,999999), 100)