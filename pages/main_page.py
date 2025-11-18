import allure
from pages.order_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на кнопку '{button_locator}'")
    def click_button(self, button_locator):
        button = self.driver.find_element(*button_locator)
        button.click()

    @allure.step("Получить текст ответа по локатору '{answer_locator}'")
    def get_answer_text(self, answer_locator):
        return self.driver.find_element(*answer_locator).text
    
    @allure.step("Прокрутить элемент в видимую область '{element_locator}'")
    def scroll_into_view(self, element_locator):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидать появления текста '{text}' в элементе '{locator}'")
    def wait_for_text_to_be_present_in_element(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Нажать на элемент с использованием JavaScript '{locator}'")
    def click_button_with_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)