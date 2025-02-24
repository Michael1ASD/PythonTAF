#Tested page: https://www.saucedemo.com/


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
from selenium.webdriver.support.ui import Select


#SUPPORT
# WebDriverWait(sut, 10).until(EC.element_to_be_clickable(SUBPAGE_WAIT_CONDITIONS_BUTTON)).click()
# screenshot_file_path = 'screenshot.png'
# driver.save_screenshot(screenshot_file_path)

#SETUP
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (Linux)
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("enable-logging")
chrome_options.add_argument("v=1")
chrome_options.add_argument("--start-maximized")

# Enable logging to a specific log file
log_file_path = "chromedriver.log"  # Specify your desired log file name
chrome_options.add_argument(f"--log-path={log_file_path}")
chrome_options.add_argument("--log-level=ALL")  # Log levels: ALL, DEBUG, INFO, WARNING, SEVERE, OFF

#LOCATORS
BASE_URL = 'https://www.saucedemo.com/'
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
LEFT_MENU_BURGER_RESET_APP_STATUS_BUTTON = (By.XPATH, "//a[@id='reset_sidebar_link']")
SORT_PRODUCTS_DROPDOWN = (By.XPATH, "//select[@class='product_sort_container']")
FACEBOOK_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-facebook']")
X_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-twitter']")
LINKEDIN_LOGO_LOC = (By.XPATH, "//a[@data-test = 'social-linkedin']")

SORTING_METHODS_DICT = {"NAME ASC" : "Name (A to Z)", "NAME DESC" : "Name (Z to A)", "PRICE ASC" : "Price  (low to high)", "PRICE DESC" : "Price  (high to low)"}

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
driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)

#ACT
actual_title = driver.title

#ASSERT
assert actual_title == LOGIN_PAGE_TITLE_EXPECTED, f"Expected title '{LOGIN_PAGE_TITLE_EXPECTED}', but got '{actual_title}'"


#TEARDOWN
# sut.find_element(*LEFT_MENU_BURGER_CLOSE_BUTTON).click()
driver.quit()

# ********

#Test case 2: Successful login
#ARRANGE
driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)

#ACT
driver.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
driver.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
driver.find_element(*LOGIN_BUTTON_LOC).click()

#ASSERT
app_logo_actual = driver.find_element(*APP_LOGO_LOC)
assert app_logo_actual.text == APP_LOGO_EXPECTED, f"Expected logo '{APP_LOGO_EXPECTED}', but got '{app_logo_actual}'"


#TEARDOWN
# sut.find_element(*LEFT_MENU_BURGER_CLOSE_BUTTON).click()
driver.quit()

# ********

#Test case 3: Failed login
#ARRANGE
driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)

#ACT
driver.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
driver.find_element(*PASSWORD_FIELD_LOC).send_keys("Invalid password")
driver.find_element(*LOGIN_BUTTON_LOC).click()

#ASSERT
error_banner = driver.find_element(*ERROR_LOC)
assert error_banner.text == ERROR_WRONG_LOGIN_EXPECTED, f"Expected error '{ERROR_WRONG_LOGIN_EXPECTED}', but got '{error_banner.text}'"

#TEARDOWN
# sut.find_element(*LEFT_MENU_BURGER_CLOSE_BUTTON).click()
driver.quit()

# ********

#Test case 4: Check if cart is empty
#ARRANGE
driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)
driver.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
driver.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
driver.find_element(*LOGIN_BUTTON_LOC).click()

#ACT

#ASSERT
is_invisible = WebDriverWait(driver, 1).until(EC.invisibility_of_element_located(SHOPPING_CART_NUMBER_LOC))
assert is_invisible, f"Element {is_invisible} should not be visible!"


#TEARDOWN
# sut.find_element(*LEFT_MENU_BURGER_CLOSE_BUTTON).click()
driver.quit()

# ********

#Test case 5: Logout
#ARRANGE
driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)
driver.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
driver.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
driver.find_element(*LOGIN_BUTTON_LOC).click()

#ACT
driver.find_element(*LEFT_MENU_BURGER_OPEN_BUTTON).click()
WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
actual_title = driver.title

#ASSERT
assert actual_title == LOGIN_PAGE_TITLE_EXPECTED, f"Expected title '{LOGIN_PAGE_TITLE_EXPECTED}', but got '{actual_title}'"

# TEARDOWN
driver.quit()

# ********

#Test case 6: Add all (6) items to the cart
#ARRANGE
driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)
driver.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
driver.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
driver.find_element(*LOGIN_BUTTON_LOC).click()
time.sleep(3)

#ACT
add_to_cart_buttons = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_primary")))
for index in range(6):
    add_to_cart_buttons[index].click()
driver.find_element(*SHOPPING_CART_LOC).click()
inventory_count = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))))

#ASSERT
assert inventory_count == 6, f"Expected number of items is 6, but got '{inventory_count}'"

# TEARDOWN
driver.quit()


# ********

#Test case 7: Remove item from cart
#ARRANGE
driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)
driver.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
driver.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
driver.find_element(*LOGIN_BUTTON_LOC).click()

# ACT
add_to_cart_buttons = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_primary")))
add_to_cart_buttons[0].click()
driver.find_element(*SHOPPING_CART_LOC).click()
inventory_count = len(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))))
driver.find_element(By.CLASS_NAME, "cart_button").click()
is_invisible = WebDriverWait(driver, 1).until(EC.invisibility_of_element_located((By.XPATH, "//button[text()='Remove']")))

#ASSERT
assert is_invisible == True, f"Expected False, but got '{is_invisible}'"

# TEARDOWN
driver.quit()


# ********

#Test case 8: Sorting by price ascending
#ARRANGE
driver = webdriver.Chrome()
driver.get(BASE_URL)
driver.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
driver.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
driver.find_element(*LOGIN_BUTTON_LOC).click()

# ACT
sort_dropdown = driver.find_element(*SORT_PRODUCTS_DROPDOWN)
select = Select(sort_dropdown)
select.select_by_visible_text("Price (low to high)")
time.sleep(5)

items_to_order = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
price_list = []
cleaned_price_list = []

for price in items_to_order:
    price_list.append(price.text)
    cleaned_price_list = [float(price.replace('$', '')) for price in price_list]

# #ASSERT
assert cleaned_price_list[0] == min(cleaned_price_list), f"Expected minimum value is {min(cleaned_price_list)}, but got '{cleaned_price_list[0]}'"

# TEARDOWN
driver.quit()

# ********

#Test case 9: Sorting by name descending
#ARRANGE
driver = webdriver.Chrome()
driver.get(BASE_URL)
driver.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
driver.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
driver.find_element(*LOGIN_BUTTON_LOC).click()

# ACT
sort_dropdown = driver.find_element(*SORT_PRODUCTS_DROPDOWN)
select = Select(sort_dropdown)
select.select_by_visible_text("Name (Z to A)")

items_to_order = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
products_list = []

for product_name in items_to_order:
    products_list.append(product_name.text)

#ASSERT
assert products_list[0] == max(products_list), f"Expected first value is {max(products_list)}, but got '{products_list[0]}'"

# TEARDOWN
driver.quit()

# ********

#Test case 10: Social media links
#ARRANGE
driver = webdriver.Chrome()
driver.get(BASE_URL)
driver.find_element(*USERNAME_FIELD_LOC).send_keys(USERNAME_VALID)
driver.find_element(*PASSWORD_FIELD_LOC).send_keys(PASSWORD_VALID)
driver.find_element(*LOGIN_BUTTON_LOC).click()

# ACT
x_is_visible = WebDriverWait(driver, 1).until(EC.visibility_of_element_located(X_LOGO_LOC))
facebook_is_visible = WebDriverWait(driver, 1).until(EC.visibility_of_element_located(FACEBOOK_LOGO_LOC))
linkedin_is_visible = WebDriverWait(driver, 1).until(EC.visibility_of_element_located(LINKEDIN_LOGO_LOC))

#ASSERT
assert x_is_visible, f"Element {x_is_visible} should  be visible!"
assert facebook_is_visible, f"Element {facebook_is_visible} should  be visible!"
assert linkedin_is_visible, f"Element {linkedin_is_visible} should  be visible!"

# TEARDOWN
driver.quit()


