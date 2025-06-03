from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

url = 'https://www.facebook.com/r.php?entry_point=login'
driver.get(url)

first_name = driver.find_element(By.NAME,'firstname')
first_name.send_keys('Chinu')

sure_name = driver.find_element(By.NAME,'lastname')
sure_name.send_keys('Biswajit')

male = driver.find_element(By.XPATH,'//div/span/span[2]/label/input').click()


time.sleep(3)
driver.quit()