import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.config_provider import ConfigProvider
from pathlib import Path

cwd = Path.cwd()
cookies = cwd.parent / "cookies.txt"
driver = ConfigProvider.get_selenium_driver()
wait = WebDriverWait(driver, 5)
driver.get("https://the-internet.herokuapp.com/upload")

# choosing a file to upload through send_keys()
choose_button = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
time.sleep(2)
choose_button.send_keys(str(cookies))

# clicking the upload button
upload_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
upload_button.click()

# verifying the text
upload_confirmation = wait.until(
    EC.visibility_of_element_located((By.ID, "uploaded-files"))
)
if upload_confirmation.text == "File Uploaded!":
    print("File uploaded!")
else:
    print("File not uploaded!")
