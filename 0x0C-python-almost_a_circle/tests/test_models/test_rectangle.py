#!/usr/bin/python3
"""Unittest for base"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import io
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """Test to file/ class Rectangle"""

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
        new_obj5 = Rectangle(5, 10)
        self.assertEqual(new_obj5.id, 30)

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

    def test_dimensions(self):
        """ check if w & h dimensions are validate """
        rDim = Rectangle(2, 8)
        self.assertEqual(rDim.width, 2)
        self.assertEqual(rDim.height, 8)
        rDim.width = 10
        rDim.height = 3
        self.assertEqual(rDim.width, 10)
        self.assertEqual(rDim.height, 3)
        rDim.width = 0x0F
        rDim.height = 0x0F
        self.assertEqual(rDim.width, 15)
        self.assertEqual(rDim.height, 15)
        self.assertRaises(TypeError, Rectangle, 'Cinco', 10)
        self.assertRaises(TypeError, Rectangle, 10, '5')
        self.assertRaises(TypeError, Rectangle, None, 10)
        self.assertRaises(TypeError, Rectangle, 10, None)
        self.assertRaises(TypeError, Rectangle, True, 10)
        self.assertRaises(TypeError, Rectangle, 10, True)
        self.assertRaises(ValueError, Rectangle, -5, 10)
        self.assertRaises(ValueError, Rectangle, 5, -10)
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 0, 10)

    def test_update_args(self):
        """ check the update function with 'no-keyword' arguments """
        rUpdateArg = Rectangle(1, 2)
        rUpdateArg.update(6)
        self.assertEqual(rUpdateArg.id, 6)
        rUpdateArg.update(10, 5)
        self.assertEqual(rUpdateArg.id, 10)
        self.assertEqual(rUpdateArg.area(), 5 * 2)
        rUpdateArg.update(10, 10, 10)
        self.assertEqual(rUpdateArg.area(), 10 * 10)
        rUpdateArg.update(10, 10, 10, 10)
        self.assertEqual(rUpdateArg.x, 10)
        rUpdateArg.update(10, 10, 10, 10, 10)
        self.assertEqual(rUpdateArg.y, 10)
        rUpdateArg.update(5, 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 5)
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)
        rUpdateArg.update(5, 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 5)
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)
        rUpdateArg.update('A', 10, 15, 20, 25)
        self.assertEqual(rUpdateArg.id, 'A')
        self.assertEqual(rUpdateArg.area(), 10 * 15)
        self.assertEqual(rUpdateArg.x, 20)
        self.assertEqual(rUpdateArg.y, 25)
        self.assertRaises(TypeError, rUpdateArg.update(), 6, "3", 10, 19, 14)
        self.assertRaises(TypeError, rUpdateArg.update(), 10, 5, 5, None, 0)
        with self.assertRaises(ValueError):
            rUpdateArg.update(10, 5, 0, 0, 0)
        with self.assertRaises(ValueError):
            rUpdateArg.update(10, 0, 5, 0, 0)

    def test_update_kwargs(self):
        """ check update function with 'key-worded' argument """
        rUpdateKarg = Rectangle(1, 2)
        rUpdateKarg.update(id=6)
        self.assertEqual(rUpdateKarg.id, 6)
        rUpdateKarg.update(id=10, width=5)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 5 * 2)
        rUpdateKarg.update(id=10, width=7, height=8)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 8)
        rUpdateKarg.update(id=10, width=7, height=8, x=9)
        self.assertEqual(rUpdateKarg.id, 10)
        self.assertEqual(rUpdateKarg.area(), 7 * 8)
        self.assertEqual(rUpdateKarg.x, 9)
        rUpdateKarg.update(y=14, height=10, id=6, x=19, width=3)
        self.assertEqual(rUpdateKarg.id, 6)
        self.assertEqual(rUpdateKarg.area(), 30)
        self.assertEqual(rUpdateKarg.x, 19)
        self.assertEqual(rUpdateKarg.y, 14)

    def setUp(self):
        """Reset the number of objects"""
        Base._nb_objects = 0

    def test_args_order(self):
        """Checks correct order of arguments"""
        f = io.StringIO()
        s = "[Rectangle] (41) 10/10 - 10/89"
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=89)
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = "[Rectangle] (89) 10/10 - 10/10"
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(**{'id': 89})
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(width=1, x=2)
        f = io.StringIO()
        s = "[Rectangle] (89) 2/10 - 1/10"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(y=1, width=2, x=3, id=89)
        f = io.StringIO()
        s = "[Rectangle] (89) 3/1 - 2/10"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(x=1, height=2, y=3, width=4)
        f = io.StringIO()
        s = "[Rectangle] (89) 1/3 - 4/2"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = "[Rectangle] (89) 10/10 - 1/10"
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(**{'id': 89, 'width': 1})
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = "[Rectangle] (88) 10/10 - 1/2"
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(**{'id': 88, 'width': 1, 'height': 2})
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = "[Rectangle] (88) 3/10 - 1/2"
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(**{'id': 88, 'width': 1, 'height': 2, 'x': 3})
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = "[Rectangle] (88) 3/4 - 1/2"
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(**{'id': 88, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

    def test_wrong_keywords(self):
        """Test keywords"""
        s1 = Rectangle(10, 2, 1)
        s1.update(key=23, school=32)
        self.assertEqual(getattr(s1, "key", 0), 0)
        self.assertEqual(getattr(s1, "school", 0), 0)

    def test_many_args(self):
        """Test with too many arguments"""
        r1 = Rectangle(10, 10)
        r1.update(10, 10, 10, 10, 10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/10")
