import random
from pages.actions.login_page import LoginPage
from utils.test_data import accepted_users, password

def test_login_success(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.load()
    username = random.choice(accepted_users)
    login_page.login(username, password)

    # Check if login succeeded
    assert "inventory" in driver.current_url
