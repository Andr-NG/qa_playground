import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

load_dotenv()


class ConfigProvider:

    URLS = {
        "prod": "https://app.multilogin.com/",
        "stg": "https://app-staging-eu.mlx.yt/"
    }
    SESSION_ENV = os.getenv("ENV")

    @classmethod
    def get_url(cls) -> str | None:
        if cls.SESSION_ENV.lower() not in cls.URLS:
            raise ValueError("ENV doesn't exist")
        return cls.URLS[cls.SESSION_ENV.lower()]

    @classmethod
    def get_selenium_driver(cls) -> WebDriver:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("detach", True)
        return webdriver.Chrome(options=options)
