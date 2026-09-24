import pytest
from playwright.sync_api import playwright, APIRequestContext

@pytest.fixture(scope="session")
def api_context() -> APIRequestContext:
    """Fixture to create Playwright API request context for the test session."""
    with playwright() as p:
        request_context = p.request.new_context()
        yield request_context
        request_context.dispose()