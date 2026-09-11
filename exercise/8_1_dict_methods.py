# dict_methods.py

"""
Demonstrates Python dictionary methods and behaviors.
Focus: access, mutation, inspection, conditions.
"""

# ---------------------------
# Access
# ---------------------------

def get_value(data, key):

def get_value_with_default(data, key, default):


# ---------------------------
# Add / Update
# ---------------------------

def add_or_update(data, key, value):


def merge_dict(data, new_data):

def set_default_value(data, key, default):


# ---------------------------
# Remove
# ---------------------------

def remove_key(data, key):

def clear_dict(data):



# ---------------------------
# Inspect
# ---------------------------

def get_keys(data):

def get_values(data):

def get_items(data):

def dict_size(data):


# ---------------------------
# Conditions
# ---------------------------

def has_key(data, key):

def is_dict_truthy(data):


# ---------------------------
# Pytest Tests
# ---------------------------

import pytest

def test_access():
    d = {"a": 1}
    assert get_value(d, "a") == 1
    assert get_value(d, "x") is None
    assert get_value_with_default(d, "x", 0) == 0

def test_add_update():
    d = {}
    assert add_or_update(d, "a", 1) == {"a": 1}
    assert merge_dict(d, {"b": 2}) == {"a": 1, "b": 2}

def test_setdefault():
    d = {"a": 1}
    assert set_default_value(d, "a", 100) == 1
    assert set_default_value(d, "b", 200) == 200
    assert d == {"a": 1, "b": 200}

def test_remove_clear():
    d = {"a": 1, "b": 2}
    assert remove_key(d, "a") == 1
    assert remove_key(d, "x") is None
    assert clear_dict(d) == {}

def test_inspect():
    d = {"a": 1, "b": 2}
    assert dict_size(d) == 2
    assert set(get_keys(d)) == {"a", "b"}
    assert set(get_values(d)) == {1, 2}
    assert ("a", 1) in get_items(d)

def test_conditions():
    d = {"a": 1}
    assert has_key(d, "a") is True
    assert is_dict_truthy(d) is True
    assert is_dict_truthy({}) is False

# Run using:
# pytest dict_methods.py
