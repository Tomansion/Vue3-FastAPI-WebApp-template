# Pytest unit tests

## Run

```bash
pip install coverage pytest pytest-cov
pytest --cov-report term --cov=. --cov-report=html -sx
```

## Coverage analysis

```bash
firefox htmlcov/index.html
```
