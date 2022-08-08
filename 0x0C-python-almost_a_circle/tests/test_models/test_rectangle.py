#!/usr/bin/python3
"""Unittest Class for module Rectangle Class"""
import unittest as utest
import pep8
from models.rectangle import Rectangle


class testRectangleDocs(utest.TestCase):
    def testPEP8_Rectangle(self):
        """Test that base.py conforms to PEP8 Style"""
        pep8Style = pep8.StyleGuide()
        check = pep8Style.check_files(['models/rectangle.py'])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 Style errors: %d" % check.total_errors)

    def testModuleDocString(self):
        """Test Doc String in modules"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def testClassDocString(self):
        """Test Doc String in class"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def testFuntionsDocString(self):
        """Test Doc String in functions"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)
