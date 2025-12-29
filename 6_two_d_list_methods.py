# two_d_list_methods.py

"""
Demonstrates 2D list (nested list) behavior in Python.
Focus: access, mutation, traversal, conditions.
"""

# ---------------------------
# Creation
# ---------------------------

def create_matrix(rows):
    return [row.copy() for row in rows]


# ---------------------------
# Access
# ---------------------------

def get_cell(matrix, row, col):
    return matrix[row][col]

def get_row(matrix, row):
    return matrix[row]

def get_column(matrix, col):
    return [row[col] for row in matrix]


# ---------------------------
# Update
# ---------------------------

def update_cell(matrix, row, col, value):
    matrix[row][col] = value
    return matrix

def update_row(matrix, row, new_row):
    matrix[row] = new_row
    return matrix


# ---------------------------
# Add / Remove
# ---------------------------

def add_row(matrix, row):
    matrix.append(row)
    return matrix

def remove_row(matrix, index):
    matrix.pop(index)
    return matrix


# ---------------------------
# Conditions
# ---------------------------

def has_rows(matrix):
    return bool(matrix)

def has_columns(matrix):
    return bool(matrix and matrix[0])

def matrix_shape(matrix):
    if not matrix:
        return (0, 0)
    return (len(matrix), len(matrix[0]))


# ---------------------------
# Pytest Tests
# ---------------------------

import pytest

def test_access():
    m = [[1, 2], [3, 4]]
    assert get_cell(m, 0, 1) == 2
    assert get_row(m, 1) == [3, 4]
    assert get_column(m, 0) == [1, 3]

def test_update():
    m = [[1, 2], [3, 4]]
    assert update_cell(m, 1, 0, 99)[1][0] == 99
    assert update_row(m, 0, [7, 8])[0] == [7, 8]

def test_add_remove():
    m = [[1, 2]]
    assert add_row(m, [3, 4]) == [[1, 2], [3, 4]]
    assert remove_row(m, 0) == [[3, 4]]

def test_conditions():
    assert has_rows([[1]]) is True
    assert has_rows([]) is False
    assert has_columns([[1, 2]]) is True
    assert matrix_shape([[1, 2], [3, 4]]) == (2, 2)
    assert matrix_shape([]) == (0, 0)

def test_reference_safety():
    original = [[1, 2], [3, 4]]
    matrix = create_matrix(original)
    matrix[0][0] = 99
    assert original[0][0] == 1

# Run using:
# pytest two_d_list_methods.py
