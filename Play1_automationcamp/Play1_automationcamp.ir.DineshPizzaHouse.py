import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SUBPAGE_WAIT_CONDITIONS_BUTTON)).click()
# screenshot_file_path = 'screenshot.png'
# driver.save_screenshot(screenshot_file_path)

chrome_options = Options()
prefs = {"download.default_directory" : r"C:\Users\User\Downloads\test"}
chrome_options.add_experimental_option("prefs",prefs)

# LOCATORS
BASE_URL = 'https://play1.automationcamp.ir/order_submit.html'
PIZZA_SIZE = {"Large": "Large", "Medium": "Medium", "Small": "Small"}
PIZZA_FLAVOR = {"Cheese": "Cheese", "Pepperoni": "Pepperoni", "Supreme": "Supreme", "Veggie Delight": "Veggie Delight"}
SAUCE = {"Marinara": "Marinara", "Buffala": "Buffala", "Barbeque": "Barbeque"}
TOPPINGS = {"Onions": "Onions", "Green Olive": "Green Olive", "Tomatoes": "Tomatoes"}
ADD_TO_CART_BUTTON_LOC = "//button[@id='submit_button']"



# TEST CASE 1 - Adding to Cart

#ARRANGE
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(BASE_URL)

validation = driver.find_element(By.XPATH, "//h2[@id='added_message']")

#ACT
quantity = driver.find_element(By.XPATH, "//input[@id='quantity']")
quantity.send_keys("1")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@id='submit_button']").click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//h2[@id='added_message']")))

#ASSERT
assert driver.find_element(By.XPATH, "//h2[@id='added_message']").text == "Pizza added to the cart!"

#TEARDOWN
driver.close()
