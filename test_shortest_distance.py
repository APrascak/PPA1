# PPA1 - CIS4930 - Fall 2019
# Alexander Prascak

import unittest
from ppa1 import shortest_distance

class TestShortestDistance(unittest.TestCase):

    def test_same_point(self):
        self.assertEqual(shortest_distance(10,10,10,10), 0)

    def test_same_line(self):
        self.assertEqual(shortest_distance(10,4,10,7), 3)

    def test_diagonal_line(self):
        self.assertEqual(shortest_distance(3,3,6,7), 5)