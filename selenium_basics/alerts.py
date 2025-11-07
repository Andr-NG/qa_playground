import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.config_provider import ConfigProvider


driver = ConfigProvider.get_selenium_driver()
wait = WebDriverWait(driver, 5)
driver.get("https://demoqa.com/alerts")

alert_button = driver.find_element(By.ID, "alertButton")
alert_button.click()
time.sleep(3)

alert: EC.Alert = wait.until(lambda d: d.switch_to.alert)
alert.accept()

