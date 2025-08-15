from playwright.sync_api import Page

def test_basic_navigation(page: Page):
    page.goto("https://playwright.dev/")
    assert "Playwright" in page.title()
