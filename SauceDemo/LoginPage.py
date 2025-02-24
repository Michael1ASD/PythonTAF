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

#SETUP
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (Linux)
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("enable-logging")
chrome_options.add_argument("v=1")

class LoginPage:

    def openLoginPageAndLogIn (self, url, username_loc, password_loc, login_button, username, password):
        sut = webdriver.Chrome(options=chrome_options)
        sut.get(url)
        sut.find_element(username_loc).send_keys(username)
        sut.find_element(password_loc).send_keys(password)
        sut.find_element(login_button).click()

if __name__ == "__main__":
    LoginPage.openLoginPageAndLogIn(BASE_URL, USERNAME_FIELD_LOC, PASSWORD_FIELD_LOC, LOGIN_BUTTON_LOC,USERNAME_VALID, PASSWORD_VALID)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class LoginPage:
    def __init__(self):
        chrome_options = Options()
        # Add any necessary Chrome options here
        self.driver = webdriver.Chrome(options=chrome_options)

    def openLoginPageAndLogIn(self, url, username_loc, password_loc, login_button, username, password):
        self.driver.get(url)
        self.driver.find_element(*username_loc).send_keys(username)
        self.driver.find_element(*password_loc).send_keys(password)
        self.driver.find_element(*login_button).click()

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    # Define the necessary constants
    BASE_URL = "https://example.com/login"
    USERNAME_FIELD_LOC = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_FIELD_LOC = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON_LOC = (By.XPATH, "//input[@id='login-button']")
    USERNAME_VALID = 'standard_user'
    PASSWORD_VALID = 'secret_sauce'

       # Create an instance of LoginPage
    login_page = LoginPage()

    # Call the method on the instance
    login_page.openLoginPageAndLogIn(BASE_URL, USERNAME_FIELD_LOC, PASSWORD_FIELD_LOC, LOGIN_BUTTON_LOC, USERNAME_VALID, PASSWORD_VALID)

    # Close the browser
    login_page.close()
