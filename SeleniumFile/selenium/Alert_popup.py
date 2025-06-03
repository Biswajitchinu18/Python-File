from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#ALERT
'''
name = driver.find_element(By.ID,'name')
name.send_keys('Biswajit')
alert_button = driver.find_element(By.ID,'alertbtn').click()
time.sleep(2)
alert = Alert(driver)
alert.accept()
'''

#POPUP
'''
name = driver.find_element(By.ID,'name')
name.send_keys('Biswajit')
pop_button = driver.find_element(By.ID,'confirmbtn').click()
time.sleep(2)
alert = Alert(driver)

text_from_alert = alert.text
print(text_from_alert)
# alert.accept()
alert.dismiss()
'''


time.sleep(3)

driver.close()
