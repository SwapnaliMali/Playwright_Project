import pytest
from playwright.sync_api import expect, Page, sync_playwright


def test_locators():
    browser = sync_playwright().start().chromium.launch(headless = False)
    context = browser.new_context()
    Page = context.new_page()

    Page.goto("https://app.vwo.com/#/login") #navigate to this url. Step1
    Page.title() # to fetch the title of page

    Page.wait_for_load_state("networkidle") # Step2.  networkidle : means html, images, api everything is loaded

    Page.locator("#login-username").fill("admin") #Step 3, locate the fields. # used first means fetching by id, so add # when by id
    Page.locator("#login-password").fill("password")
    Page.locator("#js-login-btn").click()

    #Verify the error message
    error_message = Page.locator("#js-notification-box") #firstly locate the message box
    expect(error_message).to_have_text("Your email, password, IP address or location did not match")
    #playwright provides "expect" to validate, similar to assert in pytest, which also can be used here.


    #dispose context once no longer used
    context.close()





