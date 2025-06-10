from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def get_congratulation_text(self, timeout=50):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, "has-text-align-center"))
        )
        return element.text