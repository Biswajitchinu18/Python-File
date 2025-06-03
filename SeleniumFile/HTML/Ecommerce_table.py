from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import json


driver = webdriver.Chrome()

file_path = os.path.abspath('E_commerce.html')

driver.get(file_path)

'''json file handel in test data activities'''

'''with open('test_data.json','r') as file:
    data = file.read()
    expected_result = json.loads(data)

print(expected_result)'''


# total row count of the table

'''actual_total_rows = driver.find_elements(By.XPATH,'//tbody/tr')
# print(len(actual_total_rows))
assert expected_result['row_counts'] == len(actual_total_rows)'''


time.sleep(3)

#how many product buy an indivisual customer and price,product name,& provide the product name

'''Category = 'Beauty'
Products = driver.find_elements(By.XPATH,f"//tr/td[text()='{Category}']/following-sibling::td[3]")
# print(len(Products))
products_name = [i.text for i in Products]
print(products_name)
print(Products)'''



#price

'''price = driver.find_elements(By.XPATH,f"//tr/td[text()='{Category}']/following-sibling::td[2]")

all_price_list = [eval(i.text) for i in price]
print(sum(all_price_list))'''

#check stocks between 1st 15 days and last 15 days, compair them.

stocks = driver.find_elements(By.XPATH,'//tr/td[5]')
for i in stocks:
    sts = int(i.text)



driver.close()