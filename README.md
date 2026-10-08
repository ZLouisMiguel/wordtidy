# wordtidy

Small, dependency-free text helpers for Python 3.8+.

## Installation

```bash
pip install wordtidy
```

## Usage

```python
from wordtidy import slugify, word_count, truncate, is_palindrome, squeeze_spaces

slugify("Hello, World!")                 # "hello-world"
word_count("one two three")              # 3
truncate("hello world", 8)               # "hello..."
is_palindrome("A man, a plan, a canal: Panama")  # True
squeeze_spaces("  a   b  ")              # "a b"
```

## API

| Function                               | Description                                                                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `slugify(text)`                        | Lowercase, hyphen-separated, ASCII-only URL slug                                                 |
| `word_count(text)`                     | Number of whitespace-separated words                                                             |
| `truncate(text, length, suffix="...")` | Shorten to at most `length` characters; raises `ValueError` if `length` is shorter than `suffix` |
| `is_palindrome(text)`                  | Palindrome check, ignoring case and punctuation                                                  |
| `squeeze_spaces(text)`                 | Collapse repeated whitespace and trim ends                                                       |

## Development

```bash
pip install -e ".[dev]"
pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT, see [LICENSE](LICENSE).
