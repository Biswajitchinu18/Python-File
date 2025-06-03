from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

#switch frame

driver.switch_to.frame('courses-iframe')

time.sleep(3)

click_course = driver.find_element(By.LINK_TEXT,'Courses')
click_course.click()

time.sleep(2)

#switch to main frame
driver.switch_to.default_content()

driver.close()