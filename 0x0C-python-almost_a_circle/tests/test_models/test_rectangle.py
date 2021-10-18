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

    def test_00_case_x_negative(self):
        with self.assertRaises(ValueError):
            new_obj = Rectangle(8, 12, -5, 3, 26)

    def test_00_case_y_negative(self):
        with self.assertRaises(ValueError):
            new_obj = Rectangle(8, 12, 5, -3, 26)

    def test_00_case_id_default_negative_width(self):
        with self.assertRaises(ValueError):
            new_obj = Rectangle(-5, 10)

    def test_00_case_id_default_negative_height(self):
        with self.assertRaises(ValueError):
            new_obj = Rectangle(5, -10)

    def test_01_case_fail_01_one_arg(self):
        with self.assertRaises(TypeError):
            new_obj = Rectangle(5)

    def test_01_case_fail_02_without_args(self):
        with self.assertRaises(TypeError):
            new_obj = Rectangle()

    def test_12_case_height_string(self):
        with self.assertRaises(TypeError):
            Rectangle(8, "string", 5, 3, 26)

    def test_01_case_fail_03_args_letter_int(self):
        with self.assertRaises(TypeError):
            new_obj = Rectangle("a", 5)

    def test_01_case_fail_04_args_letters(self):
        with self.assertRaises(TypeError):
            new_obj = Rectangle("a", "b")

    def test_02_setter_width_success(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        new_obj.width = 40
        self.assertEqual(new_obj.width, 40)

    def test_02_setter_height_success(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        new_obj.height = 81
        self.assertEqual(new_obj.height, 81)

    def test_02_setter_width_fail(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.width = -8

    def test_02_setter_height_fail(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.height = -8

    def test_02_setter_x_success(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        new_obj.x = 40
        self.assertEqual(new_obj.x, 40)

    def test_02_setter_y_success(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        new_obj.y = 81
        self.assertEqual(new_obj.y, 81)

    def test_02_setter_x_fail(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.x = -8

    def test_02_setter_y_fail(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.y = -8

    def test_03_area_success(self):
        new_obj = Rectangle(7, 11, 5, 3, 26)
        self.assertEqual(new_obj.area(), 77)

    def test_03_area_fail(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertNotEqual(new_obj.area(), 77)

    def test_10_case_instance_rectangle(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertIsInstance(new_obj, Rectangle)

    def test_13_case_x_string(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 12, "x", 3, 26)

    def test_14_case_y_string(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 12, 5, "y", 26)

    def test_22_case_whit_float_values(self):
        with self.assertRaises(TypeError):
            Rectangle(3.8, 5.6, 7, 9)

    def test_21_case_whit_more_than_one_value(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 3, 7, 8, 9, 10)

    def test_23_case_whit_list(self):
        with self.assertRaises(TypeError):
            Rectangle([7, 9], 3)

    def test_24_case_check_area_result(self):
        new_obj = Rectangle(3, 2)
        self.assertEqual(new_obj.area(), 6)
        with self.assertRaises(TypeError):
            Rectangle.area()
        self.assertEqual(new_obj.area(), 6)
        with self.assertRaises(TypeError):
            Rectangle.area(3, 5, 6)
        self.assertEqual(new_obj.area(), 6)
        with self.assertRaises(TypeError):
            Rectangle.area(float('inf'), 5)
