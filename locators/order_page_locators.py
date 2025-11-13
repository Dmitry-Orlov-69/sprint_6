from selenium.webdriver.common.by import By

class OrderPageLocators:
    button_order_top = (By.XPATH, "//button[@class='Button_Button__ra12g' and contains(text(), 'Заказать')]") # кнопка "Заказать" вверху главной страницы
    input_name = (By.CSS_SELECTOR, "input[placeholder='* Имя']") # поле "Имя" в форме заказа
    input_surname = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']") # поле "Фамилия" в форме заказа
    input_address = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']") # поле "Адрес: куда привезти заказ" в форме заказа
    input_metro_station = (By.CSS_SELECTOR, "input.select-search__input") # поле "Станция метро" в форме заказа
    metro_station_bulvar_rokovskogo = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='Бульвар Рокоссовского']") # кнопка со станцией "Бульвар Рокоссовского"
    input_phone = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']") # поле "Телефон: на него позвонит курьер" в форме заказа
    button_next = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and contains(text(), 'Далее')]") # кнопка "Далее" в форме заказа
    input_pickup_date = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']") # поле "Когда привезти самокат" в форме заказа
    date_picker_20th = (By.CSS_SELECTOR, ".react-datepicker__day--020") # кнопка с 20 числом месяца
    dropdown_rental_period = (By.CSS_SELECTOR, ".Dropdown-placeholder") # поле "Срок аренды" в форме заказа
    option_rental_period_day = (By.XPATH, "//div[text()='сутки']") # кнопка "сутки"
    checkbox_color_black = (By.ID, "black") # первый чекбокс в поле "Цвет самоката" (чёрный жемчуг)
    input_comment = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']") # поле "Комментарий для курьера" в форме заказа
    button_place_order = (By.XPATH, "//*[@id='root']/div/div[2]/div[3]/button[2]") # кнопка "Заказать" в форме заказа
    modal_header_confirm_order = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]") # текст "Хотите оформить заказ?" в форме заказа
    button_yes = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and contains(text(), 'Да')]") # кнопка "Да" в форме заказа
    modal_header_order_confirmed = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]") # текст "Заказ оформлен" в форме заказа
    button_order_bottom = (By.XPATH, "//*[@id='root']/div/div/div[4]/div[2]/div[5]/button") # кнопка "Заказать" внизу главной страницы
    date_picker_19th = (By.CSS_SELECTOR, ".react-datepicker__day--019") # кнопка с 19 числом месяца
    option_rental_period_two_days = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']") # кнопка "двое суток"
    checkbox_color_grey = (By.ID, "grey") # второй чекбокс в поле "Цвет самоката" (серая безысходность)