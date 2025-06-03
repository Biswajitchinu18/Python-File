from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

file_path = os.path.abspath('First.html')

driver.get(file_path)

expected_res = 3

thead = driver.find_elements(By.XPATH,'//thead/tr/th')

marks_index = 1
for i in thead:
    if i.text == 'Marks':
        break
    marks_index = marks_index+1
print(marks_index)

marks = driver.find_elements(By.XPATH,f"//tbody/tr/td[{marks_index}]")
total_sum = 0


for mark in marks:
    total_sum = total_sum + int(mark.text)
print(total_sum)


count_candidates = driver.find_elements(By.XPATH,'//tbody//tr/td[1]')
actual_res = len(count_candidates)

# assert expected_res == actual_res,'failed due to count mismatch'

if expected_res == actual_res:
    print('pass')

time.sleep(3)
driver.close()


