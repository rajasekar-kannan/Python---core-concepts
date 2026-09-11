# number_methods.py

"""
Demonstrates Python number methods and numeric behaviors.
Focus: int methods, float methods, and numeric truthiness.
"""

# ---------------------------
# Integer Methods
# ---------------------------

def int_bit_length(n: int):

def int_to_bytes(n: int):

def int_from_bytes(b: bytes):


# ---------------------------
# Float Methods
# ---------------------------

def float_is_integer(n: float):

def float_as_ratio(n: float):

def float_to_hex(n: float):

def float_from_hex(hex_value: str):


# ---------------------------
# Common Numeric Behaviors
# ---------------------------

def absolute_number(n):

def rounded_number(n, digits=0):

def power(base, exp):

def quotient_and_remainder(a, b):


def is_truthy_number(n):

# ---------------------------
# Pytest Test Cases
# ---------------------------

import pytest

def test_int_methods():
    assert int_bit_length(10) == 4
    b = int_to_bytes(10)
    assert int_from_bytes(b) == 10

def test_float_methods():
    assert float_is_integer(10.0) is True
    assert float_is_integer(10.5) is False
    assert float_as_ratio(0.5) == (1, 2)

def test_float_hex():
    hex_value = float_to_hex(10.5)
    assert float_from_hex(hex_value) == 10.5

def test_common_numeric_behaviors():
    assert absolute_number(-10) == 10
    assert rounded_number(10.567, 2) == 10.57
    assert power(2, 3) == 8
    assert quotient_and_remainder(10, 3) == (3, 1)

def test_numeric_truthiness():
    assert is_truthy_number(0) is False
    assert is_truthy_number(0.0) is False
    assert is_truthy_number(5) is True
    assert is_truthy_number(-3) is True

# Run using:
# pytest number_methods.py
