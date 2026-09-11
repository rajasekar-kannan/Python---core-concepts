"""
dictionary_filtering_methods.py

Focused examples of filtering and functional-style operations
(map, filter, reduce, any, all) applied to dictionaries.
"""

from functools import reduce

# =========================
# Logic Section
# =========================

def filter_by_value_greater_than(data, threshold):
    """
    Keep items where value > threshold.
    """



def filter_by_key_startswith(data, prefix):
    """
    Keep items where key starts with a given prefix.
    """



def map_values_double(data):
    """
    Transform values by doubling them.
    """


def map_values_conditionally(data):
    """
    Double values only if they are even.
    """



def reduce_sum_of_values(data):
    """
    Reduce dictionary values into a single sum.
    """


def any_value_above_threshold(data, threshold):
    """
    Check if ANY value satisfies the condition.
    """


def all_values_positive(data):
    """
    Check if ALL values are positive.
    """


def filter_nested_dictionary(data, threshold):
    """
    Filter nested dictionary values by threshold.

    Example:
    {
        "user1": {"score": 80},
        "user2": {"score": 40}
    }
    """
    

def find_max_value_key(data):
    """Return key with maximum value."""
    

def count_nested_keys(nested_data):
    """
    Count total keys in a nested dictionary.
    """
    


def flatten_nested_dictionary(nested_data):
    """
    Flatten one-level nested dictionary.
    """
   
# =========================
# Pytest Test Section
# =========================

def test_filter_by_value_greater_than():
    data = {"a": 10, "b": 5, "c": 20}
    assert filter_by_value_greater_than(data, 9) == {"a": 10, "c": 20}


def test_filter_by_key_startswith():
    data = {"prod_1": 10, "dev_1": 5, "prod_2": 20}
    assert filter_by_key_startswith(data, "prod") == {
        "prod_1": 10,
        "prod_2": 20
    }


def test_map_values_double():
    data = {"a": 2, "b": 3}
    assert map_values_double(data) == {"a": 4, "b": 6}


def test_map_values_conditionally():
    data = {"a": 2, "b": 3, "c": 4}
    assert map_values_conditionally(data) == {"a": 4, "b": 3, "c": 8}


def test_reduce_sum_of_values():
    data = {"a": 1, "b": 2, "c": 3}
    assert reduce_sum_of_values(data) == 6


def test_any_value_above_threshold():
    data = {"a": 10, "b": 5}
    assert any_value_above_threshold(data, 9) is True
    assert any_value_above_threshold(data, 20) is False


def test_all_values_positive():
    assert all_values_positive({"a": 1, "b": 2}) is True
    assert all_values_positive({"a": 1, "b": -2}) is False


def test_filter_nested_dictionary():
    data = {
        "user1": {"score": 80},
        "user2": {"score": 40},
        "user3": {"score": 90},
    }

    result = {
        "user1": {"score": 80},
        "user3": {"score": 90},
    }

    assert filter_nested_dictionary(data, 50) == result

def test_find_max_value_key():
    data = {"a": 10, "b": 50, "c": 20}
    assert find_max_value_key(data) == "b"
    assert find_max_value_key({}) is None


def test_count_nested_keys():
    data = {
        "user": {"id": 1, "name": "Raj"},
        "meta": {"active": True}
    }
    assert count_nested_keys(data) == 3


def test_flatten_nested_dictionary():
    data = {
        "user": {"id": 1, "name": "Raj"},
        "meta": {"active": True}
    }
    result = {
        "user.id": 1,
        "user.name": "Raj",
        "meta.active": True
    }
    assert flatten_nested_dictionary(data) == result