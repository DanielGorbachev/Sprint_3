from selenium.webdriver.common.by import By


class Locators:

    # поле для ввода email'а
    email_field = (By.XPATH, "//input[@name = 'name']")

    # поле ввода пароля
    password_field = (By.CSS_SELECTOR, ".text[name='Пароль']")

    # кнопка "личный кабинет"
    cabinet = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

    # кнопка "Войти"
    to_log_in = (By.XPATH, "/html/body/div[1]/div/main/div/form/button[text()='Войти']")

    # кнопка "войти в аккаунт"
    enter_acc = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

    # кнопка "Зарегистрироваться" на странице входа


    # кнопка "Оформить заказ"
    place_order = (By.XPATH, "/html/body/div/div/main/section/div/button")

    # поле с логином в кабинете после входа на сайт
    my_login_field = (By.XPATH, "/html/body/div/div/main/div/div/div/ul/li/div/div/input")

    # ПЕРЕХОД НА РОДИТЕЛЯ ДЛЯ НАДПИСЕЙ КОЛЛЕКТОРА ДЛЯ ПРОВЕРКИ ИХ ВЫБОРА
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

    # КОПКА зарегистрироваться
    to_register = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")