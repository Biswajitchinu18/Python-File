from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ecs
import time

driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

driver.implicitly_wait(3)

search_field = driver.find_element(By.XPATH,"//input[@type='search']")
search_field.send_keys('er')


time.sleep(3)
result =driver.find_elements(By.XPATH,"//div[@class='products']/div//button")

for i in result:
    i.click()

cart_image_click = driver.find_element(By.XPATH,"//img[@alt='Cart']").click()

checkout = driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

text = driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys('done')

apply = driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()

# code = driver.find_element(By.XPATH,"//span[@class='promoInfo']")
# print(code.text)

wait = WebDriverWait(driver,15)
wait.until(Ecs.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))


time.sleep(3)
driver.close()