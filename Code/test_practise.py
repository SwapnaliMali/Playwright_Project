import pytest
from playwright.sync_api import Page,expect,sync_playwright

def test_practise():

    browser = sync_playwright().start().chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://app.noramoney.com/")

    #expect(page).to_have_title("noramoney")
