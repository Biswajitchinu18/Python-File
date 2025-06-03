from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#get - hit the url
driver.get('https://www.facebook.com/')

email = driver.find_element(By.ID,'email')
email.send_keys('cb@gmail.com')

password = driver.find_element(By.ID,'pass')
password.send_keys('cb18@2001')

submit = driver.find_element(By.ID,'login')
submit.click()

time.sleep(5)
driver.quit()
