from playwright.sync_api import sync_playwright

def login_facebook(email,password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.facebook.com/login.php/')

        page.fill("//input[@id='email']",email)
        page.fill("//input[@id='pass']",password)

        page.click("//button[@id='loginbutton']")

        #screenshot
        page.screenshot(path='fblogin.png')

        page.wait_for_timeout(5000)
        browser.close()

login_facebook('biswajitchinu@2001','@2001')



#https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php - practice

