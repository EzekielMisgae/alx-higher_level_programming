#!/usr/bin/python3
"""Unittest Class for module Base Class"""
import unittest as utest
import pep8
from models.base import Base


class testBaseDocs(utest.TestCase):
    def testPEP8_Base(self):
        """Test that base.py conforms to PEP8 Style"""
        pep8Style = pep8.StyleGuide()
        check = pep8Style.check_files(['models/base.py'])
        self.assertEqual(check.total_errors, 0,
                         "PEP8 Style errors: %d" % check.total_errors)

    def testModuleDocString(self):
        """Test Doc String in modules"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def testClassDocString(self):
        """Test Doc String in class"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def testFuntionsDocString(self):
        """Test Doc String in functions"""
        self.assertTrue(len(Base.__doc__) >= 1)
