import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators

@pytest.mark.parametrize('name, surname, address, phone, metro_station, comment', [
    ("Иван", "Иванов", "г. Санкт-Петербург", "89821234567", "metro_station_bulvar_rokovskogo", "мой первый комментарий"),
    ("Петр", "Петров", "г. Москва", "89822345678", "metro_station_bulvar_rokovskogo", "мой второй комментарий")
])
def test_order_flow(driver, name, surname, address, phone, metro_station, comment):
    order_page = OrderPage(driver)
    driver.get("https://qa-scooter.praktikum-services.ru")

    # Нажимаем на кнопку "Заказать" вверху главной страницы
    order_page.click_button(OrderPageLocators.button_order_top)

    # Ждём перехода на страницу с формой заказа
    WebDriverWait(driver, 10).until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/order"))

    # Заполняем форму заказа
    order_page.fill_field(OrderPageLocators.input_name, name)
    order_page.fill_field(OrderPageLocators.input_surname, surname)
    order_page.fill_field(OrderPageLocators.input_address, address)
    order_page.click_button(OrderPageLocators.input_metro_station)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(getattr(OrderPageLocators, metro_station))).click()
    order_page.fill_field(OrderPageLocators.input_phone, phone)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.button_next))
    order_page.click_button(OrderPageLocators.button_next)

    # Выбираем дату и срок аренды
    order_page.click_button(OrderPageLocators.input_pickup_date)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.date_picker_20th)).click()
    order_page.click_button(OrderPageLocators.dropdown_rental_period)
    order_page.select_option(OrderPageLocators.option_rental_period_day)

    # Выбираем цвет самоката и добавляем комментарий
    order_page.click_button(OrderPageLocators.checkbox_color_black)
    order_page.fill_field(OrderPageLocators.input_comment, comment)

    # Завершаем оформление заказа
    order_page.click_button(OrderPageLocators.button_place_order)
    confirm_modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.modal_header_confirm_order))
    order_page.click_button(OrderPageLocators.button_yes)

    # Проверяем сообщение об успешном оформлении заказа
    order_confirmed_modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.modal_header_order_confirmed))
    assert "Заказ оформлен" in order_confirmed_modal.text