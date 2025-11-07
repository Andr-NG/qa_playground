import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utils.config_provider import ConfigProvider
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = ConfigProvider.get_selenium_driver()
wait = WebDriverWait(driver, 5)
action = ActionChains(driver)
double_click_loc = (By.XPATH, "//button[@id='doubleClick']")
hover_loc = (By.XPATH, "//button[@id='colorChangeOnHover']")

driver.get("https://testkru.com/Elements/Buttons")
time.sleep(2)

# double-clicking 
double_click_button = driver.find_element(*double_click_loc)
action.double_click(double_click_button).perform()
text = wait.until(
    EC.text_to_be_present_in_element(double_click_loc, "I was double-clicked!")
)
if text:
    print("I was double-clicked!")
else:
    print("I WAS NOT double-clicked!")

# hovering over
hover_button = driver.find_element(*hover_loc)
action.move_to_element(hover_button)\
    .pause(2)\
    .perform()
time.sleep(3)
color_on_hover = hover_button.value_of_css_property('color')
print(color_on_hover)
