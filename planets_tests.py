import unittest
import io, sys
from planets import *

class Test_planets(unittest.TestCase):

    def test_01(self):
        sys.stdin = io.StringIO("136")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 51.68 pounds.\nOn Jupiter you would weigh 318.24 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_02(self):
        sys.stdin = io.StringIO("0.0000")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh 0.00 pounds.\nOn Jupiter you would weigh 0.00 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())

    #testing negative numbers just in case
    def test_03(self):
        sys.stdin = io.StringIO("-4.8123")
        sys.stdout = student_output = io.StringIO()
        expected_out = "What do you weigh on earth? \nOn Mars you would weigh -1.83 pounds.\nOn Jupiter you would weigh -11.26 pounds."
        weight_on_planets()
        #print(student_output.getvalue().strip())
        self.assertEqual(expected_out, student_output.getvalue().strip())

if __name__ == "__main__":
        unittest.main()
