from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser =p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

    page.fill("//input[@id='name']",'Biswajit Chinu')
    page.fill("//input[@id='email']",'cb18@gmail.com')
    page.click("//input[@id='gender']")
    page.fill("//input[@id='mobile']",'6370162096')
    page.fill("//input[@id='dob']",'2001-04-18')
    page.fill("//input[@id='subjects']",'Automation Testing')
    page.click("//input[@id='hobbies']")
    #page.click("//*[id='practiceForm']/div[7]/div/div/div[2]/input")
    page.fill("//textarea[@id='picture']",'Bhubaneswar,Kendrapara')




    page.wait_for_timeout(5000)
    browser.close()