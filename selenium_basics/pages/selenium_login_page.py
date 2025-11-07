from selenium_basics.pages.selenium_base_page import SeleniumBasePage
from selenium.webdriver.common.by import By

USERNAME_LOCATOR = "#mat-input-0"
PASS_LOCATOR = "#mat-input-1"
LOG_IN_BUTTON_LOCATOR = ".mdc-button.mdc-button--unelevated"
REMEMBER_LOCATOR = "#mat-mdc-checkbox-1-input"
DROPDOWN_LOCATOR = "#mat-mdc-chip-0"


class LoginPage(SeleniumBasePage):

    def log_in(self, email: str, password: str) -> None:
        self.driver.find_element(By.ID, USERNAME_LOCATOR.replace("#", "")).send_keys(email)
        self.driver.find_element(By.ID, PASS_LOCATOR.replace("#", "")).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, REMEMBER_LOCATOR).click()
        self.driver.find_element(By.CSS_SELECTOR, LOG_IN_BUTTON_LOCATOR).click()
