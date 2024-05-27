import pytest
from playwright.sync_api import sync_playwright,expect,Page

def test_locators():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    Page = context.new_page()

    Page.goto("https://superadmin.noramoney.com/")
    Page.title()
    Page.wait_for_load_state("networkidle")
    Page.locator("#phone").fill("937386810")

