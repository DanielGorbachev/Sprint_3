from selenium.webdriver.common.by import By


class Locator:

    # поле для ввода email'а
    email_field = (By.XPATH, "//input[@name = 'name']")

    # поле ввода пароля
    password_field = (By.XPATH, "//input[@name = 'Пароль']")

    # кнопка "личный кабинет"
    cabinet = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

    # кнопка "войти в аккаунт"
    enter_acc = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

    # кнопка "Оформить заказ"
    place_order = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # поле с логином в кабинете после входа на сайт
    my_login_field = (By.XPATH, "//label[contains(text(),'Логин')]")

    # ПЕРЕХОД НА РОДИТЕЛЯ НАДПИСЕЙ КОЛЛЕКТОРА ДЛЯ ПРОВЕРКИ ИХ ВЫБОРА
    # булки
    buns = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div")
    # соусы
    souses = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div")
    # начинки
    stuffing = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div")

    # новая кнопка "Войти"
    to_log_in_new = (By.XPATH, "//button[contains(text(),'Войти')]")

    # новая кнопка "зарегистрироваться", работающая как гиперссылка
    to_register_href = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")

    # новая кнопка "оформить заказ"
    place_order_new = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # новое поле с моим логином в кабинете после входа на сайт
    my_login_field_new = (By.XPATH, "//input[@value='daniil_gorbachev_08_888@yandex.ru']")\

    # кнопка восстановить пароль
    recover_password = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    # кнопка "войти", работающая как гиперссылка
    to_login_href = (By.XPATH, "//a[contains(text(),'Войти')]")

    # КНОПКА зарегистрироваться
    to_register = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")

    # Поле ввода имени
    enter_name_field = (By.XPATH, ".//fieldset[1]/div/div/input")
    # Поле ввода почты
    enter_mail_field = (By.XPATH, ".//fieldset[2]/div/div/input")
    # Заголовок с надписью ВХОД
    header_enter = (By.XPATH, "//h2[contains(text(),'Вход')]")
    # Кнопка "выход"
    exit_btn = (By.XPATH, "//button[contains(text(),'Выход')]")
    # Кнопка "история заказов"
    order_history_btn = (By.XPATH, "//a[contains(text(),'История заказов')]")
    # Кнопка "Конструктор"
    constructor_btn = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    # Оглавление "Соберите бургер"
    header_assemble_burger = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
    # URL главной страницы сайта
    site_url = "https://stellarburgers.nomoreparties.site/"
    # Ошибка "Некорректный пароль"
    wrong_password = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")