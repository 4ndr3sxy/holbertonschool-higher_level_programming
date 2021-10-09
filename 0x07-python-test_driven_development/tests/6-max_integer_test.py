#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """"""
    def test_00_case_base_success(self):
        array = [1, 2, 3, 4]
        self.assertEqual(max_integer(array), 4)

    def test_00_case_base_success_int_float(self):
        array = [1, 2.8, 3, 4, 4.5]
        self.assertEqual(max_integer(array), 4.5)

    def test_00_case_base_success_int_float_reverse(self):
        array = [4.5, 4, 3, 2.8, 1]
        self.assertEqual(max_integer(array), 4.5)

    def test_00_case_base_success_int_float_middle(self):
        array = [4.5, 4, 88.3, 2.8, 1]
        self.assertEqual(max_integer(array), 88.3)

    def test_00_case_base_success_one_value_float(self):
        array = [99.5]
        self.assertEqual(max_integer(array), 99.5)

    def test_00_case_base_success_one_value_int(self):
        array = [81]
        self.assertEqual(max_integer(array), 81)

    def test_00_case_base_fail(self):
        array = [1, 2, 3, 4]
        self.assertNotEqual(max_integer(array), 8)

    def test_01_case_array_empty_success(self):
        array = []
        self.assertEqual(max_integer(array), None)

    def test_01_case_array_empty_fail(self):
        array = []
        self.assertNotEqual(max_integer(array), 4)

    def test_02_case_array_object_success(self):
        array = [1, 2, 3, 4]
        self.assertIsInstance(array, list)

    def test_02_case_array_object_success_1(self):
        array = []
        self.assertIsInstance(array, list)

    def test_02_case_array_object_fail(self):
        array = ""
        self.assertNotIsInstance(array, list)

    def test_02_case_array_object_fail_1(self):
        array = {1, 2, 3, 4}
        self.assertNotIsInstance(array, list)

    def test_02_case_array_object_fail_2(self):
        array = (1, 2, 3, 4)
        self.assertNotIsInstance(array, list)

    def test_02_case_array_object_fail_2(self):
        array = (1, 2, 3, 4)
        self.assertNotIsInstance(array, list)

    def validate_type_array(self, array, types):
        for val in array:
            if type(val) not in types:
                return 0
        return 1

    def test_03_case_type_array_success_int(self):
        array = [2, 4, 6 , 8]
        validator = self.validate_type_array(array, (float, int))
        self.assertEqual(validator, 1)

    def test_03_case_type_array_success_float(self):
        array = [2.5, 4.33, 6.15 , 8.01]
        validator = self.validate_type_array(array, (float, int))
        self.assertEqual(validator, 1)

    def test_03_case_type_array_success_float_int(self):
        array = [2.5, 4, 6.15 , 8]
        validator = self.validate_type_array(array, (float, int))
        self.assertEqual(validator, 1)

    def test_03_case_type_array_fail_string(self):
        array = [2.5, 4.33, 6.15 , "xy"]
        validator = self.validate_type_array(array, (float, int))
        self.assertEqual(validator, 0)

    def test_03_case_type_array_fail_tuple(self):
        array = [2.5, 4.33, 6.15 , (1, 2, 3, 4)]
        validator = self.validate_type_array(array, (float, int))
        self.assertEqual(validator, 0)

    def test_04_case_list_mixed(self):
        with self.assertRaises(TypeError):
            max_integer([[1], [3], [5], [9], "house", [11]])

    def test_04_case_list_tuple_fail(self):
        """Typeerror"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, (5, 10, 15)])



