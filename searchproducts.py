from selenium.webdriver.common.action_chains import  ActionChains

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://magento.com/products/magento-open-source")

time.sleep(10)
ActionChains(driver).move_to_element(driver.find_element_by_css_selector("a[href='/search/']")).perform()
print('ok')
time.sleep(3)
search_field = driver.find_element_by_css_selector("input[class='form-search']")
print('ok')
search_field.send_keys('phone')
search_field.submit()

