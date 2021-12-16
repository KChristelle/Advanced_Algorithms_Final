import unittest

from decrypt import Decryption
from encryptDecrypt import EncryptDecrypt
from grandingStudents import gradingStudents
from myTest import Summation
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

    # Test for question 3
    def test_array6(self):
        n_value = 148
        k = 3
        expected_answer = 3
        answer = Summation(n_value, k)
        self.assertEqual(answer, expected_answer)

    # Test for question 3
    def test_array7(self):
        n_value = 9875
        k = 4
        expected_answer = 8
        answer = Summation(n_value, k)
        self.assertEqual(answer, expected_answer)

    def test_array8(self):
        answer = EncryptDecrypt("Plain text", 2)
        expect_answer = "Pantxli et"
        self.assertEqual(answer, expect_answer)

    def test_array9(self):
        answer = Decryption("Pantxli et", 2)
        expect_answer = "Plain text"
        self.assertEqual(answer, expect_answer)

    def test_array10(self):
        answer = EncryptDecrypt("Plain text", 3)
        expect_answer = "Pnxli etat"
        self.assertEqual(answer, expect_answer)

    def test_array11(self):
        answer = Decryption("Pnxli etat", 3)
        expect_answer = "Plain text"
        self.assertEqual(answer, expect_answer)
