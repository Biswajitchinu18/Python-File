from playwright.sync_api import sync_playwright


#with automatically open the file and close the file
with sync_playwright() as p:
    print(dir(p))
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #navigate to the web page

    page.goto('https://www.youtube.com/')

    page.pause()

    browser.close()