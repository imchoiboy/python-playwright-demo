import os
import pytest
from playwright.sync_api import sync_playwright
from pages.todo_page import TodoPage
from utils.config import Config

@pytest.fixture(scope="session")
def playwright_instance():
    """Start Playwright once per test session."""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    """Launch browser once per session."""
    headless = Config.HEADLESS
    # Allow overriding with environment variable
    headless_env = os.getenv("HEADLESS")
    if headless_env is not None:
        headless = headless_env.lower() == "true"

    browser_type = getattr(playwright_instance, Config.BROWSER)
    browser = browser_type.launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    """Create a new browser context for each test (fresh cookies, storage, etc)."""
    context = browser.new_context(base_url=Config.BASE_URL)
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """Provide a fresh page for each test."""
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def todo_page(page) -> TodoPage:
    """Return a TodoPage object with a fresh page instance."""
    todo_page = TodoPage(page)
    todo_page.navigate()
    return todo_page
