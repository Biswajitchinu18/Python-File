#selective dropdown

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
#
# driver = webdriver.Chrome()
#
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#
# select_locater = Select(driver.find_element(By.ID,'dropdown-class-example'))
# select_locater.select_by_index(1)
# select_locater.select_by_value('option2')
# select_locater.select_by_visible_text('Option1')
#
# select_locater.select_by_value('option2')
# time.sleep(3)


# driver.close()


#18min 6th may

#The difference between verification and assertion (imp interview question)


#Autoselective dropdown

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

input_box = driver.find_element(By.ID,'autocomplete')
input_box.send_keys('ind')

#values = driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li")

time.sleep(3)
ul_tag = driver.find_element(By.XPATH,"//ul[@id='ui-id-1']")
values = ul_tag.find_elements(By.XPATH,'li')

# print(len(values))
for value in values:
    if value.text == 'India':
        # print(value)
        # print(value.text)
        value.click()


time.sleep(2)
driver.close()

#screenshot............
