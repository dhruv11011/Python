# Opening a webpage and locating the elements

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.python.org/")


# Locate an element by ID
# element_by_id = driver.find_element_by_id("element_id")
element_by_id=driver.find_element(By.ID,"id-search-field")
print(element_by_id)

# Locate an element by class name
element_by_class= driver.find_element(By.CLASS_NAME,"main-header")
print(element_by_class)
# Locate an element by tag name
element_by_tag=driver.find_element(By.TAG_NAME,"h1")
# Go back to the previous page
driver.back()
time.sleep(5)
# Go forward
driver.forward()

#CLose the Browser
driver.close()
# driver.quit()

# =======================================================================================

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")
# driver.get("https://www.tutorialspoint.com/javascript/javascript_dialog_boxes.htm")
# Locate the dropdown element
button = driver.find_element(By.TAG_NAME, "button")
# button = driver.find_element(By.CSS_SELECTOR,'input[type="submit"][value="Click Me"]')
time.sleep(2)
button.click()  # Clicks on the located button element

# Switch to the alert
alert = driver.switch_to.alert
time.sleep(2)
# Simulates 'OK' and Accepts the alert dialog, and then dismisses the alert.
alert.accept()
# alert.dismiss() is used to simulate 'Cancel'
time.sleep(2)
