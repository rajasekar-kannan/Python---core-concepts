# dict_methods.py

"""
Demonstrates Python dictionary methods and behaviors.
Focus: access, mutation, inspection, conditions.
"""

# ---------------------------
# Access
# ---------------------------

def get_value(data, key):
    return data.get(key)

def get_value_with_default(data, key, default):
    return data.get(key, default)


# ---------------------------
# Add / Update
# ---------------------------

def add_or_update(data, key, value):
    data[key] = value
    return data

def merge_dict(data, new_data):
    data.update(new_data)
    return data

def set_default_value(data, key, default):
    return data.setdefault(key, default)


# ---------------------------
# Remove
# ---------------------------

def remove_key(data, key):
    return data.pop(key, None)

def clear_dict(data):
    data.clear()
    return data


# ---------------------------
# Inspect
# ---------------------------

def get_keys(data):
    return list(data.keys())

def get_values(data):
    return list(data.values())

def get_items(data):
    return list(data.items())

def dict_size(data):
    return len(data)


# ---------------------------
# Conditions
# ---------------------------

def has_key(data, key):
    return key in data

def is_dict_truthy(data):
    return bool(data)


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
