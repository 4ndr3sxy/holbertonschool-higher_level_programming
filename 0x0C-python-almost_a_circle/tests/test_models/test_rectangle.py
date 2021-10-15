#!/usr/bin/python3

"""Unittest for base"""

import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """"""
    def test_00_case_width_success(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.width, 5)

    def test_00_case_height_success(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.height, 10)

    def test_00_case_x_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.x, 0)

    def test_00_case_y_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.y, 0)

    def test_00_case_id_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.id, 2)



    def test_00_case_width_success_01(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.width, 8)

    def test_00_case_height_success_01(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.height, 12)

    def test_00_case_x_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.x, 5)

    def test_00_case_y_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.y, 3)

    def test_00_case_id_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.id, 26)

    def test_01_case_fail_01_one_arg(self):
        with self.assertRaises(TypeError):
            new_obj = Rectangle(5)

    def test_01_case_fail_02_without_args(self):
        with self.assertRaises(TypeError):
            new_obj = Rectangle()

    def test_01_case_fail_03_args_letter_int(self):
        with self.assertRaises(TypeError):
            new_obj = Rectangle("a",5)

    def test_01_case_fail_04_args_letters(self):
        with self.assertRaises(TypeError):
            new_obj = Rectangle("a","b")

    
    