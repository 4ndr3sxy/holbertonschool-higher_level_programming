#!/usr/bin/python3

"""Unittest for base"""

import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import io
from contextlib import redirect_stdout


class TestBase(unittest.TestCase):
    """"""
    def setUp(self):
        """Reset the number of objects"""
        Base._nb_objects = 0

    def test_00_case_base_success_id(self):
        new_obj1 = Base()
        self.assertEqual(new_obj1.id, 3)

    def test_00_case_base_success_id_01(self):
        new_obj2 = Base(112)
        self.assertEqual(new_obj2.id, 112)

    def test_00_case_base_fail_id(self):
        new_obj3 = Base()
        self.assertNotEqual(new_obj3.id, 50)

    def test_00_case_base_fail_id_01(self):
        new_obj4 = Base(25)
        self.assertNotEqual(new_obj4.id, 50)

    def test_01_case_instance_Rectangle_success(self):
        new_obj1 = Rectangle(5, 5)
        self.assertIsInstance(new_obj1, Rectangle)

    def test_01_case_instance_Square_success(self):
        new_obj1 = Square(5)
        self.assertIsInstance(new_obj1, Rectangle)

    def test_01_case_instance_fail_01(self):
        new_obj1 = {"size": 5}
        self.assertIsNot(new_obj1, (Rectangle, Square))

    def test_01_case_instance_fail_02(self):
        new_obj1 = {"width": 5, "height": 13}
        self.assertIsNot(new_obj1, (Rectangle, Square))

    def test_02_type_from_json_string_success(self):
        new_obj = Rectangle(2, 3)
        to_string = '[{"id": 1, "width": 10, "_Rectangle__height": 7, "_Rectangle__x": 2, "_Rectangle__y": 8}, {"id": 2, "_Rectangle__width": 2, "_Rectangle__height": 4, "_Rectangle__x": 0, "_Rectangle__y": 0}]'
        result = new_obj.from_json_string(to_string)
        self.assertEqual(type(result), list)

    def test_03_create_rquare_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsInstance(new_obj2, Square)

    def test_03_create_rectangle_success(self):
        new_obj1 = Rectangle(5, 2)
        dictionary = {"width": 10, "height": 5, "x": 2, "y": 2}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsInstance(new_obj2, Rectangle)

    def test_03_create_rquare_fail(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsNot(new_obj2, Rectangle)

    def test_03_create_rectangle_fail(self):
        new_obj1 = Rectangle(5, 2)
        dictionary = {"width": 10, "height": 5, "x": 2, "y": 2}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsNot(new_obj2, Square)

    def test_04_create_size_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertEqual(new_obj2.size, 10)

    def test_04_create_x_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        new_obj2.x = 15
        self.assertEqual(new_obj2.x, 15)

    def test_set_id_none(self):
        b_cero = Base()
        self.assertEqual(b_cero.id, 13)

    def test_set_id_none_fail(self):
        b_one = Base()
        self.assertNotEqual(b_one.id, 74)

    def test_set_id_74(self):
        b = Base(74)
        self.assertEqual(b.id, 74)

    def test_set_id_74_fail(self):
        b74 = Base()
        self.assertNotEqual(b74.id, 74)

    def test_private(self):
        b_private = Base(3)
        with self.assertRaises(AttributeError):
            print(b_private.nb_objects)
        with self.assertRaises(AttributeError):
            print(b_private.__nb_objects)

    def test_to_json_string(self):
        Base._Base__nb_objects = 0
        b1 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        b2 = {"id": 5, "width": 4, "height": 3, "x": 2, "y": 1}
        json_s = Base.to_json_string([b1, b2])
        self.assertTrue(type(json_s) is str)
        b0 = json.loads(json_s)
        self.assertEqual(b0, [b1, b2])

    def test_from_json_string_empty(self):
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string(self):
        """Tests normal from_json_string"""
        json_str = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, \
                     {"id": 5, "width": 4, "height": 3, "x": 2, "y": 1}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertEqual(json_l[0], {"id": 1, "width": 2, "height": 3,
                                     "x": 4, "y": 5})
        self.assertEqual(json_l[1], {"id": 5, "width": 4, "height": 3,
                                     "x": 2, "y": 1})

    def test_base_case_00(self):
        """Checks the display method"""
        file = io.StringIO()
        expected = "\n" * 2 + ((' ' * 2 + '#' * 2 + '\n') * 3)
        r1 = Rectangle(2, 3, 2, 2)
        with redirect_stdout(file):
            r1.display()
        self.assertEqual(file.getvalue(), expected)
    def test_base_case_01(self):
        """Checks the display method"""
        file = io.StringIO()
        expected = "\n" * 0 + ((' ' * 1 + '#' * 3 + '\n') * 2)
        r1 = Rectangle(3, 2, 1, 0)
        with redirect_stdout(file):
            r1.display()
        self.assertEqual(file.getvalue(), expected)

    def test_display(self):
        """Test display with valid arguments"""
        # creation of file that stores the
        # representation of display() in the future
        f = io.StringIO()
        s = ('#' * 4 + '\n') * 3
        r1 = Rectangle(4, 3)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

    def test_display_valid(self):
        """Test display with valid arguments"""
        file = io.StringIO()
        expected = ('#' * 32 + '\n') * 32
        r1 = Rectangle(32, 32)
        with redirect_stdout(file):
            r1.display()
        self.assertEqual(file.getvalue(), expected)
        file = io.StringIO()
        expected = ('#' * 2 + '\n') * 52
        r2 = Rectangle(2, 52)
        with redirect_stdout(file):
            r2.display()
        self.assertEqual(file.getvalue(), expected)

        """Tests for the instance id from base class"""
    def test_00_base_case(self):
        """Test for a instance"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_01_base_cases(self):
        """Tests normal instances"""
        b1 = Base()
        self.assertEqual(b1.id, 4)
        b2 = Base()
        self.assertEqual(b2.id, 5)
        b3 = Base()
        self.assertEqual(b3.id, 6)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 7)

    def test_02_giving_not_a_integer(self):
        """Tests for None case"""
        b6 = Base()
        self.assertEqual(b6.id, 8)
        b7 = Base()
        self.assertEqual(b7.id, 9)
        b8 = Base()
        self.assertEqual(b8.id, 10)
        b9 = Base(None)
        self.assertEqual(b9.id, 11)

    def test_03_arguments_in_init(self):
        """Tests for arguments exceded in the class"""
        with self.assertRaises(TypeError):
            b10 = Base(1, 2)

    def test_04_infinite_passed(self):
        """Tests when infinite is passed to the class"""
        b11 = Base(float('inf'))
        self.assertEqual(b11.id, float('inf'))

    def test_negative_numbers(self):
        """Tests for negative numbers"""
        b12 = Base(-13)
        self.assertEqual(b12.id, -13)

    def test_floats_numbers(self):
        """Tests for floats numbers"""
        b13 = Base(13.3)
        self.assertEqual(b13.id, 13.3)

    def test_float_negative_numbers(self):
        """Tests for float negative numbers"""
        b14 = Base(-13.3)
        self.assertEqual(b14.id, -13.3)

    def test_bolean_true(self):
        """Tests for bloean true"""
        b15 = Base(True)
        self.assertEqual(b15.id, 1)

    def test_bolean_false(self):
        """Tests for bolean false numbers"""
        b16 = Base(False)
        self.assertEqual(b16.id, 0)

    def test_list_01(self):
        """Tests for list"""
        b17 = Base([])
        self.assertEqual(b17.id, [])

    def test_tuple_01(self):
        """Tests for tuple"""
        b18 = Base(())
        self.assertEqual(b18.id, ())

    def test_list_02(self):
        """Tests for list"""
        b19 = Base([1])
        self.assertEqual(b19.id, [1])

    def test_tuple_02(self):
        """Tests for list"""
        b20 = Base((1))
        self.assertEqual(b20.id, 1)

    def test_list_03(self):
        """Tests for list"""
        b21 = Base([1, 2, 3])
        self.assertEqual(b21.id, [1, 2, 3])

    def test_tuple_03(self):
        """Tests for tuple"""
        b22 = Base((1, 2, 3))
        self.assertEqual(b22.id, (1, 2, 3))

    def test_strings(self):
        """Tests for string"""
        b23 = Base("python")
        self.assertEqual(b23.id, "python")

    def test_character(self):
        """Tests for characters"""
        b24 = Base('C')
        self.assertEqual(b24.id, 'C')

    def test_05_instances_with_same_id(self):
        """Tests instances with same id"""
        b25 = Base(123)
        self.assertEqual(b25.id, 123)
        b26 = Base(123)
        self.assertEqual(b26.id, 123)

    def test_06_ids_too_large(self):
        """Tests id with long numbers"""
        b27 = Base(54651513215645416546546548974486846874987889877)
        self.assertEqual(
            b27.id, 54651513215645416546546548974486846874987889877)
        b28 = Base(
            87437568947689547689576985487689547569847654756486798954)
        self.assertEqual(
            b28.id, 87437568947689547689576985487689547569847654756486798954)
