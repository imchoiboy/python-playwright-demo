import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config

@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = getattr(p, Config.BROWSER).launch(headless=Config.HEADLESS)
        context = browser.new_context(base_url=Config.BASE_URL)
        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(playwright_context):
    page = playwright_context.new_page()
    yield page
    page.close()
