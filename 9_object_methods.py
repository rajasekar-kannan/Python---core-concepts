# object_methods.py

"""
Demonstrates object behavior and object-level methods in Python.
Focus: identity, type, state, introspection.
"""

# ---------------------------
# Custom Class
# ---------------------------

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return f"User(name={self.name}, age={self.age})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.name == other.name and self.age == other.age


# ---------------------------
# Object Identity
# ---------------------------

def same_identity(a, b):
    return a is b

def same_value(a, b):
    return a == b


# ---------------------------
# Object Introspection
# ---------------------------

def get_class(obj):
    return obj.__class__

def has_attribute(obj, attr):
    return hasattr(obj, attr)

def get_attribute(obj, attr):
    return getattr(obj, attr, None)

def set_attribute(obj, attr, value):
    setattr(obj, attr, value)
    return obj

def delete_attribute(obj, attr):
    if hasattr(obj, attr):
        delattr(obj, attr)
    return obj


# ---------------------------
# Pytest Tests
# ---------------------------

import pytest

def test_identity_vs_equality():
    a = [1, 2]
    b = a
    c = [1, 2]

    assert same_identity(a, b) is True
    assert same_identity(a, c) is False
    assert same_value(a, c) is True

def test_custom_object():
    u = User("Raj", 25)
    assert u.is_adult() is True
    assert str(u) == "User(name=Raj, age=25)"

def test_object_equality():
    u1 = User("Raj", 25)
    u2 = User("Raj", 25)
    u3 = User("Raj", 17)

    assert u1 == u2
    assert u1 != u3

def test_introspection():
    u = User("Raj", 25)
    assert has_attribute(u, "name") is True
    assert get_attribute(u, "name") == "Raj"

    set_attribute(u, "city", "Chennai")
    assert u.city == "Chennai"

    delete_attribute(u, "city")
    assert not hasattr(u, "city")

def test_type_and_class():
    u = User("Raj", 25)
    assert get_class(u) == User
    assert isinstance(u, User)

# Run using:
# pytest object_methods.py
