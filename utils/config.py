import os

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://demo.playwright.dev/todomvc/")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    BROWSER = os.getenv("BROWSER", "chromium")  # chromium, firefox, webkit
