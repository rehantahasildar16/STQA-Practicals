from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


driver.get(r"file:///D:/STQA PRA 12.html")

driver.maximize_window()
time.sleep(10)



rows = driver.find_elements(By.XPATH, "//table[@id='studentTable']/tr")
columns = driver.find_elements(By.XPATH, "//table[@id='studentTable']/tr[1]/th")

print("Total Rows :", len(rows)-1)
print("Total Columns :", len(columns))

print("\nStudent Table Data\n")

for i in range(2, len(rows)+1):
    for j in range(1, len(columns)+1):

        value = driver.find_element(
            By.XPATH,
            "//table[@id='studentTable']/tr[" + str(i) + "]/td[" + str(j) + "]"
        ).text

        print(value, end="\t")

    print()



driver.find_element(By.XPATH, "//button[text()='Sort By Name']").click()

time.sleep(2)

names = driver.find_elements(By.XPATH,
"//table[@id='studentTable']/tr/td[1]")

actual = []

for name in names:
    actual.append(name.text)

expected = sorted(actual)

print("\nSorted Names")

for n in actual:
    print(n)

if actual == expected:
    print("\nSorting Validation Passed")
else:
    print("\nSorting Validation Failed")



search = driver.find_element(By.ID, "search")
search.send_keys("BCA")

driver.find_element(By.XPATH,
"//button[text()='Search']").click()

time.sleep(2)

courses = driver.find_elements(By.XPATH,
"//table[@id='studentTable']/tr/td[2]")

print("\nFiltered Results")

for course in courses:

    if course.is_displayed():

        print(course.text)

print("\nFilter Validation Successful")

time.sleep(10)

driver.quit()