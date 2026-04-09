# UI Automation - Twitch (Pytest + Selenium)

This project automates Twitch in Chrome mobile emulation.

## Stack
- Python 3
- Pytest
- Selenium

## Structure
- `src/core`: config and driver creation
- `src/pages`: page objects
- `tests`: test cases and fixtures
- `artifacts/screenshots`: test screenshots

## Scenario Covered
1. Open `https://m.twitch.tv`
2. Click search icon
3. Go to `https://m.twitch.tv/search`
4. Search `StarCraft II`
5. Scroll down twice
6. Select one streamer
7. Wait for page/player load
8. Take screenshot

## Run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -m ui
```

## Test Case Table
| Test Name | Description | Expected Result |
|---|---|---|
| Twitch mobile search and stream open | Validate full mobile journey and screenshot capture | Streamer page opens and screenshot is saved |

## Validation Strategy
- Explicit waits are used for clickable/visible elements to reduce flakiness.
- Popup handlers run before and during stream navigation.
- Mobile emulation is enforced from the driver factory (`iPhone X` profile).

## GIF
Added run recording GIF here ("https://github.com/Kapil-creator/SportyGroupTask-UI-Automation/Animation_UI.gif")

## Evaluation Mapping
- **Attention to detail**: Mobile emulation enabled, Twitch flow matches the assignment steps, and popups are handled.
- **Problem-solving**: Resilient XPaths and JS click/scroll handle layout changes and intercepted clicks.
- **Flakiness & reliability**: Explicit waits wrap all key interactions; no hard sleeps are used.
- **Coding standards**: Page Object Model, clear naming, and configuration in src/core/settings.py.
- **Testing approach**: End-to-end user journey with screenshot artifact and reusable fixtures.
- **Scalability**: New flows can be added via new page methods and 	ests/*.py files.
