import unittest

import regexcalc

class TestCalc2(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(regexcalc.extract_numbers("Suesha 1 is 43"),[1, 43])

    def test_2(self):
        self.assertAlmostEquals(regexcalc.extract_numbers("SUESHA"),[])

    def test_3(self):
        self.assertAlmostEquals(regexcalc.extract_numbers("12%SUESHA@67"),[12,67])

    def test_values(self):
        self.assertRaises(ValueError,regexcalc.extract_numbers,"")

    def test_type(self):
        self.assertRaises(TypeError, regexcalc.extract_numbers,12345)
        self.assertRaises(TypeError, regexcalc.extract_numbers,['suesha','is',3])