import time
from selenium_basics.pages.selenium_login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import allure


@allure.story("Logging in")
def test_selenium_login(login_page: LoginPage, driver: WebDriver) -> None:
    with allure.step("Going to the login page and inputing the creds"):
        allure.attach(
            json.dumps(
                {"email": "andrey.nguyen@multilogin.com", "password": "Qwerty123!"}
            ),
            "Request body",
            attachment_type=allure.attachment_type.TEXT,
        )
        login_page.open("https://app.multilogin.com/en/auth/signin")
        login_page.log_in("andrey.nguyen@multilogin.com", "Qwerty123!")

    # wait = WebDriverWait(driver, timeout=4)

    # with allure.step("Closing the referral banner"):
    #     wait.until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, ".close.cursor-pointer"))
    #     ).click()
    #     allure.attach(
    #         driver.get_screenshot_as_png(),
    #         "home_page_screenshot",
    #         allure.attachment_type.PNG,
    #     )

    with allure.step("Asserting"):
    #     wait.until(
    #         EC.presence_of_element_located(
    #             (By.XPATH, '//div[@class="sidebar-container-logo"]')
    #         )
    #     )
    #     driver.execute_cdp_cmd(
    #         "Browser.setPermission",
    #         {
    #             "permission": {"name": "local-network"},
    #             "setting": "granted",  # or "denied"
    #             "origin": "https://app.multilogin.com",
    #         },
    #     )
        time.sleep(2)
        home_page = driver.current_url
        title = driver.title
        assert home_page == "https://app.multilogin.com/en/home/profiles"
        assert title == "Profiles"


@allure.story("Logging in with wrong creds")
def test_negative_selenium_login(login_page: LoginPage, driver: WebDriver) -> None:
    with allure.step("Going to the login page and inputing wrong creds"):
        allure.attach(
            json.dumps(
                {"email": "andrey.nguyen@multilogin.com", "password": "Qwerty1234!"}
            ),
            "Request body",
            attachment_type=allure.attachment_type.TEXT,
        )
        login_page.log_in("andrey.nguyen@multilogin.com", "Qwerty1234!")
    wait = WebDriverWait(driver, timeout=5)
    notification = (By.CSS_SELECTOR, ".mat-body-medium.text")
    notification_text = wait.until(EC.visibility_of_element_located(notification)).text
    print(notification_text)

    with allure.step("Asserting"):
        home_page = driver.current_url
        title = driver.title
        assert home_page == "https://app.multilogin.com/en/home/profiles"
        assert title == "Profiles"
