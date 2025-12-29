# list_methods.py

"""
Demonstrates Python list methods and behaviors.
Focus: mutation, searching, ordering, truthiness.
"""

# ---------------------------
# Adding elements
# ---------------------------

def add_item(lst, item):
    lst.append(item)
    return lst

def add_items(lst, items):
    lst.extend(items)
    return lst

def insert_item(lst, index, item):
    lst.insert(index, item)
    return lst


# ---------------------------
# Removing elements
# ---------------------------

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def pop_item(lst, index=None):
    if not lst:
        return None
    
    # return lst.pop() if index is None else lst.pop(index)

    if index is None:
      return lst.pop()
    else:
        return lst.pop(index)

def clear_list(lst):
    lst.clear()
    return lst


# ---------------------------
# Searching & checking
# ---------------------------

def find_index(lst, item):
    return lst.index(item) if item in lst else -1

def count_item(lst, item):
    return lst.count(item)

def contains_item(lst, item):
    return item in lst


# ---------------------------
# Ordering & copying
# ---------------------------

def sort_list(lst):
    lst.sort()
    return lst

def reverse_list(lst):
    lst.reverse()
    return lst

def copy_list(lst):
    return lst.copy()


# ---------------------------
# Truthiness
# ---------------------------

def is_list_truthy(lst):
    return bool(lst)


# ---------------------------
# Pytest Tests
# ---------------------------

import pytest

def test_add_methods():
    assert add_item([1, 2], 3) == [1, 2, 3]
    assert add_items([1], [2, 3]) == [1, 2, 3]
    assert insert_item([1, 3], 1, 2) == [1, 2, 3]

def test_remove_methods():
    assert remove_item([1, 2, 3], 2) == [1, 3]
    assert pop_item([1, 2, 3]) == 3
    assert clear_list([1, 2]) == []

def test_search_methods():
    assert find_index([1, 2, 3], 2) == 1
    assert find_index([1, 2], 5) == -1
    assert count_item([1, 1, 2], 1) == 2
    assert contains_item([1, 2, 3], 3) is True

def test_ordering_methods():
    assert sort_list([3, 1, 2]) == [1, 2, 3]
    assert reverse_list([1, 2, 3]) == [3, 2, 1]

def test_copy_method():
    original = [1, 2]
    copied = copy_list(original)
    copied.append(3)
    assert original == [1, 2]
    assert copied == [1, 2, 3]

def test_list_truthiness():
    assert is_list_truthy([]) is False
    assert is_list_truthy([1]) is True

# Run using:
# pytest list_methods.py
