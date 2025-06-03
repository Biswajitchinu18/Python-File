from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.facebook.com/')

#interact with a hyperlink

driver.find_element(By.PARTIAL_LINK_TEXT,'Forgotten password?').click()

time.sleep(4)
driver.close()

#https://rahulshettyacademy.com/AutomationPractice/
