# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak

import unittest
from ppa1 import split_the_tip

class TestSplitTheTip(unittest.TestCase):

    def test_same_point(self):
        self.assertEqual(split_the_tip(10,10), 0)