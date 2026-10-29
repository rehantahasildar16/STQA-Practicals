from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()

driver.get(r"file:///D:/STQA PRAC 13.html")

driver.maximize_window()

time.sleep(5)

# Upload File

filepath = r"C:\Users\DESKTOP\Downloads\logisim-win-2.7.1 (3).exe"

driver.find_element(By.ID,"file").send_keys(filepath)

time.sleep(5)

driver.find_element(By.XPATH,"//button[text()='Upload']").click()

time.sleep(5)

message = driver.find_element(By.ID,"msg").text

print("Upload Status :",message)

# Download File

driver.find_element(By.XPATH,"//button[text()='Download']").click()

print("Downloading File...")

time.sleep(10)

download_path = r"C:\Users\DESKTOP\Downloads\sample.txt"

if os.path.exists(download_path):

    print("Download Successful")

else:

    print("Download Failed")

time.sleep(5)

driver.quit()