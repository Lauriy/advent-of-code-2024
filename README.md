# AoC 2024

# Setup
```shell
python3.12 -m venv .venv
source .venv/bin/activate  # . .\.venv\Scripts\activate on Windows
pip install --upgrade setuptools pip wheel uv
uv sync
```

# Tests (get answers)

```shell
uv run pytest # -n 8 or smth to run the whole suite faster
```

# Linting
```shell
ruff format .
ruff check --fix --unsafe-fixes .
```

# Previous years

- https://github.com/Lauriy/advent-of-code-2018
- https://github.com/Lauriy/advent-of-code-2020
- https://github.com/Lauriy/advent-of-code-2021
- https://github.com/Lauriy/advent-of-code-2022