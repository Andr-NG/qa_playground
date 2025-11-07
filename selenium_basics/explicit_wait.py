from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.config_provider import ConfigProvider

driver = ConfigProvider.get_selenium_driver()
wait = WebDriverWait(driver, timeout=10)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
start_locator = (By.XPATH, '//button[text()="Start"]')
text_locator = (By.XPATH, '//div[@id="finish"]')

# explicitly waiting for element to be clickable
wait.until(EC.visibility_of_element_located((start_locator))).click()

# explicitly waiting for text in element
text = wait.until(
    EC.text_to_be_present_in_element(text_locator, "Hello World!")
)
if text:
    print(driver.find_element(*text_locator).text)
    with open("cookies.txt", "w") as file:
        file.write(str(driver.get_cookies()))
else:
    print("Text not found")

driver.find_element(By.LINK_TEXT, "Open new tab").click()
driver.switch_to.window(driver.window_handles[1])
