#Loop Concepts in Python for Lists and Dictionaries
# List
""" 
#1 Basic for loop (most common)
    for item in lst:
        ...

    * Reads values directly
    * Cleanest
    * Preferred in 90% cases

    Use when:
    * we don’t need index

#2 Loop with index using range()

    for i in range(len(lst)):
        item = lst[i]

    * Index-based access
    * More error-prone
    * Needed only when index matters

#3 Loop with index + value using enumerate()

    for index, value in enumerate(lst):
        ...

    * Best of both worlds
    * Pythonic
    * Highly recommended

#4 While loop

    i = 0
    while i < len(lst):
        item = lst[i]
        i += 1

    * Manual control
    * Rarely needed
    * Used in custom iteration logic

#5 Reverse loop

    for item in reversed(lst):
        ...
    Or:

    for i in range(len(lst) - 1, -1, -1):
        ...

#6 Loop with condition (filtering)

    for item in lst:
        if item > 15:
            ...

#7 Nested loop (2D list)

    for row in matrix:
        for cell in row:
            ...

    Used for:
    * Tables
    * Grids
    * Matrices
"""

# Dictionary
""" 
Ways to loop a DICTIONARY
Assume:
    data = {"a": 1, "b": 2}

#1 Loop over keys (default behavior)

    for key in data:
        value = data[key]

    Equivalent to:
        for key in data.keys():

#2 Loop over values

    for value in data.values():
        ...
    Use when:
    * Key doesn’t matter

#3 Loop over key-value pairs (most important)

    for key, value in data.items():
        ...
    This is the most common and recommended.

#4 Loop with condition

    for key, value in data.items():
        if value > 1:
            ...

#5 Nested dictionary loops

    for key, inner_dict in data.items():
        for inner_key, inner_value in inner_dict.items():
            ...

    Used in:
    * JSON
    * API payloads
    * Config trees

4. Loop control statements (deep understanding)
    break
      * Stops loop completely
    continue
      * Skips current iteration
    else with loop (very Python-specific)

    for item in lst:
        if item == 99:
            break
    else:
        # runs only if loop was NOT broken

    This is not if-else.

5. Modifying data while looping (danger zone)
    Don’t do this

    for item in lst:
        lst.remove(item)

    Why:
    * we’re changing the iterable while iterating
    
    Safe patterns
    * Loop over a copy
    * Build a new list

"""