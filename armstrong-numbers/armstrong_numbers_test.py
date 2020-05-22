# import unittest
import pytest

from armstrong_numbers import is_armstrong_number

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

VALID = [
    (0, True),
    (5, True),
    (153, True),
    (9474, True),
    (9926315, True)]

INVALID = [
    (10, False),
    (100, False),
    (9475, False),
    (9926314, False)]

@pytest.mark.parametrize("check, expect", VALID)
def test_valid(check, expect):
    assert is_armstrong_number(check) == expect

@pytest.mark.parametrize("check, expect", INVALID)
def test_invalid(check, expect):
    assert is_armstrong_number(check) == expect

# class ArmstrongNumbersTest(unittest.TestCase):
#     def test_zero_is_an_armstrong_number(self):
#         self.assertIs(is_armstrong_number(0), True)

#     def test_single_digit_numbers_are_armstrong_numbers(self):
#         self.assertIs(is_armstrong_number(5), True)

#     def test_there_are_no_2_digit_armstrong_numbers(self):
#         self.assertIs(is_armstrong_number(10), False)

#     def test_three_digit_number_that_is_an_armstrong_number(self):
#         self.assertIs(is_armstrong_number(153), True)

#     def test_three_digit_number_that_is_not_an_armstrong_number(self):
#         self.assertIs(is_armstrong_number(100), False)

#     def test_four_digit_number_that_is_an_armstrong_number(self):
#         self.assertIs(is_armstrong_number(9474), True)

#     def test_four_digit_number_that_is_not_an_armstrong_number(self):
#         self.assertIs(is_armstrong_number(9475), False)

#     def test_seven_digit_number_that_is_an_armstrong_number(self):
#         self.assertIs(is_armstrong_number(9926315), True)

#     def test_seven_digit_number_that_is_not_an_armstrong_number(self):
#         self.assertIs(is_armstrong_number(9926314), False)


# if __name__ == "__main__":
#     unittest.main()
