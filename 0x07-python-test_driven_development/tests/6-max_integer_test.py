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
