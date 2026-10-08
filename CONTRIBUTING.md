# Contributing to wordtidy

Thanks for helping! Keep changes small and focused.

## Setup

```bash
git clone https://github.com/ZLouisMiguel/wordtidy
cd wordtidy
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Making a change

1. Create a branch: `git checkout -b my-change`
2. Source code goes in `src/wordtidy/`, tests in `tests/`.
3. Add or update tests for every behavior change, then run `pytest`.
4. Open a pull request explaining what changed and why.

## Guidelines

- Type hints and a short docstring on every public function.
- No third-party runtime dependencies.

## Reporting bugs

Open an issue with the code you ran, what you expected, what happened, and your Python version.

## Releasing (maintainers)

1. Bump the version in `pyproject.toml` and `src/wordtidy/__init__.py`.
2. `python -m build` then `python -m twine check dist/*`
3. TestPyPI first: `python -m twine upload --repository testpypi dist/*`
4. Verify in a clean virtualenv, then: `python -m twine upload dist/*`

Username is `__token__`, password is your API token. Never commit tokens.
