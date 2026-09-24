import pytest
from playwright.sync_api import Page, expect

def test_login_success(page: Page):
    """Verify successful user authentication flow."""
    page.goto("https://the-internet.herokuapp.com/login")
    
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")

def test_dynamic_loading(page: Page):
    """Verify handling of dynamically loaded web elements with auto-waiting."""
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    
    page.click("div#start button")
    finish_element = page.locator("div#finish h4")
    
    expect(finish_element).to_be_visible(timeout=10000)
    expect(finish_element).to_have_text("Hello World!")
