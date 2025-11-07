# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utils.config_provider import ConfigProvider

driver = ConfigProvider.get_selenium_driver()

dropdown_locator = (By.XPATH, "//select[@id='dropdown']")
driver.get("https://the-internet.herokuapp.com/dropdown")

# creating Select object with its web element
dropdown = Select(driver.find_element(*dropdown_locator))

# dropdown.select_by_index(1) "Option 1"
# dropdown.select_by_visible_text("Option 1")

all_options = dropdown.options
for opt in all_options:

    time.sleep(3)
    dropdown.select_by_visible_text(opt.text)     # the text of the opt is passed
    dropdown.select_by_index(all_options.index(opt))  # the index of opt is passed