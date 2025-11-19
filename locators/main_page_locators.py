from selenium.webdriver.common.by import By 

class MainPageLocators:
    button_how_much = (By.ID, "accordion__heading-0") # кнопка вопроса "Сколько это стоит? И как оплатить?"
    button_multiple_scooters = (By.ID, "accordion__heading-1") # кнопка вопроса "Хочу сразу несколько самокатов! Так можно?"
    button_rental_time = (By.ID, "accordion__heading-2") # кнопка вопроса "Как рассчитывается время аренды?"
    button_today_order = (By.ID, "accordion__heading-3") # кнопка вопроса "Можно ли заказать самокат прямо на сегодня?"
    button_extend_order = (By.ID, "accordion__heading-4") # кнопка вопроса "Можно ли продлить заказ или вернуть самокат раньше?"
    button_charging = (By.ID, "accordion__heading-5") # кнопка вопроса "Вы привозите зарядку вместе с самокатом?"
    button_cancel_order = (By.ID, "accordion__heading-6") # кнопка вопроса "Можно ли отменить заказ?"
    button_outside_mkad = (By.ID, "accordion__heading-7") # кнопка вопроса "Я жизу за МКАДом, привезёте?"

    answer_how_much = (By.ID, "accordion__panel-0") # текст ответа на соответствующий вопрос
    answer_multiple_scooters = (By.ID, "accordion__panel-1") # текст ответа на соответствующий вопрос
    answer_rental_time = (By.ID, "accordion__panel-2") # текст ответа на соответствующий вопрос
    answer_today_order = (By.ID, "accordion__panel-3") # текст ответа на соответствующий вопрос
    answer_extend_order = (By.ID, "accordion__panel-4") # текст ответа на соответствующий вопрос
    answer_charging = (By.ID, "accordion__panel-5") # текст ответа на соответствующий вопрос
    answer_cancel_order = (By.ID, "accordion__panel-6") # текст ответа на соответствующий вопрос
    answer_outside_mkad = (By.ID, "accordion__panel-7") # текст ответа на соответствующий вопрос