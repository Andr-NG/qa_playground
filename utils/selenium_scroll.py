from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains


class Scrolls:

    def __init__(self, driver: WebDriver, action: ActionChains):
        self.driver = driver
        self.action = action

    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, element, extra):
        self.action.scroll_to_element(element).perform()
        script = """
        window.scrollTo({
            top: window.scrollY + 700},
        });
        """
        self.driver.execute_script(script.replace("700", str(extra)))

