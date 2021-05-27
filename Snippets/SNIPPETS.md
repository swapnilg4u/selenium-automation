<h2>Selenium Code Snippets</h2>
I'm making this a markdown file so that you can copy the specific snippets line by line to learn what each of them do.

### Basic Program

```
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox 
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("YOUR EMAILID")
password.send_keys("YOUR PASSWORD")
# Step 4) Click Login
submit.click()
wait = WebDriverWait( browser, 5 )
page_title = browser.title
assert page_title == "Facebook"
```

### Basic program to run selenium remotely

```
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://youtube.com")
```

### Give fake agent requests to avoid Captcha

```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\ChromeDriver\chromedriver_win32\chromedriver.exe')
driver.get("https://www.google.co.in")
driver.quit()
```
