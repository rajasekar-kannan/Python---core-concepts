"""
if_else_conditions.py

This module demonstrates how Python if-else conditions work
across different data types in a clear and structured way.

Structure:
1. Business logic functions
2. Unit tests using unittest
"""

# =========================
# Business Logic Functions
# =========================

def check_string(value):
    """
    Evaluates a string condition.

    Returns:
    - "empty" if string is empty
    - "valid" if string has content
    - "invalid" if value is None or not a string
    """
    if value is None or not isinstance(value, str):
        return "invalid"
    if value:
        return "valid"
    return "empty"


def check_number(value):
    """
    Evaluates a number condition.

    Returns:
    - "positive" if number > 0
    - "zero" if number == 0
    - "negative" if number < 0
    - "invalid" if not a number
    """
    if not isinstance(value, (int, float)):
        return "invalid"
    if value > 0:
        return "positive"
    if value == 0:
        return "zero"
    return "negative"


def check_list(value):
    """
    Evaluates a list condition.

    Returns:
    - "empty" if list is empty
    - "single_item" if list has exactly one item
    - "multiple_items" if list has more than one item
    - "invalid" if value is not a list
    """
    if not isinstance(value, list):
        return "invalid"
    if not value:
        return "empty"
    if len(value) == 1:
        return "single_item"
    return "multiple_items"


def check_common(value):
    """
    Evaluates common truthy / falsy cases.

    Returns:
    - "truthy" if value evaluates to True
    - "falsy" if value evaluates to False
    """
    if value:
        return "truthy"
    return "falsy"


# =========================
# Unit Tests
# =========================

import unittest


class TestIfElseConditions(unittest.TestCase):

    # String tests
    def test_string_valid(self):
        self.assertEqual(check_string("Python"), "valid")

    def test_string_empty(self):
        self.assertEqual(check_string(""), "empty")

    def test_string_invalid(self):
        self.assertEqual(check_string(None), "invalid")
        self.assertEqual(check_string(123), "invalid")

    # Number tests
    def test_number_positive(self):
        self.assertEqual(check_number(10), "positive")

    def test_number_zero(self):
        self.assertEqual(check_number(0), "zero")

    def test_number_negative(self):
        self.assertEqual(check_number(-5), "negative")

    def test_number_invalid(self):
        self.assertEqual(check_number("10"), "invalid")

    # List tests
    def test_list_empty(self):
        self.assertEqual(check_list([]), "empty")

    def test_list_single_item(self):
        self.assertEqual(check_list([1]), "single_item")

    def test_list_multiple_items(self):
        self.assertEqual(check_list([1, 2, 3]), "multiple_items")

    def test_list_invalid(self):
        self.assertEqual(check_list("not a list"), "invalid")

    # Common truthy / falsy tests
    def test_common_truthy(self):
        self.assertEqual(check_common("data"), "truthy")
        self.assertEqual(check_common([1]), "truthy")

    def test_common_falsy(self):
        self.assertEqual(check_common(None), "falsy")
        self.assertEqual(check_common(""), "falsy")
        self.assertEqual(check_common(0), "falsy")


if __name__ == "__main__":
    unittest.main()
