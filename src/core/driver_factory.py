from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.core.settings import ui_settings


def create_mobile_chrome_driver() -> webdriver.Chrome:
    options = Options()
    options.add_experimental_option(
        "mobileEmulation",
        {"deviceName": ui_settings.device_name},
    )
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(ui_settings.implicit_wait_seconds)
    return driver
