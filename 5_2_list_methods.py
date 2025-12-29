"""
list_functional_methods.py

Demonstrates functional-style operations on Python lists:
map, filter, reduce, and related helpers.
"""

from functools import reduce

# =========================
# Logic Section
# =========================

def double_numbers(numbers):
    """Return a list with each number doubled."""
    return list(map(lambda x: x * 2, numbers))


def get_even_numbers(numbers):
    """Return only even numbers from the list."""
    return list(filter(lambda x: x % 2 == 0, numbers))


def sum_numbers(numbers):
    """Return the sum of all numbers in the list."""
    if not numbers:
        return 0
    return reduce(lambda a, b: a + b, numbers)


def multiply_numbers(numbers):
    """Return the product of all numbers in the list."""
    if not numbers:
        return 1
    return reduce(lambda a, b: a * b, numbers)


def has_any_positive(numbers):
    """Check if the list has at least one positive number."""
    return any(map(lambda x: x > 0, numbers))


def are_all_positive(numbers):
    """Check if all numbers are positive."""
    return all(map(lambda x: x > 0, numbers))


def sort_by_length(strings):
    """Sort list of strings by their length."""
    return sorted(strings, key=lambda s: len(s))


def get_longest_string(strings):
    """Return the longest string from the list."""
    if not strings:
        return None
    return max(strings, key=lambda s: len(s))


def get_shortest_string(strings):
    """Return the shortest string from the list."""
    if not strings:
        return None
    return min(strings, key=lambda s: len(s))


# =========================
# Pytest Test Section
# =========================

def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]


def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_sum_numbers():
    assert sum_numbers([1, 2, 3, 4]) == 10
    assert sum_numbers([]) == 0


def test_multiply_numbers():
    assert multiply_numbers([1, 2, 3, 4]) == 24
    assert multiply_numbers([]) == 1


def test_has_any_positive():
    assert has_any_positive([-1, -2, 3]) is True
    assert has_any_positive([-1, -2, -3]) is False


def test_are_all_positive():
    assert are_all_positive([1, 2, 3]) is True
    assert are_all_positive([1, -2, 3]) is False


def test_sort_by_length():
    assert sort_by_length(["aaa", "b", "cc"]) == ["b", "cc", "aaa"]


def test_get_longest_string():
    assert get_longest_string(["a", "abcd", "abc"]) == "abcd"
    assert get_longest_string([]) is None


def test_get_shortest_string():
    assert get_shortest_string(["a", "abcd", "abc"]) == "a"
    assert get_shortest_string([]) is None
