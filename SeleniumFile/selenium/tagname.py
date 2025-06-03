from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://www.flipkart.com/motorola-edge-60-pro-pantone-dazzling-blue-256-gb/p/itmbe844b03e063b?pid=MOBH9C9JNBGHUVS7&param=8768&otracker=clp_bannerads_1_3.bannerAdCard.BANNERADS_Motorola%2Bedge%2B60%2Bpro%2BPL-Sale%2BIs%2BLive_mobile-phones-store_8KWLVXIJQJ4C')

tags = driver.find_elements(By.TAG_NAME,'a')
print(len(tags))

#driver.quit()
#driver.close()

for i in tags:
    print(i.text)

