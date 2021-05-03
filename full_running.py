from selenium import webdriver
import time
from random_cred import *
import os

#Enter details for testing inputs
name = ran_name
uname = user
mobile = mob
email = ranemail
password = c_password = "pass"
"""
name = "swapnil"
uname = "swapnil"
mobile = 9753864211
email = "somemail@gmail.com"
password = c_password = "pass"
"""
print(" --  Full site testing starts here  -- ")
driver = webdriver.Chrome("C:/Users\\Swapnil\\Desktop\\selenium\\chromedriver.exe")
driver.maximize_window()
driver.get("http://localhost/home-rental")
time.sleep(2)
"""
exec(open('register.py').read())
exec(open('login.py').read())
exec(open('register_room.py').read())
exec(open('edit_room.py').read())
exec(open('search.py').read())"""

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

# -- Now we will edit registered data --
driver.find_element_by_xpath("//a[contains(text(),'Details/Update')]").click()
time.sleep(2)
driver.find_element_by_xpath("//body/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]").click()
time.sleep(2)
driver.find_element_by_id("rent").clear()
driver.find_element_by_id("rent").send_keys("16000")
time.sleep(1)
driver.find_element_by_id("other").send_keys("none")
time.sleep(1)
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
time.sleep(2)


# -- Logging Out and Searching --
driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
time.sleep(2)
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

time.sleep(15)
driver.close()
driver.quit()
print(" --  Testing completed  -- ")