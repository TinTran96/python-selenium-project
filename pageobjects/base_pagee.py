class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    def click(self, element):
        element.click()

    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)