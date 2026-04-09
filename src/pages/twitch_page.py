from __future__ import annotations

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

from src.core.settings import ui_settings
from src.pages.base_page import BasePage


class TwitchPage(BasePage):
    SEARCH_ICON_CANDIDATES = [
        (By.XPATH, "//button[contains(@aria-label,'Search')]"),
        (By.XPATH, "//a[contains(@href,'/search')]"),
        (By.XPATH, "//button[contains(.,'Search')]"),
    ]
    SEARCH_INPUT_CANDIDATES = [
        (By.XPATH, "//input[@type='search']"),
        (By.XPATH, "//input[contains(@placeholder,'Search')]"),
        (By.XPATH, "//input[contains(@aria-label,'Search')]"),
    ]
    STREAM_LINK_CANDIDATES = [
        (By.XPATH, "//a[contains(@href,'/videos/')]"),
        (By.XPATH, "//a[starts-with(@href,'/') and not(contains(@href,'/directory/')) and not(contains(@href,'/search'))]"),
    ]
    PLAYER_CANDIDATES = [
        (By.XPATH, "//video"),
        (By.XPATH, "//*[@data-a-target='player-overlay-click-handler']"),
        (By.XPATH, "//*[@data-a-target='video-player']"),
    ]
    POPUP_CLOSE_CANDIDATES = [
        (By.XPATH, "//button[@aria-label='Close']"),
        (By.XPATH, "//button[@data-a-target='modal-close-button']"),
        (By.XPATH, "//button[contains(.,'Accept')]"),
        (By.XPATH, "//button[contains(.,'I understand')]"),
        (By.XPATH, "//button[contains(.,'Close')]"),
        (By.XPATH, "//button[contains(.,'Start Watching')]"),
        (By.XPATH, "//button[contains(.,'Watch now')]"),
    ]

    def close_popups_if_any(self) -> None:
        for locator in self.POPUP_CLOSE_CANDIDATES:
            self.click_if_present(locator)

    def click_search_icon(self) -> None:
        for locator in self.SEARCH_ICON_CANDIDATES:
            try:
                self.wait_clickable(locator).click()
                return
            except TimeoutException:
                continue

    def go_to_search_page(self) -> None:
        self.driver.get(ui_settings.search_url)

    def search_for(self, term: str) -> None:
        for locator in self.SEARCH_INPUT_CANDIDATES:
            try:
                field = self.wait_visible(locator)
                field.clear()
                field.send_keys(term)
                field.send_keys(Keys.ENTER)
                return
            except TimeoutException:
                continue
        raise TimeoutException("Search input did not appear.")

    def scroll_down_twice(self) -> None:
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.35);")
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.35);")

    def open_first_streamer(self) -> None:
        self.close_popups_if_any()
        for locator in self.STREAM_LINK_CANDIDATES:
            links = self.driver.find_elements(*locator)
            if links:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", links[0])
                self.close_popups_if_any()
                self.driver.execute_script("arguments[0].click();", links[0])
                return
        raise AssertionError("No streamer found in search results.")

    def wait_for_stream_player(self) -> None:
        self.close_popups_if_any()
        for locator in self.PLAYER_CANDIDATES:
            try:
                self.wait.until(ec.visibility_of_element_located(locator))
                return
            except TimeoutException:
                continue
        raise TimeoutException("Streamer page loaded but player element not visible.")
