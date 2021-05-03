import unittest
import average

class test_average(unittest.TestCase):
# Test whole number average
    def test_avg_whole(self):
        self.assertEqual(average.avg([2,2,2,2]), 2)
# Test floating point average
    def test_avg_floating(self):
        self.assertEqual(average.avg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.5)
# Test string list
    def test_avg_string(self):
        self.assertEqual(average.avg(['a', 'b', 'c', 'd', 'e']), 'f')
# Test empty list
    def test_avg_empty(self):
        self.assertEqual(average.avg([]), 0)
    
if __name__ == '__main__':
    unittest.main()

