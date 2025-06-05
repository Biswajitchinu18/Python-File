#lunching browser : chromium,firefox and webkit

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #chromium
    browser = p.chromium.launch(headless=False)

    #firefox

    #browser = p.firefox.launch(headless=False)

    #webkit

    #browser = p.webkit.launch(headless=False)

    #opening a new context and page
    context = browser.new_context()

    #new Page
    page = context.new_page()



    browser.close()








