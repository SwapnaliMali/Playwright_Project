import pytest
from playwright.sync_api import expect,Page,sync_playwright

def test_context():
    browser = sync_playwright().start().chromium.launch(headless=False)

    context = browser.new_context()
    context1 = browser.new_context()

    page1 = context.new_page()
    page2 = context1.new_page()

    page1.goto("https://superadmin.noramoney.com/")
    page2.goto("https://www.noramoney.com/")


"""
Browser —> rendering engine : Browser [ chromium / webkit ]
Context → Window [ 1 / 2 multiple windows of 1 browser ]
Page → Tabs in context [ 1 browser -> 1 context → 1 tab ]


"""


