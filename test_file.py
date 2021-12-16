import unittest

from grandingStudents import gradingStudents
from test_file import *
from totalSum import totalSum


class TestSummative(unittest.TestCase):
    # Test for question 1 for 10
    def test_array1(self):
        number = 10
        expected_answer = 55
        answer = totalSum(number)
        self.assertEqual(answer, expected_answer)

    # Test for question 1 for 10000
    def test_array2(self):
        number = 10000
        expected_answer = 50005000
        answer = totalSum(number)
        self.assertEqual(answer, expected_answer)

    # Test for question 1 for 1000000
    def test_array3(self):
        number = 1000000
        expected_answer = 500000500000
        answer = totalSum(number)
        self.assertEqual(answer, expected_answer)

    # Test for question 2
    def test_array5(self):
        grades = [4, 73, 67, 38, 33]
        expected_answer = [75, 67, 40, 33]
        answer = gradingStudents(grades)
        self.assertEqual(answer, expected_answer)

    # def test_array2(self):
        # n = 80
        # ar = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5, 2, 7, 2, 1, 0, 9, 8, 61, 11, 2,
        #       4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 0, 6, 6, 3, 6, 1, 4, 5, 5, 5, 2, 7, 23, 1, 0, 9, 8, 61, 11, 2,
        #       4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 15]
        # answer = sock_merchant(n, ar)
        # expect_answer = 36
        # self.assertEqual(answer, expect_answer)


