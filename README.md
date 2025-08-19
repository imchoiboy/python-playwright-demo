[![Python Playwright Tests](https://github.com/imchoiboy/python-playwright-demo/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/matthewchoi66/playwrightPythonDemo/actions/workflows/tests.yml)

# Playwright Python Demo - TodoMVC

## Installation

1. Clone the repo:
```bash
git clone https://github.com/imchoiboy/python-playwright-demo.git
cd playwright-python-demo
```
2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
```
3. Install dependencies:
```bash
pip install -r requirements.txt
python -m playwright install --with-deps
```

## Running Tests
```bash
pytest --html=report.html --self-contained-html
```
