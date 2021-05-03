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


# -- This code block is for registering user --
driver.find_element_by_xpath("//a[contains(text(),'Register')]").click()
time.sleep(2)
driver.find_element_by_id("fullname").send_keys(name)
time.sleep(1)
driver.find_element_by_id("username").send_keys(uname)
time.sleep(1)
driver.find_element_by_id("mobile").send_keys(mobile)
time.sleep(1)
driver.find_element_by_id("email").send_keys(email)
time.sleep(1)
driver.find_element_by_id("password").send_keys(password)
time.sleep(1)
driver.find_element_by_id("c_password").send_keys(c_password)
time.sleep(1)
driver.find_element_by_name("register").click()
time.sleep(2)

time.sleep(5)
driver.close()
driver.quit()
print(" --  Testing completed  -- ")