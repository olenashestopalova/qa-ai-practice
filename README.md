# qa-ai-practice

A small API test automation portfolio project, built to practice API testing with
Python, pytest, and requests, and to practice working with AI coding agents.

## Target API

[DummyJSON](https://dummyjson.com) — a free, public REST API that requires no API key.

## Setup

```bash
pip install -r requirements.txt
```

## Run tests

```bash
pytest
```
## Current coverage

- GET /products/{id}
- Positive and negative product ID scenarios
- Boundary value checks
- Basic response validation