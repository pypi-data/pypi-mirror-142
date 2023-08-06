# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 21:11:39 2022

@author: MERT
"""





import unittest
import poipackage


class TestPoiPackage(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(poipackage.abc(2, 2), 4)

    def test_subtraction(self):
        self.assertEqual(poipackage.abd(4, 2), 2)

        

if __name__ == '__main__':
    unittest.main()