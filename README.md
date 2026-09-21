Playwright & Python Test Automation Portfolio

An automated test suite demonstrating end-to-end (E2E) UI and REST API test coverage using Python, Playwright (Sync API), and Pytest.

🚀 Key Features

Page Object Model (POM): Scalable and maintainable UI test design pattern.

API Test Suite: Functional REST API validation (GET, POST, DELETE) with status code checks and data payload assertions.

Pytest Fixtures: Modular setup and teardown handling.

Reporting & Logging: Clean assertion logic with clear test execution status.

🛠️ Tech Stack

Language: Python 3.10+

UI Framework: Playwright

API Testing: Requests / Playwright API Context

Test Runner: Pytest

Pattern: Page Object Model (POM)

📁 Repository Structure

.
├── tests/
│   ├── test_ui.py          # E2E UI automated tests
│   └── test_api_suite.py   # Functional REST API test coverage
├── pages/                  # Page Object Model components
├── conftest.py             # Pytest fixtures and environment setup
├── requirements.txt        # Project dependencies
└── README.md               # Framework documentation


⚙️ Installation & Setup

Clone the repository:

git clone https://github.com/DrRafael/playwright-python-portfolio.git
cd playwright-python-portfolio


Create and activate virtual environment:

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


Install dependencies and Playwright browsers:

pip install -r requirements.txt
playwright install


🧪 Running Tests

Execute the full test suite:

pytest -v


Run API tests only:

pytest tests/test_api_suite.py


Run UI tests in headed mode:

pytest tests/test_ui.py --headed


Author: Rafael Tugushev — QA Automation Engineer
