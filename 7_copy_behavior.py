# copy_behavior.py

"""
Demonstrates shallow vs deep copy behavior in Python.
Focus: nested lists and reference behavior.

Key Rules (memorize these)
Rule 1
    = never copies — it just points
Rule 2
    Shallow copy copies only the first level
Rule 3
    Nested mutable objects are shared in shallow copies
Rule 4
    Only deepcopy() guarantees isolation

| Scenario                         | Use          |
| -------------------------------- | ------------ |
| Flat list of numbers             | Shallow copy |
| 2D list                          | Deep copy    |
| Dict with lists                  | Deep copy    |
| Performance-critical & read-only | Shallow      |
| Tests / isolation                | Deep         |

"""

import copy


# ---------------------------
# No Copy (Assignment)
# ---------------------------

def no_copy(original):
    return original


# ---------------------------
# Shallow Copies
# ---------------------------

def shallow_copy_list(original):
    return original.copy()

def shallow_copy_slice(original):
    return original[:]

def shallow_copy_module(original):
    return copy.copy(original)


# ---------------------------
# Deep Copy
# ---------------------------

def deep_copy(original):
    return copy.deepcopy(original)


# ---------------------------
# Pytest Tests
# ---------------------------

import pytest

def test_no_copy():
    original = [[1, 2], [3, 4]]
    new = no_copy(original)
    new[0][0] = 99
    assert original[0][0] == 99  # same object

def test_shallow_copy():
    original = [[1, 2], [3, 4]]
    new = shallow_copy_list(original)
    new[0][0] = 99
    assert original[0][0] == 99  # inner list shared

def test_shallow_copy_slice():
    original = [[1, 2], [3, 4]]
    new = shallow_copy_slice(original)
    new[1][1] = 88
    assert original[1][1] == 88

def test_shallow_copy_module():
    original = [[1, 2], [3, 4]]
    new = shallow_copy_module(original)
    new[0][1] = 77
    assert original[0][1] == 77

def test_deep_copy():
    original = [[1, 2], [3, 4]]
    new = deep_copy(original)
    new[0][0] = 99
    assert original[0][0] == 1  # fully independent

def test_outer_change_shallow():
    original = [[1, 2], [3, 4]]
    new = shallow_copy_list(original)
    new.append([5, 6])
    assert len(original) == 2  # outer list copied

def test_outer_change_deep():
    original = [[1, 2], [3, 4]]
    new = deep_copy(original)
    new.append([5, 6])
    assert len(original) == 2

# Run using:
# pytest copy_behavior.py
