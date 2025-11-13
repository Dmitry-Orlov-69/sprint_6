class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def click_button(self, button_locator):
        button = self.driver.find_element(*button_locator)
        button.click()

    def fill_field(self, field_locator, text):
        field = self.driver.find_element(*field_locator)
        field.send_keys(text)

    def select_option(self, option_locator):
        option = self.driver.find_element(*option_locator)
        option.click()