#!/usr/bin/python3

"""Unittest for base"""

import unittest

from models.square import Square

class TestSquare(unittest.TestCase):
    """"""
    def test_00_case_base_success(self):
        new_obj = Square(5)
        self.assertEqual(new_obj.size, 5)

    def test_00_case_all_args_success(self):
        new_obj = Square(15, 4, 7, 15)
        self.assertEqual(new_obj.x, 4)

    def test_00_case_all_args_fail(self):
        with self.assertRaises(TypeError):
            new_obj = Square(15, 4, "40", 15)

    def test_00_case_all_args_fail_negatives(self):
        with self.assertRaises(ValueError):
            new_obj = Square(-15, -5, -2, 8)

    def test_00_case_all_args_fail_zero(self):
        with self.assertRaises(ValueError):
            new_obj = Square(0, 0, 0, 8)

    def test_01_case_fail_01_without_args(self):
        with self.assertRaises(TypeError):
            new_obj = Square()


    def test_02_setter_size_height_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.size = 40
        self.assertEqual(new_obj.height, 40)

    def test_02_setter_size_width_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.size = 40
        self.assertEqual(new_obj.width, 40)

    def test_02_setter_size_fail(self):
        new_obj = Square(8, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.size = -8

    def test_02_setter_x_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.x = 40
        self.assertEqual(new_obj.x, 40)

    def test_02_setter_y_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.y = 81
        self.assertEqual(new_obj.y, 81)

    def test_02_setter_x_fail(self):
        new_obj = Square(8, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.x = -8

    def test_02_setter_y_fail(self):
        new_obj = Square(8, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.y = -8

    def test_03_area_success(self):
        new_obj = Square(7, 5, 3, 26)
        self.assertEqual(new_obj.area(), 49)

    def test_03_area_fail(self):
        new_obj = Square(8, 5, 3, 26)
        self.assertNotEqual(new_obj.area(), 49)
