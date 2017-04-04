# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest

from record_locator.record_locator import RecordLocator


class TestRecordLocator(unittest.TestCase):

    def test_default_record_locator(self):
        rl = RecordLocator()
        self.assertEqual("6R", rl.encode(100))
        self.assertEqual(100, rl.decode("6R"))
        self.assertEqual("3G7W3A", rl.encode(20290290))
        self.assertTrue(rl.encode(20290290).isupper())
        self.assertEqual(20290290, rl.decode("3G7W3A"))
        self.assertEqual(20290290, rl.decode(rl.encode(20290290)))

    def test_custom_record_locator(self):
        rl = RecordLocator(base_characters="ABCDEFGHIJKL")
        self.assertEqual("IE", rl.encode(100))
        self.assertEqual(100, rl.decode("IE"))
        self.assertEqual("GJGGAJG", rl.encode(20290290))
        self.assertTrue(rl.encode(20290290).isupper())
        self.assertEqual(20290290, rl.decode("GJGGAJG"))
        self.assertEqual(20290290, rl.decode(rl.encode(20290290)))

    def test_check_digit(self):
        rl = RecordLocator(has_check_digit=True)
        self.assertEqual("6RK", rl.encode(100))
        self.assertEqual(100, rl.decode("6RK"))
        self.assertEqual("3G7W3AA", rl.encode(20290290))
        self.assertTrue(rl.encode(20290290).isupper())
        self.assertEqual(20290290, rl.decode("3G7W3AA"))
        self.assertEqual(20290290, rl.decode(rl.encode(20290290)))
