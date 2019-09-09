# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak

import unittest
from ppa1 import email_verifier

class TestShortestDistance(unittest.TestCase):

    def test_period_first(self):
        self.assertEqual(email_verifier(".alexprascak@gmail.com"), False)

    def test_no_period(self):
        self.assertEqual(email_verifier("alexprascak@gmail.com"), True)