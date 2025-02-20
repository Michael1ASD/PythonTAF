import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SUBPAGE_WAIT_CONDITIONS_BUTTON)).click()
# screenshot_file_path = 'screenshot.png'
# driver.save_screenshot(screenshot_file_path)

# LOCATORS
BASE_URL = 'https://play1.automationcamp.ir/'
SUBPAGE_WAIT_CONDITIONS_BUTTON = (By.XPATH, '//a[@href="expected_conditions.html"]')

# TEST CASE 1 - Wait for alert to be present
#ARRANGE
driver = webdriver.Chrome()
driver.get(BASE_URL)
driver.find_element(*SUBPAGE_WAIT_CONDITIONS_BUTTON).click()

#ACT
driver.find_element(By.XPATH, "//button[@id='alert_trigger']").click()
WebDriverWait(driver, 5).until(EC.alert_is_present())
Alert(driver).accept()
alert_handled = driver.find_element(By.XPATH, "//span[@id='alert_handled_badge']")
print(alert_handled)
#ASSERT
assert EC.visibility_of_element_located(alert_handled)

#TEARDOWN
# driver.close()

