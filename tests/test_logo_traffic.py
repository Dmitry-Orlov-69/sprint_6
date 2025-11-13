from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.base_locators import BaseLocators

def test_navigate_by_logo_scooter(driver):
    order_page = OrderPage(driver)
    driver.get("https://qa-scooter.praktikum-services.ru")

    # Нажимаем на кнопку "Заказать" вверху главной страницы
    order_page.click_button(OrderPageLocators.button_order_top)

    # Ждём перехода на страницу с формой заказа
    WebDriverWait(driver, 10).until(EC.url_contains("qa-scooter.praktikum-services.ru"))

    # Нажимаем на логотип "Самоката"
    order_page.click_button(BaseLocators.logo_scooter)

    assert "qa-scooter.praktikum-services.ru" in driver.current_url, "Переход на главную страницу не произошёл"

def test_navigate_by_logo_yandex(driver):
    order_page = OrderPage(driver)
    driver.get("https://qa-scooter.praktikum-services.ru")

    # Нажимаем на кнопку "Заказать" вверху главной страницы
    order_page.click_button(OrderPageLocators.button_order_top)

    # Ждём перехода на страницу с формой заказа
    WebDriverWait(driver, 10).until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/order"))

    # Нажимаем на логотип "Яндекса"
    order_page.click_button(BaseLocators.logo_yandex)

    # Переключаемся на новую вкладку
    driver.switch_to.window(driver.window_handles[1])

    # Добавляем ожидание полной загрузки страницы Дзена
    WebDriverWait(driver, 15).until(lambda d: "dzen.ru" in d.current_url)

    assert "dzen.ru" in driver.current_url, "Переход на страницу Дзена не произошёл"