
from selenium import webdriver
import time
from random_cred import *
import os

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



# -- Now we will register a new room --
image_path=os.path.abspath('.\\home.jpg')

driver.find_element_by_xpath("//a[contains(text(),'Register')]").click()
time.sleep(2)
driver.find_element_by_id("fullname").send_keys(name)
time.sleep(1)
driver.find_element_by_id("mobile").send_keys(mobile)
time.sleep(1)
driver.find_element_by_id("email").send_keys("not"+email)
time.sleep(1)
driver.find_element_by_id("plot_number").send_keys("32A")
time.sleep(0.5)
driver.find_element_by_id("rooms").send_keys("2BHK")
time.sleep(0.5)
driver.find_element_by_id("country").send_keys("India")
time.sleep(0.5)
driver.find_element_by_id("state").send_keys("MH")
time.sleep(0.5)
driver.find_element_by_id("city").send_keys("Mumbai")
time.sleep(0.5)
driver.find_element_by_id("rent").send_keys("14000")
time.sleep(0.5)
driver.find_element_by_id("deposit").send_keys("28000")
time.sleep(0.5)
driver.find_element_by_id("accommodation").send_keys("4")
time.sleep(0.5)
driver.find_element_by_id("landmark").send_keys("near atm")
time.sleep(0.5)
driver.find_element_by_id("description").send_keys("Nice place")
time.sleep(0.5)
driver.find_element_by_id("address").send_keys("Borivali")
time.sleep(0.5)
driver.find_element_by_id("image").clear()
driver.find_element_by_id("image").send_keys(image_path)
time.sleep(2)
driver.find_element_by_xpath("//body/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]").click()
time.sleep(2)

time.sleep(5)
driver.close()
driver.quit()
print(" --  Testing completed  -- ")