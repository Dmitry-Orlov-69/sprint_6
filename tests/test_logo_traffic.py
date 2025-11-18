from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from locators.base_locators import BaseLocators
import allure

@allure.title("Переход по логотипу 'Самокат'")
def test_navigate_by_logo_scooter(navigate_to_main_page):
    order_page = OrderPage(navigate_to_main_page)

    # Нажимаем на кнопку "Заказать" вверху главной страницы
    order_page.click_button(OrderPageLocators.button_order_top)

    # Ждём перехода на страницу с формой заказа
    order_page.wait_for_url_contains("qa-scooter.praktikum-services.ru")

    # Нажимаем на логотип "Самоката"
    order_page.click_button(BaseLocators.logo_scooter)

    assert "qa-scooter.praktikum-services.ru" in navigate_to_main_page.current_url, "Переход на главную страницу не произошёл"

@allure.title("Переход по лого 'Яндекс'")
def test_navigate_by_logo_yandex(navigate_to_main_page):
    order_page = OrderPage(navigate_to_main_page)

    # Нажимаем на кнопку "Заказать" вверху главной страницы
    order_page.click_button(OrderPageLocators.button_order_top)

    # Ждём перехода на страницу с формой заказа
    order_page.wait_for_url_contains("https://qa-scooter.praktikum-services.ru/order")

    # Нажимаем на лого "Яндекса"
    order_page.click_button(BaseLocators.logo_yandex)

    # Переключаемся на новую вкладку
    navigate_to_main_page.switch_to.window(navigate_to_main_page.window_handles[1])

    # Добавляем ожидание полной загрузки страницы Дзена
    order_page.wait_for_url_contains("dzen.ru")

    assert "dzen.ru" in navigate_to_main_page.current_url, "Переход на страницу Дзена не произошёл"