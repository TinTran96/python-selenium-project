import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from selenium import webdriver
from utilities.driver_factory import DriverFactory
from pageobjects.login_page import LoginPage
from pageobjects.dashboard_page import DashboardPage
import dotenv

dotenv.load_dotenv()

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    driver = None  # Class variable

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup_and_teardown(cls, request):
        # Setup: runs before each test
        driver_factory = DriverFactory("chrome")
        cls.driver = driver_factory.create_driver()
        yield
        # Teardown: runs after each test
        cls.driver.quit()

    @pytest.mark.order(1)
    def test_login(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        email = os.getenv("TEST_EMAIL")
        password = os.getenv("TEST_PASSWORD")
        self.driver.get(os.getenv("SITE_URL"))
        self.driver.set_window_size(1797, 1079)
        login_page.enter_username(email)
        login_page.enter_password(password)
        login_page.click_login()
        congrat_text = dashboard_page.get_congratulation_text()
        assert congrat_text, "Congratulations student. You successfully logged in!"