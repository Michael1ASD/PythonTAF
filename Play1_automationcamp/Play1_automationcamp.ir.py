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

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SUBPAGE_WAIT_CONDITIONS_BUTTON)).click()
# screenshot_file_path = 'screenshot.png'
# driver.save_screenshot(screenshot_file_path)

# LOCATORS
BASE_URL = 'https://play1.automationcamp.ir/'
SUBPAGE_WAIT_CONDITIONS_BUTTON = (By.XPATH, '//a[@href="expected_conditions.html"]')

# # TEST CASE 1 - Handling browser alert with waiting
# #ARRANGE
# driver = webdriver.Chrome()
# driver.get(BASE_URL)
# driver.find_element(*SUBPAGE_WAIT_CONDITIONS_BUTTON).click()
#
# #ACT
# driver.find_element(By.XPATH, "//button[@id='alert_trigger']").click()
# WebDriverWait(driver, 5).until(EC.alert_is_present())
# Alert(driver).accept()
# alert_handled = driver.find_element(By.XPATH, "//span[@id='alert_handled_badge']")
#
# #ASSERT
# assert alert_handled.is_displayed(), "Alert not handled"
#
# #TEARDOWN
# driver.close()

#-------------------

# # TEST CASE 2 - Handling confirmation dismissal with waiting
# #ARRANGE
# driver = webdriver.Chrome()
# driver.get(BASE_URL)
# driver.find_element(*SUBPAGE_WAIT_CONDITIONS_BUTTON).click()
#
# #ACT
# driver.find_element(By.XPATH, "//button[@id='prompt_trigger']").click()
# WebDriverWait(driver, 5).until(EC.alert_is_present())
# Alert(driver).dismiss()
# confirmation_handled = driver.find_element(By.XPATH, "//h3[@id='confirm_cancelled']")
#
# # ASSERT
# assert confirmation_handled.is_displayed(), "Confirmation not handled"

#-------------------

# # TEST CASE 3 - Wait for element to be visible
# #ARRANGE
# driver = webdriver.Chrome()
# driver.get(BASE_URL)
# driver.find_element(*SUBPAGE_WAIT_CONDITIONS_BUTTON).click()
#
# #ACT
# driver.find_element(By.XPATH, "//button[@id='visibility_trigger']").click()
# visible_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='visibility_target']")))
#
# # ASSERT
# assert visible_button.is_displayed(), "Button is not visible"

#-------------------

# # TEST CASE 4 - Wait for element to be Invisible
# #ARRANGE
# driver = webdriver.Chrome()
# driver.get(BASE_URL)
# driver.find_element(*SUBPAGE_WAIT_CONDITIONS_BUTTON).click()
#
# #ACT
# driver.find_element(By.XPATH, "//button[@id='invisibility_trigger']").click()
# # driver.find_element(By.XPATH, "/div[@id='invisibility_target']").click()
# invisible_button = WebDriverWait(driver, 6).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id='invisibility_target']")))
#
# # ASSERT
# assert not invisible_button.is_displayed(), "Spinner is still visible"

#-------------------

# # TEST CASE 5 - Wait for element to be enabled
# #ARRANGE
# driver = webdriver.Chrome()
# driver.get(BASE_URL)
# driver.find_element(*SUBPAGE_WAIT_CONDITIONS_BUTTON).click()
#
# #ACT
# driver.find_element(By.XPATH, "//button[@id='enabled_trigger']").click()
# enabled_button = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='enabled_target']")))
#
# # ASSERT
# assert enabled_button.is_enabled(), "Button is still disabled"

#-------------------

# # TEST CASE 6 - Keyboard Actions
# #ARRANGE
# driver = webdriver.Chrome()
# driver.get("https://play1.automationcamp.ir/keyboard_events.html")
#
# #ACT
# textbox = driver.find_element(By.XPATH, "//textarea[@id='area']")
#
# action = ActionChains(driver)
# action.click(textbox)
# action.send_keys("abc")
# action.perform()
#
# # ASSERT
# assert textbox.get_attribute('value') == "abc", "No text typed in"

#-------------------

# # TEST CASE 6 - Mouse Actions
# #ARRANGE
# driver = webdriver.Chrome()
# driver.get("https://play1.automationcamp.ir/mouse_events.html")
#
# #ACT
# textbox = driver.find_element((By.XPATH, "//div[@id='click_area']"))
# action = ActionChains(driver)
# action.context_click(textbox)
# # ASSERT

#-------------------

# # TEST CASE 7 - Perform mouse hover to interact with drop-down menu
# #ARRANGE
# driver = webdriver.Chrome()
# driver.get("https://play1.automationcamp.ir/mouse_events.html")
#
# #ACT
# hoverable = driver.find_element(By.XPATH, "//button[@class='dropbtn']")
# ActionChains(driver).move_to_element(hoverable).perform()
# driver.find_element(By.XPATH, "//p[@id='dd_python']").click()
# validation = driver.find_element(By.XPATH, "//h4[@id='hover_validate']")
#
# # ASSERT
# assert validation.text == ("Python"), "No dropdown selected"

#-------------------

# #TEST CASE 8 - Drag and Drop - Drag blue box on the green box
# #ARRANGE
# driver = webdriver.Chrome()
# driver.get("https://play1.automationcamp.ir/mouse_events.html")
#
# #ACT
# draggable = driver.find_element(By.XPATH, "//button[@id='drag_source']")
# start = draggable.location
# finish = driver.find_element(By.ID, "drop_target").location
# ActionChains(driver).drag_and_drop_by_offset(draggable, finish['x'] - start['x'], finish['y'] - start['y']).perform()
#
# # ASSERT
# assert driver.find_element(By.XPATH, "//div[@id='drop_target']").text == "Drop is successful!", "Drag and drop failed"

#-------------------

# TEST CASE 9 - Multiple windows

#ARRANGE
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://play1.automationcamp.ir/multi_window.html")

#ACT
source_tab = driver.current_window_handle
button_opening_new_tab = driver.find_element(By.XPATH, "//a[@id='window1']")
button_opening_new_tab.click()
all_tabs = driver.window_handles
for handle in all_tabs:
    if handle != source_tab:
        driver.switch_to.window(handle)
        assert driver.find_element(By.XPATH, "//a[@class='navbar-brand']").is_displayed(), "New tab not visible"
button_in_the_new_tab = driver.find_element(By.XPATH, "//button[@id='click_me_2']")
button_in_the_new_tab.click()

# ASSERT
assert button_in_the_new_tab.text == "Clicked", "Target button not clicked"