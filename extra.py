from selenium import webdriver
import time
from random_cred import *

#Enter details for testing inputs
name = "swapnil"
uname = "admin"
mobile = 9847586923
email = "admin@admin.com"
password = c_password = "admin"

print(" --  Admin testing starts here  -- ")
driver = webdriver.Chrome("C:/Users\\Swapnil\\Desktop\\selenium\\chromedriver.exe")
driver.maximize_window()
driver.get("http://localhost/home-rental")
time.sleep(2)

driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
time.sleep(2)
driver.find_element_by_id("exampleInputEmail1").send_keys(email)
time.sleep(1)
driver.find_element_by_id("exampleInputPassword1").send_keys(password)
time.sleep(1)
driver.find_element_by_name("login").click()
time.sleep(2)

