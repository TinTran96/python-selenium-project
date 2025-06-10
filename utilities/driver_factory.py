class DriverFactory:
    def __init__(self, browser):
        self.browser = browser
        self.driver = None

    def create_driver(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        from selenium.webdriver.firefox.options import Options as FirefoxOptions

        url = "http://127.0.0.1:4444/wd/hub"

        if self.browser.lower() == 'chrome':
            options = ChromeOptions()
            options.add_argument("--disable-dev-shm-usage")
            self.driver = webdriver.Remote(
                command_executor=url,
                options=options
            )
        elif self.browser.lower() == 'firefox':
            options = FirefoxOptions()
            options.add_argument("--disable-dev-shm-usage")
            self.driver = webdriver.Remote(
                command_executor=url,
                options=options
            )
        else:
            raise ValueError(f"Browser '{self.browser}' is not supported.")

        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()