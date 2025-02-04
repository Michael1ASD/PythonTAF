#IMPORTS
import time
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
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
ERROR_WRONG_LOGIN_EXPECTED = 'Epic sadface: Username and password do not match any user in this service'
ERROR_LOC = (By.CSS_SELECTOR, "h3[data-test='error']")
SHOPPING_CART_NUMBER_LOC = (By.XPATH, "//span[@class='shopping_cart_badge']")
LEFT_MENU_BURGER_OPEN_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
LEFT_MENU_BURGER_CLOSE_BUTTON = (By.XPATH, "//button[@id='react-burger-cross-btn']")
LOGOUT_BUTTON = (By.XPATH, "//a[@id='logout_sidebar_link']")
ALL_ITEMS_BUTTON = (By.XPATH, "//a[@id='inventory_sidebar_link']")
SHOPPING_CART_LOC = (By.XPATH, "//a[@class='shopping_cart_link']")


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
actual_title = sut.title

try:
    #ASSERT
    assert actual_title == LOGIN_PAGE_TITLE_EXPECTED, f"Expected title '{LOGIN_PAGE_TITLE_EXPECTED}', but got '{actual_title}'"

except Exception as e:
    print(f"An error occurred: {e}")

#TEARDOWN
# sut.find_element(*LEFT_MENU_BURGER_CLOSE_BUTTON).click()
sut.quit()

# ********

#Test case 2: Successful login
#ARRANGE
sut = webdriver.Chrome()
sut.get(BASE_URL)

#ACT
sut.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
sut.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
sut.find_element(*LOGIN_BUTTON_LOC).click()

try:
    #ASSERT
    app_logo_actual = sut.find_element(*APP_LOGO_LOC)
    assert app_logo_actual.text == APP_LOGO_EXPECTED, f"Expected logo '{APP_LOGO_EXPECTED}', but got '{app_logo_actual}'"

except Exception as e:
    print(f"An error occurred: {e}")

#TEARDOWN
# sut.find_element(*LEFT_MENU_BURGER_CLOSE_BUTTON).click()
sut.quit()

# ********

#Test case 3: Failed login
#ARRANGE
sut = webdriver.Chrome()
sut.get(BASE_URL)

#ACT
sut.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
sut.find_element(*PASSWORD_FIELD_LOC).send_keys("Invalid password")
sut.find_element(*LOGIN_BUTTON_LOC).click()

try:
    #ASSERT
    error_banner = sut.find_element(*ERROR_LOC)
    assert error_banner.text == ERROR_WRONG_LOGIN_EXPECTED, f"Expected error '{ERROR_WRONG_LOGIN_EXPECTED}', but got '{error_banner.text}'"

except Exception as e:
    print(f"An error occurred: {e}")

#TEARDOWN
# sut.find_element(*LEFT_MENU_BURGER_CLOSE_BUTTON).click()
sut.quit()

# ********

#Test case 4: Check if cart is empty
#ARRANGE
sut = webdriver.Chrome()
sut.get(BASE_URL)
sut.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
sut.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
sut.find_element(*LOGIN_BUTTON_LOC).click()

#ACT
try:
    #ASSERT
    is_invisible = WebDriverWait(sut, 1).until(EC.invisibility_of_element_located(SHOPPING_CART_NUMBER_LOC))
    assert is_invisible, f"Element {is_invisible} should not be visible!"

except Exception as e:
    print(f"An error occurred: {e}")

#TEARDOWN
# sut.find_element(*LEFT_MENU_BURGER_CLOSE_BUTTON).click()
sut.quit()

# ********

#Test case 5: Logout
#ARRANGE
sut = webdriver.Chrome()
sut.get(BASE_URL)
sut.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
sut.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
sut.find_element(*LOGIN_BUTTON_LOC).click()

#ACT
sut.find_element(*LEFT_MENU_BURGER_OPEN_BUTTON).click()
WebDriverWait(sut, 3).until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
actual_title = sut.title

try:
    #ASSERT
    assert actual_title == LOGIN_PAGE_TITLE_EXPECTED, f"Expected title '{LOGIN_PAGE_TITLE_EXPECTED}', but got '{actual_title}'"

except Exception as e:
    print(f"An error occurred: {e}")

# TEARDOWN
sut.quit()

# ********

#Test case 6: Add all (6) items to the cart
#ARRANGE
sut = webdriver.Chrome()
sut.get(BASE_URL)
sut.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
sut.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
sut.find_element(*LOGIN_BUTTON_LOC).click()
time.sleep(3)

#ACT
add_to_cart_buttons = WebDriverWait(sut, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_primary")))
for index in range(6):
    add_to_cart_buttons[index].click()
sut.find_element(*SHOPPING_CART_LOC).click()
inventory_count = len(WebDriverWait(sut, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))))

try:
    #ASSERT
    assert inventory_count == 6, f"Expected number of items is 6, but got '{inventory_count}'"

except Exception as e:
    print(f"An error occurred: {e}")

# TEARDOWN
sut.quit()

# ********

#Test case 7: Remove item from cart
#ARRANGE
sut = webdriver.Chrome()
sut.get(BASE_URL)
sut.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
sut.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
sut.find_element(*LOGIN_BUTTON_LOC).click()

# ACT
add_to_cart_buttons = WebDriverWait(sut, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"btn_primary")))
add_to_cart_buttons[0].click()
sut.find_element(*SHOPPING_CART_LOC).click()
inventory_count = len(WebDriverWait(sut, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))))
sut.find_element(By.CLASS_NAME, "cart_button").click()
is_invisible = WebDriverWait(sut, 1).until(EC.invisibility_of_element_located((By.XPATH, "//button[text()='Remove']")))

try:
    #ASSERT
    assert is_invisible == True, f"Expected False, but got '{is_invisible}'"

except Exception as e:
    print(f"An error occurred: {e}")

# TEARDOWN
sut.quit()


