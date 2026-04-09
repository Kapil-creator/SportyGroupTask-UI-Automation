from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pytest

from src.core.driver_factory import create_mobile_chrome_driver


@pytest.fixture
def driver():
    web_driver = create_mobile_chrome_driver()
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="session")
def screenshots_dir() -> Path:
    folder = Path("artifacts/screenshots")
    folder.mkdir(parents=True, exist_ok=True)
    return folder


@pytest.fixture
def screenshot_file(screenshots_dir: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return screenshots_dir / f"twitch_stream_{timestamp}.png"
