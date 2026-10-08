import pytest

from wordtidy import is_palindrome, slugify, squeeze_spaces, truncate, word_count


def test_slugify():
    assert slugify("  Hello, World! Café ") == "hello-world-cafe"


def test_word_count():
    assert word_count("one two  three") == 3
    assert word_count("") == 0


def test_truncate():
    assert truncate("hello world", 8) == "hello..."
    assert truncate("short", 10) == "short"
    with pytest.raises(ValueError):
        truncate("hello", 2)


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("hello")


def test_squeeze_spaces():
    assert squeeze_spaces("  a   b \n c ") == "a b c"