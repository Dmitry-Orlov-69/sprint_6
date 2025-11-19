import allure
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на кнопку '{button_locator}'")
    def click_button(self, button_locator):
        button = self.driver.find_element(*button_locator)
        button.click()

    @allure.step("Заполнить поле '{field_locator}' текстом '{text}'")
    def fill_field(self, field_locator, text):
        field = self.driver.find_element(*field_locator)
        field.send_keys(text)

    @allure.step("Выбрать опцию по локатору '{option_locator}'")
    def select_option(self, option_locator):
        option = self.driver.find_element(*option_locator)
        option.click()

    @allure.step("Ожидать, пока элемент станет кликабельным '{locator}'")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидать видимости элемента '{locator}'")
    def wait_for_visibility_of_element_located(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))