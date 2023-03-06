import allure
import pytest
from selene.support.shared import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
from dotenv import load_dotenv

from browserstavk_mobile_testing.helpers import attach


@pytest.fixture(scope="function", autouse=True)
def driver_config():
    load_dotenv()
    options = UiAutomator2Options().load_capabilities(
        {
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "app": os.getenv("app"),
            "bstack:options": {
                "projectName": "Wiki mibile",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack session",
                "userName": os.getenv("user_name"),
                "accessKey": os.getenv("access_key"),
            },
        }
    )

    with allure.step("Define driver"):
        browser.config.driver = webdriver.Remote(
            os.getenv("remote_url"), options=options
        )

    yield
    attach.add_video(browser)
    browser.quit()