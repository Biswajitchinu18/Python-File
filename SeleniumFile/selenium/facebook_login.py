from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

name = driver.find_element(By.XPATH,"//input[@id='name']")
name.send_keys('Biswajit')
time.sleep(1)

email = driver.find_element(By.XPATH,"//input[@id='email']")
email.send_keys('biswajitchinu2@gmail.com')
time.sleep(1)

gender = driver.find_element(By.XPATH,"//input[@type='radio']")
gender.click()
time.sleep(1)

mobile_no = driver.find_element(By.XPATH,"//input[@id='mobile']")
mobile_no.send_keys('6370162096')
time.sleep(1)

dob = driver.find_element(By.XPATH,"//input[@id='dob']")
dob.send_keys('18-04-2001')
time.sleep(1)

subjects = driver.find_element(By.XPATH,"//input[@id='subjects']")
subjects.send_keys('Automation Testing')
time.sleep(1)

hobbies = driver.find_element(By.XPATH,"//input[@type='checkbox']")
hobbies.click()
time.sleep(1)

# picture = driver.find_element(By.XPATH,"//input[@type='file']")
# picture.click()

address = driver.find_element(By.XPATH,"//textarea[@id='picture']")
address.send_keys('Dist_kendrapara,Block_ Derabish')
time.sleep(1)

state = driver.find_element(By.XPATH,"//option[@value='Uttar Pradesh']").click()
time.sleep(1)

city = driver.find_element(By.XPATH,"//option[@value='Agra']").click()
time.sleep(1)

login = driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(3)


time.sleep(2)
driver.close()
