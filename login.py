from selenium import webdriver
import time
from random_cred import *


#Enter details for testing inputs
name = "swapnil"
uname = "userswapnil"
mobile = "8697051423"
email = "mail@email.com"
password = c_password = "pass"

driver = webdriver.Chrome("C:/Users\\Swapnil\\Desktop\\selenium\\chromedriver.exe")
driver.maximize_window()
driver.get("http://localhost/home-rental")
time.sleep(2)


# -- Now we will login --
driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
time.sleep(2)
driver.find_element_by_id("exampleInputEmail1").send_keys(email)
time.sleep(1)
driver.find_element_by_id("exampleInputPassword1").send_keys(password)
time.sleep(1)
driver.find_element_by_name("login").click()
time.sleep(2)

time.sleep(5)
driver.close()
driver.quit()
print(" --  Testing completed  -- ")