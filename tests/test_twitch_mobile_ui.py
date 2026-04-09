from __future__ import annotations

from pathlib import Path

import pytest

from src.core.settings import ui_settings
from src.pages.twitch_page import TwitchPage


@pytest.mark.ui
def test_twitch_search_and_open_stream_mobile(driver, screenshot_file: Path) -> None:
    page = TwitchPage(driver)

    page.open(ui_settings.base_url)
    page.click_search_icon()
    page.go_to_search_page()
    page.search_for(ui_settings.search_term)
    page.scroll_down_twice()
    page.open_first_streamer()
    page.wait_for_stream_player()

    assert driver.save_screenshot(str(screenshot_file))
