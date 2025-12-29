import pytest
# string_methods_examples.py

# ---------------------------
# String Utility Functions
# ---------------------------

def is_empty(s: str) -> bool:
    """Check if string is empty"""
    return not s

def contains_substring(s: str, substring: str) -> bool:
    """Check if string contains a substring"""
    return substring in s

def starts_with(s: str, prefix: str) -> bool:
    """Check if string starts with prefix"""
    return s.startswith(prefix)

def ends_with(s: str, suffix: str) -> bool:
    """Check if string ends with suffix"""
    return s.endswith(suffix)

def is_upper(s: str) -> bool:
    """Check if all characters in string are uppercase"""
    return s.isupper()

def is_lower(s: str) -> bool:
    """Check if all characters in string are lowercase"""
    return s.islower()

def is_alpha(s: str) -> bool:
    """Check if string contains only alphabets"""
    return s.isalpha()

def is_digit(s: str) -> bool:
    """Check if string contains only digits"""
    return s.isdigit()

def is_alnum(s: str) -> bool:
    """Check if string contains only alphabets or numbers"""
    return s.isalnum()

def strip_spaces(s: str) -> str:
    """Remove leading and trailing spaces"""
    return s.strip()

def to_upper(s: str) -> str:
    """Convert string to uppercase"""
    return s.upper()

def to_lower(s: str) -> str:
    """Convert string to lowercase"""
    return s.lower()

def replace_substring(s: str, old: str, new: str) -> str:
    """Replace a substring with another"""
    return s.replace(old, new)

def split_string(s: str, delimiter: str = " ") -> list:
    """Split string by delimiter"""
    return s.split(delimiter)

def join_strings(strings: list, delimiter: str = " ") -> str:
    """Join a list of strings with delimiter"""
    return delimiter.join(strings)

# Accessing characters by index
def char_by_index(s: str, index: int) -> str:
    """Return character at a specific index. Supports negative indexing."""
    if -len(s) <= index < len(s):
        return s[index]
    return None

# ASCII conversions
def char_to_ascii(c: str) -> int:
    """Return ASCII code of a character"""
    return ord(c)

def ascii_to_char(code: int) -> str:
    """Return character corresponding to ASCII code"""
    return chr(code)

# String concatenation
def concat_strings(*args: str) -> str:
    """Combine multiple strings"""
    return "".join(args)

# Finding characters or substrings
def substring_exists(s: str, sub: str) -> bool:
    """Check if substring exists in string"""
    return sub in s

def index_of_substring(s: str, sub: str) -> int:
    """Return index of substring. Returns -1 if not found"""
    return s.find(sub)

# Slicing strings
def slice_string(s: str, start: int = None, end: int = None, step: int = None) -> str:
    """Extract part of string using slicing"""
    return s[start:end:step]

# Splitting and joining
def split_string(s: str, delimiter: str = " ") -> list:
    """Split string into list of substrings"""
    return s.split(delimiter)

def join_strings(strings: list, delimiter: str = " ") -> str:
    """Join a list of strings into a single string"""
    return delimiter.join(strings)

# Substring operations
def extract_substring(s: str, start: int, end: int) -> str:
    """Extract substring from start index to end index (exclusive)"""
    return s[start:end]

# Trimming strings
def trim_string(s: str) -> str:
    """Remove leading and trailing whitespaces"""
    return s.strip()



import pytest

def test_is_empty():
    assert is_empty("") is True
    assert is_empty("Hello") is False

def test_contains_substring():
    assert contains_substring("Hello World", "World") is True
    assert contains_substring("Hello World", "world") is False

def test_starts_with():
    assert starts_with("Hello World", "Hello") is True
    assert starts_with("Hello World", "World") is False

def test_ends_with():
    assert ends_with("Hello World", "World") is True
    assert ends_with("Hello World", "Hello") is False

def test_is_upper():
    assert is_upper("HELLO") is True
    assert is_upper("Hello") is False

def test_is_lower():
    assert is_lower("hello") is True
    assert is_lower("Hello") is False

def test_is_alpha():
    assert is_alpha("Hello") is True
    assert is_alpha("Hello123") is False

def test_is_digit():
    assert is_digit("12345") is True
    assert is_digit("123abc") is False

def test_is_alnum():
    assert is_alnum("Hello123") is True
    assert is_alnum("Hello 123") is False

def test_strip_spaces():
    assert strip_spaces("  hello  ") == "hello"
    assert strip_spaces("world") == "world"

def test_to_upper():
    assert to_upper("hello") == "HELLO"

def test_to_lower():
    assert to_lower("HELLO") == "hello"

def test_replace_substring():
    assert replace_substring("Hello World", "World", "Python") == "Hello Python"

def test_split_string():
    assert split_string("Hello World") == ["Hello", "World"]
    assert split_string("a,b,c", ",") == ["a", "b", "c"]

def test_join_strings():
    assert join_strings(["Hello", "World"]) == "Hello World"
    assert join_strings(["a","b","c"], ",") == "a,b,c"

def test_char_by_index():
    s = "Python"
    assert char_by_index(s, 0) == "P"
    assert char_by_index(s, -1) == "n"
    assert char_by_index(s, 6) is None

def test_ascii_conversions():
    assert char_to_ascii("A") == 65
    assert ascii_to_char(65) == "A"

def test_concat_strings():
    assert concat_strings("Hello", " ", "World") == "Hello World"

def test_substring_exists():
    s = "Hello World"
    assert substring_exists(s, "World") is True
    assert substring_exists(s, "Python") is False

def test_index_of_substring():
    s = "Hello World"
    assert index_of_substring(s, "World") == 6
    assert index_of_substring(s, "Python") == -1

def test_slice_string():
    s = "Python"
    assert slice_string(s, 0, 4) == "Pyth"
    assert slice_string(s, -3, None) == "hon"
    assert slice_string(s, 0, 6, 2) == "Pto"

def test_split_and_join():
    s = "a,b,c"
    lst = split_string(s, ",")
    assert lst == ["a", "b", "c"]
    assert join_strings(lst, "-") == "a-b-c"

def test_extract_substring():
    s = "Hello World"
    assert extract_substring(s, 0, 5) == "Hello"

def test_trim_string():
    s = "   hello   "
    assert trim_string(s) == "hello"

# Run tests with:
# pytest string_advanced_examples.py