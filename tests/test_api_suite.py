import pytest
from playwright.sync_api import APIRequestContext

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts(api_context: APIRequestContext):
    """Verify successful retrieval of posts list (GET request)."""
    response = api_context.get(f"{BASE_URL}/posts")
    assert response.status == 200
    assert len(response.json()) > 0

def test_create_post(api_context: APIRequestContext):
    """Verify creation of a new post resource (POST request)."""
    payload = {
        "title": "QA Automation Test",
        "body": "Testing Playwright API Context",
        "userId": 1
    }
    response = api_context.post(f"{BASE_URL}/posts", data=payload)
    assert response.status in (200, 201)
    assert response.json()["title"] == payload["title"]

def test_delete_post(api_context: APIRequestContext):
    """Verify deletion of a post resource (DELETE request)."""
    response = api_context.delete(f"{BASE_URL}/posts/1")
    assert response.status == 200
