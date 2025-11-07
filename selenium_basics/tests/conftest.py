from typing import Any, Generator
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium_basics.pages.selenium_login_page import LoginPage


@pytest.fixture
def driver() -> Generator[WebDriver, Any, None]:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.close()


@pytest.fixture
def login_page(driver: WebDriver) -> LoginPage:
    driver.get("https://app.multilogin.com/en/auth/signing")
    page = LoginPage(driver)
    return page


@pytest.hookimpl(hookwrapper=True, tryfirst=True,)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    """
    This is a pytest hook that runs after each test phase (setup, call, teardown).

    hookwrapper=True tells pytest this hook will wrap execution of the real hook.
    tryfirst=True makes pytest run the hook before other hooks.

    rep = outcome.get_result() turns the outcome into a TestReport object.
    rep is what pytest itself uses to decide "test passed / failed / skipped".

    rep.when → which phase we are in: "setup", "call" (the test function itself), or "teardown".
    rep.failed → boolean flag, True if that phase failed.

    item.funcargs: dictionary of all fixtures injected into the test.

    Args:
        item (pytest.Item):  pytest test function object (Function), gives you metadata like name,
        markers, fixture arguments, etc.
        call (pytest.CallInfo): internal object representing the execution of that phase
        (setup/call/teardown). It contains info about exceptions, outcomes, and timings.
    """

    # grabbing test report
    outcome = yield
    rep: pytest.TestReport = outcome.get_result()

    # taking screenshots only on test body failures, so check rep.when == "call"
    if rep.when == "call" and rep.failed:
        driver: WebDriver = item.funcargs.get("driver")

        if driver:
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name=f"screenshot_on_failure_{item.name}",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as e:
                print(f"Could not take screenshot: {e}")
