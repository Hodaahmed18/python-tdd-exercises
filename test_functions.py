from functions import *


def test_is_even():
    assert is_even(4) == True


def test_get_initials():
    assert get_initials("John Smith") == "JS"


def test_count_vowels():
    assert count_vowels("hello") == 2


def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5]) == [2, 4]


def test_is_palindrome():
    assert is_palindrome("level") == True
