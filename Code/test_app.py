import pytest

from playwright.sync_api import Page,expect,sync_playwright
#page, expect are classes
#page --> helps to interact with browser
#expect --> helps to validate the message expected. Result = Actual result


def test_app():
    #Browser & page
    browser = sync_playwright().start().chromium.launch(headless=False) #browser : create new variable to store
    page = browser.new_page() #a browser can have multiple pages, we created one page here.

    #Code interaction with HTML  web page
    page.goto("https://superadmin.noramoney.com/") #goto is used to redirect to url. #codegen is used to generate code based on UI navigation done.
    breakpoint()
    #validations
    expect(page).to_have_title("NORAWALLET SUPER ADMIN")


    #debugging in playwright - simple, just add breakpoint() and debugger will open into which u can
    # provide inputs & get respective page output.
    # You can use expect statements in debugger as well, also page.title() etc.
    # You can either add PWDEBUG=1 in terminal while esecuting code /
    # debug configuration varible in pycharm due to this, pw inspector will open & u can debug at each line of code
    # This is an exceptional feature in playwright

    #browser --> chromium / webkit
    #



