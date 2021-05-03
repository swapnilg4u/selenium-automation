from selenium import webdriver
import time
from random_cred import *


#Enter details for testing inputs
name = ran_name
uname = user
mobile = mob
email = ranemail
password = c_password = "pass"

driver = webdriver.Chrome("C:/Users\\Swapnil\\Desktop\\selenium\\chromedriver.exe")
driver.maximize_window()
driver.get("http://localhost/home-rental")
time.sleep(2)



# -- Logging Out and Searching --

driver.find_element_by_xpath("//a[contains(text(),'Search')]").click()
time.sleep(1)
driver.find_element_by_id("keywords").send_keys("2BHK")
time.sleep(1)
driver.find_element_by_id("location").send_keys("mumbai")
time.sleep(1)
driver.find_element_by_id("other").send_keys("none")
time.sleep(1)
driver.find_element_by_xpath("//button[@id='']").click()
time.sleep(1)
driver.find_element_by_xpath("//h2[contains(text(),'List of Apartment Details')]").click()

time.sleep(5)
driver.close()
driver.quit()
print(" --  Testing completed  -- ")