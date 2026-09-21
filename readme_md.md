# Playwright & Python Test Automation Portfolio

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-green.svg)](https://playwright.dev/python/)
[![Pytest](https://img.shields.io/badge/Pytest-8.0%2B-red.svg)](https://docs.pytest.org/)

An automated test suite demonstrating end-to-end (E2E) UI and REST API test coverage using **Python**, **Playwright (Sync API)**, and **Pytest**.

## 🚀 Key Features

- **Page Object Model (POM)**: Scalable and maintainable UI test design pattern.
- **API Test Suite**: Functional REST API validation (GET, POST, DELETE) with status code checks and data payload assertions.
- **Pytest Fixtures**: Modular setup and teardown handling.
- **Reporting & Logging**: Clean assertion logic with clear test execution status.

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **UI Framework**: Playwright
- **API Testing**: Requests / Playwright API Context
- **Test Runner**: Pytest
- **Pattern**: Page Object Model (POM)

## 📁 Repository Structure

```text
.
├── tests/
│   ├── test_ui.py          # E2E UI automated tests
│   └── test_api_suite.py   # Functional REST API test coverage
├── pages/                  # Page Object Model components
├── conftest.py             # Pytest fixtures and environment setup
├── requirements.txt        # Project dependencies
└── README.md               # Framework documentation
```

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DrRafael/playwright-python-portfolio.git
   cd playwright-python-portfolio
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies and Playwright browsers**:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## 🧪 Running Tests

Execute the full test suite:
```bash
pytest -v
```

Run API tests only:
```bash
pytest tests/test_api_suite.py
```

Run UI tests in headed mode:
```bash
pytest tests/test_ui.py --headed
```

---
**Author**: [Rafael Tugushev](https://github.com/DrRafael) — QA Automation Engineer