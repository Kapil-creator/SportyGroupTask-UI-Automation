from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.core.settings import ui_settings


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, ui_settings.explicit_wait_seconds)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def wait_visible(self, locator: tuple[str, str]):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def wait_clickable(self, locator: tuple[str, str]):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click_if_present(self, locator: tuple[str, str]) -> bool:
        elements = self.driver.find_elements(*locator)
        if not elements:
            return False
        try:
            elements[0].click()
            return True
        except Exception:
            return False
