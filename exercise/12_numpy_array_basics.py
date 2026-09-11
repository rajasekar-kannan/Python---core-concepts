
"""
Demonstrates NumPy array creation, properties, operations, and utilities.
Focus: arrays, properties, math operations, reshaping, slicing, aggregation, random numbers.
"""

import numpy as np

# ---------------------------
# Creating Arrays
# ---------------------------

def create_1d_array():
    # 1, 2, 3, 4, 5

def create_2d_array():
    # [1, 2, 3], [4, 5, 6]


# ---------------------------
# Array Properties
# ---------------------------

def array_shape(arr):

def array_size(arr):

def array_dtype(arr):


# ---------------------------
# Special Arrays
# ---------------------------

def zeros_array():

def ones_array():

def identity_matrix():

def arange_array():
    # np.arange(start, stop, step) creates a NumPy array of evenly spaced values. Start from 0 (included). Stop before 10 (10 is not included)


def linspace_array():


# ---------------------------
# Mathematical Operations
# ---------------------------

def add_arrays(a, b):

def subtract_arrays(a, b):

def multiply_arrays(a, b):

def divide_arrays(a, b):

def dot_product(a, b):


# ---------------------------
# Array Reshaping
# ---------------------------

def reshape_array():


# ---------------------------
# Indexing & Slicing
# ---------------------------

def get_index_value(arr, index):

def get_slice(arr, start, end):


# ---------------------------
# Aggregation Functions
# ---------------------------

def array_sum(arr):

def array_mean(arr):

def array_std(arr):

def array_min(arr):

def array_max(arr):


# ---------------------------
# Random Numbers
# ---------------------------

def random_float_matrix():

def random_int_matrix():

# ---------------------------
# Pytest Test Cases
# ---------------------------

import pytest

def test_array_creation():
    arr1 = create_1d_array()
    arr2 = create_2d_array()

    assert arr1.tolist() == [1, 2, 3, 4, 5]
    assert arr2.shape == (2, 3)

def test_array_properties():
    arr = create_2d_array()

    assert array_shape(arr) == (2, 3)
    assert array_size(arr) == 6
    assert array_dtype(arr) == np.int64 or arr.dtype == np.int32

def test_special_arrays():
    assert np.array_equal(
        zeros_array(),
        np.array([
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0]
        ])
    )

    assert np.array_equal(
        ones_array(),
        np.array([
            [1.0, 1.0],
            [1.0, 1.0]
        ])
    )

    assert np.array_equal(
        identity_matrix(),
        np.array([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ])
    )

    assert np.allclose(
        linspace_array(),
        np.array([
            1.0,
            1.44444444,
            1.88888889,
            2.33333333,
            2.77777778,
            3.22222222,
            3.66666667,
            4.11111111,
            4.55555556,
            5.0
        ])
    )

    assert zeros_array().shape == (3, 3)
    
    assert ones_array().sum() == 4
    assert np.array_equal(identity_matrix(), np.eye(3))
    assert np.array_equal(arange_array(), np.array([0, 2, 4, 6, 8]))
    assert len(linspace_array()) == 10

def test_mathematical_operations():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    assert np.array_equal(add_arrays(a, b), np.array([5, 7, 9]))
    assert np.array_equal(subtract_arrays(a, b), np.array([-3, -3, -3]))
    assert np.array_equal(multiply_arrays(a, b), np.array([4, 10, 18]))
    assert np.allclose(divide_arrays(a, b), np.array([0.25, 0.4, 0.5]))
    assert dot_product(a, b) == 32

def test_array_reshaping():
    reshaped = reshape_array()

    assert reshaped.shape == (3, 3)
    assert reshaped[0, 0] == 1
    assert reshaped[2, 2] == 9

def test_indexing_and_slicing():
    arr = np.array([10, 20, 30, 40, 50])

    assert get_index_value(arr, 1) == 20
    assert np.array_equal(get_slice(arr, 1, 4), np.array([20, 30, 40]))

def test_aggregation_functions():
    arr = np.array([10, 20, 30, 40])

    assert array_sum(arr) == 100
    assert array_mean(arr) == 25
    assert np.isclose(array_std(arr), 11.180339887)
    assert array_min(arr) == 10
    assert array_max(arr) == 40

def test_random_arrays():
    rand_float = random_float_matrix()
    rand_int = random_int_matrix()

    assert rand_float.shape == (3, 3)
    assert rand_int.shape == (3, 3)
    assert rand_int.min() >= 1
    assert rand_int.max() < 100

def test_1d_array_slicing():
    arr = np.array([10, 20, 30, 40, 50])

    # Elements from index 1 to 3
    assert np.array_equal(arr[1:4], np.array([20, 30, 40]))

    # First three elements
    assert np.array_equal(arr[:3], np.array([10, 20, 30]))

    # Every second element
    assert np.array_equal(arr[::2], np.array([10, 30, 50]))


def test_2d_array_slicing():
    arr = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    # First two rows, from second column onward
    sliced = arr[:2, 1:]

    expected = np.array([
        [2, 3],
        [5, 6]
    ])

    assert np.array_equal(sliced, expected)


def test_slicing_creates_view_not_copy():
    arr = np.array([10, 20, 30, 40, 50])

    # Create a slice
    sliced = arr[1:4]

    # Modify slice
    sliced[0] = 999

    # Change should reflect in original array
    assert arr[1] == 999
    assert sliced[0] == 999

def test_array_dimensions_ndim():
    # 1D Array
    arr1 = np.array([1, 2, 3])
    assert arr1.ndim == 1

    # 2D Array
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    assert arr2.ndim == 2

    # 3D Array
    arr3 = np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ])
    assert arr3.ndim == 3
    
"""
| Function         | Use when                   |
| ---------------- | -------------------------- |
| `np.array_equal` | Integers or exact equality |
| `np.allclose`    | Floating-point numbers     |
| `np.isclose`     | Single float comparison    |
"""

# Run using:
# pytest 12_numpy_array_basics.py
