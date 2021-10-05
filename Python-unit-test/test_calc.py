import unittest 

import calc

class TestCalc1(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEquals(calc.extract_numbers("suesha12giri45"),1245) #arrange,act and assert

    def test_2(self):
        self.assertAlmostEquals(calc.extract_numbers("1@56suesha18g"),15618)
    
    def test_3(Self):
        Self.assertAlmostEquals(calc.extract_numbers('suesha'),False)


    def test_type(self):
        self.assertRaises(TypeError,calc.extract_numbers,[4,5,6,7])
        self.assertRaises(TypeError,calc.extract_numbers,456712)
    
    def test_value(self):
        self.assertRaises(ValueError,calc.extract_numbers,"")




