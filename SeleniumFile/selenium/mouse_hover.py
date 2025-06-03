from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')


hover_element = driver.find_element(By.ID,'mousehover')

action = ActionChains(driver)

time.sleep(3)
action.move_to_element(hover_element).perform()
time.sleep(2)

driver.find_element(By.XPATH,"//a[text()='Top']").click()

time.sleep(2)

driver.close()
