#!/usr/bin/python3

"""Unittest for base"""

import unittest

from models.base import Base

class TestBase(unittest.TestCase):
    """"""
    def test_00_case_base_success_id(self):
        new_obj1 = Base()
        self.assertEqual(new_obj1.id, 2)

    def test_00_case_base_success_id_01(self):
        new_obj2 = Base(112)
        self.assertEqual(new_obj2.id, 112)

    def test_00_case_base_fail_id(self):
        new_obj3 = Base()
        self.assertNotEqual(new_obj3.id, 50)

    def test_00_case_base_fail_id_01(self):
        new_obj4 = Base(25)
        self.assertNotEqual(new_obj4.id, 50)

