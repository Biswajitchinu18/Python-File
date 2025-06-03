# from selenium import webdriver
# import time
#
#
# driver = webdriver.Chrome()
# driver.get("https://jqueryui.com/resizable/")
# driver.maximize_window()
#
# time.sleep(2)
#
# #scrolldown using js
#
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#
# #screenshot
#
# driver.save_screenshot("screenshot1.png")
#
#
# time.sleep(3)
# driver.close()




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()

driver.implicitly_wait(5)

time.sleep(2)

iframe = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(iframe)

wait = WebDriverWait(driver,15)

source = wait.until(EC.presence_of_element_located((By.ID,'draggable')))
target = wait.until(EC.presence_of_element_located((By.ID,'droppable')))

actions = ActionChains(driver)
actions.drag_and_drop(source,target).perform()


time.sleep(3)
driver.close()