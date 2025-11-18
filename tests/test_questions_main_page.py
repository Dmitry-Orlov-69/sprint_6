import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
import allure

@pytest.mark.parametrize("question_button, expected_text, answer_locator", [
    (MainPageLocators.button_how_much, "Сутки — 400 рублей. Оплата курьеру — наличными или картой.", MainPageLocators.answer_how_much),
    (MainPageLocators.button_multiple_scooters, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.", MainPageLocators.answer_multiple_scooters),
    (MainPageLocators.button_rental_time, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.", MainPageLocators.answer_rental_time),
    (MainPageLocators.button_today_order, "Только начиная с завтрашнего дня. Но скоро станем расторопнее.", MainPageLocators.answer_today_order),
    (MainPageLocators.button_extend_order, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.", MainPageLocators.answer_extend_order),
    (MainPageLocators.button_charging, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.", MainPageLocators.answer_charging),
    (MainPageLocators.button_cancel_order, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.", MainPageLocators.answer_cancel_order),
    (MainPageLocators.button_outside_mkad, "Да, обязательно. Всем самокатов! И Москве, и Московской области.", MainPageLocators.answer_outside_mkad)
])
@allure.title("Проверка ответа на вопрос: {question_button}")
def test_questions(navigate_to_main_page, question_button, expected_text, answer_locator):
    main_page = MainPage(navigate_to_main_page)

    # Прокручиваем элемент в видимую область
    main_page.scroll_into_view(question_button)

    # Кликаем по элементу с использованием JavaScript
    main_page.click_button_with_js(question_button)

    # Добавляем ожидание появления текста ответа
    main_page.wait_for_text_to_be_present_in_element(answer_locator, expected_text)

    answer = main_page.get_answer_text(answer_locator)
    assert answer == expected_text