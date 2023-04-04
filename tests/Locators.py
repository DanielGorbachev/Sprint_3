from selenium.webdriver.common.by import By


class Locators:

    # поле для ввода email'а
    EMAIL_FIELD = (By.XPATH, "//input[@name = 'name']")

    # поле ввода пароля
    PASSWORD_FIELD = (By.CSS_SELECTOR, ".text[name='Пароль']")

    # кнопка "личный кабинет"
    CABINET = (By.XPATH, "/html/body/div/div/header/nav/a")

    # кнопка "Войти"
    TO_LOG_IN = (By.XPATH, "/html/body/div[1]/div/main/div/form/button[text()='Войти']")

    # кнопка "войти в аккаунт"
    ENTER_ACC = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

    # кнопка "Зарегистрироваться" на странице входа
    TO_REGISTER = (By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a")

    # кнопка "Оформить заказ"
    PLACE_ORDER = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]")

    # поле с логином в кабинете после входа на сайт
    MY_LOGIN_FIELD = (By.XPATH, "/html/body/div[1]/div/main/div/div/div/ul/li[2]/div/div/input")

    # ПЕРЕХОД НА РОДИТЕЛЯ ДЛЯ НАДПИСЕЙ КОЛЛЕКТОРА ДЛЯ ПРОВЕРКИ ИХ ВЫБОРА
    # булки
    BUNS = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div")
    # соусы
    SOUSES = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div")
    # начинки
    STUFFING = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div")
