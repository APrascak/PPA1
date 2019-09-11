# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak

import unittest
from ppa1 import split_the_tip

class TestSplitTheTip(unittest.TestCase):

    def test_calculate_tip(self):
        self.assertEqual(split_the_tip(55,4)[0], 63.25)
        self.assertEqual(split_the_tip(55,4)[4], 15.82)