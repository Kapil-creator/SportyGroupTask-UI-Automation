from dataclasses import dataclass


@dataclass(frozen=True)
class UiSettings:
    base_url: str = "https://m.twitch.tv"
    search_url: str = "https://m.twitch.tv/search"
    search_term: str = "StarCraft II"
    device_name: str = "iPhone X"
    implicit_wait_seconds: int = 1
    explicit_wait_seconds: int = 8


ui_settings = UiSettings()
