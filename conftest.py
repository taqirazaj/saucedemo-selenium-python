import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for CI
    options.add_argument("--no-sandbox")  # Recommended for GitHub Actions
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")  # Optional: reduce GPU errors
    options.add_argument("--remote-debugging-port=9222")  # Avoid debugging lock
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-browser-side-navigation")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
