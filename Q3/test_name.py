# Working on this program
# Don't understand Python well enough
import unittest
import name

f = raw_input("Enter first name: ")
l = raw_input("Enter last name: ")

class test_fullname(unittest.TestCase):
    if not f.isalpha():
        print("First name is not a valid input.")
    elif not l.isalpha():
        print("Last name is not a valid input.")
    elif f == "":
        print("First name can not be empty.")
    elif l == "":
        print("Last name can not be empty.")
    else:
        def test_correct_input1(self):
            self.assertEqual(name.full_name(f, l),f + " " + l)

if __name__ == '__main__':
    unittest.main()

