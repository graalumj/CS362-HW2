# Working on this program
# Don't understand Python well enough
import unittest
import name

class test_fullname(unittest.TestCase):
    def test_correct_input1(self):
        self.assertEqual(name.full_name("Alex", "Graalum"),"Alex Graalum")
    def test_correct_input2(self):
        self.assertEqual(name.full_name("123", "456"),"123 456")
if __name__ == '__main__':
    unittest.main()

