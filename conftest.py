import pytest

from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function", autouse=False)
def driver():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()  
    playwright.stop()
