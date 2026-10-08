"""Core text helper functions for wordtidy."""

import re
import unicodedata


def slugify(text: str) -> str:
    """Turn text into a lowercase, hyphen-separated URL slug."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def word_count(text: str) -> int:
    """Count the words in text."""
    return len(text.split())


def truncate(text: str, length: int, suffix: str = "...") -> str:
    """Shorten text to at most ``length`` characters, ending with ``suffix``."""
    if length < len(suffix):
        raise ValueError("length must be at least the length of suffix")
    if len(text) <= length:
        return text
    return text[: length - len(suffix)].rstrip() + suffix


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same backwards, ignoring case and punctuation."""
    cleaned = [c.lower() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]


def squeeze_spaces(text: str) -> str:
    """Collapse runs of whitespace into single spaces and trim the ends."""
    return " ".join(text.split())
