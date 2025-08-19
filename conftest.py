import pytest
from playwright.sync_api import sync_playwright
from pages.todo_page import TodoPage

@pytest.fixture(scope="session")
def browser():
    """Launch browser once per test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # set False for debugging
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    """Fresh page for each test (new context)."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def todo_page(page):
    """Todo Page object with navigation already done."""
    todo = TodoPage(page)
    todo.navigate()
    return todo
