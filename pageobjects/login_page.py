from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "submit"

    def enter_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button).click()