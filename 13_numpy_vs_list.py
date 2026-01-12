
import numpy as np
import time
import sys

# ---------------------------
# Performance Comparison
# ---------------------------

def python_list_multiply(a, b):
    return [x * y for x, y in zip(a, b)]

def numpy_array_multiply(a, b):
    return a * b

# ---------------------------
# Pytest Test Cases
# ---------------------------

import pytest

def test_numpy_vs_python_list_speed():
    size = 10**5  # Keep test fast and stable

    py_list1 = list(range(size))
    py_list2 = list(range(size))

    np_array1 = np.arange(size)
    np_array2 = np.arange(size)

    # Time Python list multiplication
    start = time.perf_counter()
    python_list_multiply(py_list1, py_list2)
    python_time = time.perf_counter() - start
    print(f"Python list multiplication time: {python_time:.6f} seconds")

    # Time NumPy array multiplication
    start = time.perf_counter()
    numpy_array_multiply(np_array1, np_array2)
    numpy_time = time.perf_counter() - start
    print(f"NumPy array multiplication time: {numpy_time:.6f} seconds")
    
    # Assertion: NumPy should be faster
    assert numpy_time < python_time


def test_numpy_vs_python_list_memory_usage():
    size = 1000

    # Python list memory usage
    py_list = list(range(size))
    py_list_memory = (
        sys.getsizeof(py_list) +
        sum(sys.getsizeof(item) for item in py_list)
    )

    # NumPy array memory usage
    np_array = np.arange(size)
    np_array_memory = np_array.nbytes

    print(f"Python list memory usage: {py_list_memory} bytes")
    print(f"NumPy array memory usage: {np_array_memory} bytes")

    # Assertion: NumPy should be more memory efficient
    assert np_array_memory < py_list_memory


# Run using:
# pytest 13_numpy_vs_list.py 
# pytest -s 13_numpy_vs_list.py // with print statements