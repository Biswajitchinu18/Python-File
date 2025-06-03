from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID,'openwindow').click()

#fetch the main windows

main_windows = driver.current_window_handle

all_windows = driver.window_handles

for i in all_windows:
    if i != main_windows:
        driver.switch_to.window(i)
        break

print(driver.title)


time.sleep(2)
driver.close()

driver.switch_to.window(main_windows)
print(driver.title)



driver.quit()


