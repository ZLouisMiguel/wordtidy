"""wordtidy: small, dependency-free text helpers."""

from .core import is_palindrome, slugify, squeeze_spaces, truncate, word_count

__version__ = "0.1.0"
__all__ = ["slugify", "word_count", "truncate", "is_palindrome", "squeeze_spaces"]