from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/dropdown")

driver.maximize_window()


dropdown = Select(driver.find_element(By.ID, "dropdown"))


items = dropdown.options


print("Total Items:", len(items))

print("\nDropdown Items:")
for item in items:
    print(item.text)

print("\nDefault Selected Items:")
print(dropdown.first_selected_option.text)

dropdown.select_by_visible_text("Option 1")
print("Selected:", dropdown.first_selected_option.text)

time.sleep(2)


dropdown.select_by_index(2)
print("Selected:", dropdown.first_selected_option.text)

time.sleep(2)

driver.quit()