import time
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

# TEST CASE 1
#SETUP
driver = webdriver.Chrome()
driver.get(BASE_URL)

#TEST
driver.find_element(*SUBPAGE_WAIT_CONDITIONS_BUTTON).click()
time.sleep(5)

#TEARDOWN
driver.close()

