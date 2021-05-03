import unittest
import cube

class test_cube(unittest.TestCase):
# Test integer inputs
    def test_cube1(self):
        self.assertEqual(cube.calculate(3), 27)
    def test_cube2(self):
        self.assertEqual(cube.calculate(5), 125)
    def test_cube3(self):
        self.assertEqual(cube.calculate(4), 16)
        
# Test floating point inputs
    def test_floating_point(self):
        self.assertEqual(cube.calculate(3.4), 39.304)
    def test_floating_point(self):
        self.assertEqual(cube.calculate(2.5), 15.625)
        
# Test invalid inputs
    def test_invalid_input(self):
        self.assertEqual(cube.calculate("r"), 8)
    def test_invalid_variable(self):
        self.assertEqual(cube.calculate(R), 69)
    
if __name__ == '__main__':
    unittest.main()

