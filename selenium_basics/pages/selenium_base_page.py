from selenium.webdriver.remote.webdriver import WebDriver


class SeleniumBasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)
