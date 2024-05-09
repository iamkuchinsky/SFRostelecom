import time

from selenium.webdriver.common.by import By

from pages.auth_page import AuthPage
from pages.locators import AuthLocators
from pages.main import web_driver


def test_auth_page_phone(web_driver):
    page = AuthPage(web_driver)
    page.enter_phone("Номер телефона")  # Здесь необходимо ввести валидный номер телефона
    page.enter_pass("Пароль")  # Здесь необходимо ввести пароль с привязкой к номеру телефона
    time.sleep(5)
    page.btn_click()
    time.sleep(5)
    expected_text = "Учетные данные"
    assert expected_text in web_driver.page_source


def test_auth_page_phone_pass_inv(web_driver):
    page = AuthPage(web_driver)
    page.enter_phone("Номер телефона")  # Здесь необходимо ввести валидный email
    page.enter_pass("Неверный пароль")  # Здесь необходимо ввести неправильный пароль
    time.sleep(5)
    page.btn_click()
    time.sleep(5)
    expected_text1 = "Неверный логин или пароль"
    assert expected_text1 in web_driver.page_source


def test_auth_page_email(web_driver):
    page = AuthPage(web_driver)
    page.email_btn_click()
    page.enter_phone("Email")  # Здесь необходимо ввести валидный email
    page.enter_pass("Пароль")  # Здесь необходимо ввести пароль с привязкой к email
    time.sleep(3)
    page.btn_click()
    time.sleep(3)
    assert web_driver.find_element(By.CSS_SELECTOR, 'img.user-avatar')


def test_auth_page_email_pass_inv(web_driver):
    page = AuthPage(web_driver)
    page.email_btn_click()
    page.enter_phone("Email")  # Здесь необходимо ввести валидный email
    page.enter_pass("Пароль")  # Здесь необходимо ввести пароль с привязкой к email
    time.sleep(3)
    page.btn_click()
    time.sleep(3)
    expected_text2 = "Неверный логин или пароль"
    assert expected_text2 in web_driver.page_source


def test_auth_page_login(web_driver):
    page = AuthPage(web_driver)
    page.log_btn_click()
    page.enter_phone("Логин")  # Здесь необходимо ввести валидный логин
    page.enter_pass("Пароль")  # Здесь необходимо ввести пароль с привязкой к логину
    time.sleep(3)
    page.btn_click()
    time.sleep(3)
    expected_text3 = "Добавить личный кабинет Москвы"
    assert expected_text3 in web_driver.page_source


def test_auth_page_login_pass_inv(web_driver):
    page = AuthPage(web_driver)
    page.log_btn_click()
    page.enter_phone("Логин")  # Здесь необходимо ввести валидный логин
    page.enter_pass("Пароль")  # Здесь необходимо ввести неправильный пароль
    time.sleep(3)
    page.btn_click()
    time.sleep(3)
    expected_text4 = "Неверный логин или пароль"
    assert expected_text4 in web_driver.page_source


def test_pass_reset_link(web_driver):
    AuthPage(web_driver)
    time.sleep(3)
    forgot_pass = web_driver.find_element(*AuthLocators.AUTH_FORGOT_PASS)
    forgot_pass.click()
    assert "/reset-credentials" in web_driver.current_url


def test_registration_link(web_driver):
    page = AuthPage(web_driver)
    time.sleep(5)
    registration_link = web_driver.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name("Максим")
    page.enter_surname("Скилфакторов")
    page.enter_email_registration("dsk4938943@skillfactory.ru")
    page.enter_pass("12345678qwerty")
    page.enter_pass_confirm("12345678qwerty")
    page.registration_button_click()
    time.sleep(5)
    # проверяем, что перешли на страницу ввода кода
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


def test_registration_dif_pass(web_driver):
    page = AuthPage(web_driver)
    time.sleep(5)
    registration_link = web_driver.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name("Максим")
    page.enter_surname("Скилфакторов")
    page.enter_email_registration("dsk4938943@skillfactory.ru")
    page.enter_pass("12345678qwertyQQ")
    page.enter_pass_confirm("12345678qwertyQ")  # Необходимо ввести другой пароль
    page.registration_button_click()
    time.sleep(5)
    # проверяем, что перешли на страницу ввода кода
    expected_text5 = "Пароли не совпадают"
    assert expected_text5 in web_driver.page_source


def test_registration_pass_low_length(web_driver):
    page = AuthPage(web_driver)
    time.sleep(5)
    registration_link = web_driver.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name("Максим")
    page.enter_surname("Скилфакторов")
    page.enter_email_registration("dsk4938943@skillfactory.ru")
    page.enter_pass("1234")
    page.enter_pass_confirm("1234")
    page.registration_button_click()
    time.sleep(5)
    # проверяем, что перешли на страницу ввода кода
    expected_text6 = "Длина пароля должна быть не менее 8 символов"
    assert expected_text6 in web_driver.page_source


def test_registration_pass_latin(web_driver):
    page = AuthPage(web_driver)
    time.sleep(5)
    registration_link = web_driver.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name("Максим")
    page.enter_surname("Скилфакторов")
    page.enter_email_registration("dsk4938943@skillfactory.ru")
    page.enter_pass("1234ыфоо4вы")
    page.enter_pass_confirm("1234ыфоо4вы")
    page.registration_button_click()
    time.sleep(5)
    # проверяем, что перешли на страницу ввода кода
    expected_text7 = "Пароль должен содержать только латинские буквы"
    assert expected_text7 in web_driver.page_source


def test_registration_pass_capital(web_driver):
    page = AuthPage(web_driver)
    time.sleep(5)
    registration_link = web_driver.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name("Максим")
    page.enter_surname("Скилфакторов")
    page.enter_email_registration("dsk4938943@skillfactory.ru")
    page.enter_pass("sak93244fs")
    page.enter_pass_confirm("sak93244fs")
    page.registration_button_click()
    time.sleep(5)
    # проверяем, что перешли на страницу ввода кода
    expected_text8 = "Пароль должен содержать хотя бы одну заглавную букву"
    assert expected_text8 in web_driver.page_source


def test_registration_name_empty(web_driver):
    page = AuthPage(web_driver)
    registration_link = web_driver.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name(" ")
    page.enter_surname("Скилфакторов")
    page.enter_email_registration("dsk4938943@skillfactory.ru")
    page.enter_pass("sak93244fsSS")
    page.enter_pass_confirm("sak93244fsSS")
    page.registration_button_click()
    time.sleep(5)

    expected_text9 = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    assert expected_text9 in web_driver.page_source


def test_registration_name_digital(web_driver):
    page = AuthPage(web_driver)
    registration_link = web_driver.find_element(*AuthLocators.AUTH_REGISTRATION_LINK)
    registration_link.click()
    page.enter_name("54321")
    page.enter_surname("Скилфакторов")
    page.enter_email_registration("dsk4938943@skillfactory.ru")
    page.enter_pass("sak93244fsSS")
    page.enter_pass_confirm("sak93244fsSS")
    page.registration_button_click()
    time.sleep(5)

    expected_text10 = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    assert expected_text10 in web_driver.page_source


def test_check_elements(web_driver):
    AuthPage(web_driver)
    time.sleep(3)
    name_field = web_driver.find_element(By.CSS_SELECTOR, 'input#username')
    pass_field = web_driver.find_element(By.CSS_SELECTOR, 'input#password')
    log_btn = web_driver.find_element(By.CSS_SELECTOR, 'button#kc-login')
    tab_btn_number = web_driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-phone')
    tab_btn_mail = web_driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail')
    tab_btn_login = web_driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-login')
    assert name_field.is_displayed()
    assert pass_field.is_displayed()
    assert log_btn.is_displayed()
    assert tab_btn_number.is_displayed()
    assert tab_btn_mail.is_displayed()
    assert tab_btn_login.is_displayed()
