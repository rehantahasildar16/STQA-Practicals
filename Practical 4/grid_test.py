from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
driver = webdriver.Remote(
   command_executor="http://192.168.1.200:4444",
   options=options
)
driver.get("https://www.google.com")
print("Page Title:", driver.title)
driver.quit()
