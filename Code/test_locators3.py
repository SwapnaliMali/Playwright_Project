import pytest

from playwright.sync_api import Page, expect, sync_playwright
import time
def test_func():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    Page = context.new_page()

    Page.goto("https://awesomeqa.com/pw/locators1.html")
    a = Page.title()
    print(a)


    Page.get_by_label("Subscribe").check()  #get_by_label inbuilt used here
    Page.get_by_role("button",name="Submit")

    expect(Page.get_by_role("listitem")).to_have_count(5)  #list items to capture & verify
    for row in Page.get_by_role("listitem").all():
        print(row.text_content())  # used to print the list items



    time.sleep(10)

