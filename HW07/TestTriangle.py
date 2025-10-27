# -*- coding: utf-8 -*-
"""
Updated Oct 27, 2025
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: jlb
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test_invalid_200(self):
        self.assertEqual(classifyTriangle(201, 150, 150), 'InvalidInput')

    def test_isosceles_alpha(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isoceles')

    def test_isosceles_beta(self):
        self.assertEqual(classifyTriangle(7, 10, 10), 'Isoceles')

    def test_scalene(self):
        self.assertEqual(classifyTriangle(7, 8, 9), 'Scalene')

    def test_not_a_triangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def test_zero_side(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'InvalidInput')

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_non_integer(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput')

    def test_large_valid_triangle(self):
        self.assertEqual(classifyTriangle(200, 199, 199), 'Isoceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

