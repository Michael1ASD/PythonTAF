#IMPORTS
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options

#SUPPORT
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SUBPAGE_WAIT_CONDITIONS_BUTTON)).click()
# screenshot_file_path = 'screenshot.png'
# driver.save_screenshot(screenshot_file_path)


#LOCATORS
BASE_URL = 'https://www.saucedemo.com/'


#SETUP
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (Linux)
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

#LOGIN_PAGE
#LOCATORS
USERNAME_FIELD_LOC = (By.XPATH, "//input[@id='user-name']")
PASSWORD_FIELD_LOC = (By.XPATH, "//input[@id='password']")
LOGIN_PAGE_BANNER_LOC = (By.XPATH, "//div[@class='login_logo']")
LOGIN_PAGE_TITLE_EXPECTED = 'Swag Labs'
LOGIN_BUTTON_LOC = (By.XPATH, "//input[@id='login-button']")
APP_LOGO_LOC = (By.XPATH, "//div[@class='app_logo']")
APP_LOGO_EXPECTED = 'Swag Labs'

#TEST DATA
# Accepted usernames are:
USERNAME_VALID = 'standard_user'
# locked_out_user
# problem_user
# performance_glitch_user
# error_user
# visual_user

# # Password for all users:
PASSWORD_VALID = 'secret_sauce'

# ********

#Test case 1: Login page is visible
#ARRANGE
sut = webdriver.Chrome(options=chrome_options)
sut.get(BASE_URL)

#ACT
sut.get(BASE_URL)
actual_title = sut.title

try:
    #ASSERT
    assert actual_title == LOGIN_PAGE_TITLE_EXPECTED, f"Expected title '{LOGIN_PAGE_TITLE_EXPECTED}', but got '{actual_title}'"

except Exception as e:
    print(f"An error occurred: {e}")

#TEARMDOWN
sut.quit()

# ********

#Test case 2: Successful login
#ARRANGE
sut = webdriver.Chrome(options=chrome_options)
sut.get(BASE_URL)

#ACT
sut.get(BASE_URL)
sut.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
sut.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
sut.find_element(*LOGIN_BUTTON_LOC).click()

try:
    #ASSERT
    app_logo_actual = sut.find_element(*APP_LOGO_LOC)
    assert app_logo_actual.text== APP_LOGO_EXPECTED, f"Expected logo '{APP_LOGO_EXPECTED}', but got '{app_logo_actual}'"

except Exception as e:
    print(f"An error occurred: {e}")

#TEARMDOWN
sut.quit()

# ********

# #Test case 3: Failed login
# #ARRANGE
# sut = webdriver.Chrome()
# sut.get(BASE_URL)
#
# #ACT
# sut.get(BASE_URL)
# sut.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
# sut.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
# sut.find_element(*LOGIN_BUTTON_LOC).click()
#
# try:
#     #ASSERT
#     app_logo_actual = sut.find_element(*APP_LOGO_LOC)
#     assert app_logo_actual.text== APP_LOGO_EXPECTED, f"Expected logo '{APP_LOGO_EXPECTED}', but got '{app_logo_actual}'"
#
# except Exception as e:
#     print(f"An error occurred: {e}")
#
# #TEARMDOWN
# sut.quit()