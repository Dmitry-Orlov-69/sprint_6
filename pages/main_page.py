class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_button(self, button_locator):
        button = self.driver.find_element(*button_locator)
        button.click()

    def get_answer_text(self, answer_locator):
        return self.driver.find_element(*answer_locator).text