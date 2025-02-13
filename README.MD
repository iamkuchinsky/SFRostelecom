В данном задании реализованы тест-кейсы для сайта https://b2c.passport.rt.ru/. Все тесты запускаются через "RUN".

1. Содержание:
base_page.py - классы для страницы авторизации необходимые для проведения тестирования.
locators.py - локаторы
main.py - фикстура, предназначена для инициализации и предоставления экземпляра веб-драйвера Selenium WebDriver для браузера Chrome.
auth_page.py - все переменные, используемые в автотестах
test_file.py - все автотесты со всеми проверками, перечисленными в тест-кейсах.
2. Ссылка на папку с тест-кейсами по ручному тестированию и баг-репорт:
https://drive.google.com/drive/folders/1kYt5pnYNf5ypV_V-y_eAfQWpcstudVBY?usp=drive_link
3. В файле test_file.py:
1) test_auth_page_phone: Проверяет, что вход с номером телефона успешен, имеется текст со страницы личного кабинета.
2) test_auth_page_phone_pass_inv : Проверяет, что вход с валидным номером и неверным паролем не совершается, выходит ошибка.
3) test_auth_page_email: Проверяет, что вход по email успешен имеется атрибут страницы личного кабинета.
4) test_auth_page_email_pass_inv: Проверяет, что вход с валидным email и неверным паролем не совершается, выходит ошибка.
5) test_auth_page_login: Проверяет, что вход по логину успешен, имеется текст со страницы личного кабинета.
6) test_auth_page_login_pass_inv: Проверяет, что вход с валидным логином и неверным паролем не совершается, выходит ошибка.
7) test_pass_reset_link: Проверяет, что после нажатия кнопки "Забыл пароль" мы оказываемся на странице сброса пароля.
8) test_registration_link: Проверяет, что после нажатия кнопки "Регистрация" мы оказываемся на странице регистрации.
9) test_registration_dif_pass: Проверяет, что при вводе разных паролей при регистрации, выходит ошибка.
10) test_registration_pass_low_length: Проверяет, что при вводе паролей при регистрации менее 8 символов, выходит ошибка.
11) test_registration_pass_latin: Проверяет, что при вводе паролей при регистрации без латинских символов выходит ошибка.
12) test_registration_pass_capital: Проверяет, что при вводе паролей при регистрации без хотя бы 1 заглавной буквы, выходит ошибка.
13) test_registration_name_empty: Проверяет обработку ошибки при попытке зарегистрироваться с пустым именем.
14) test_registration_name_digital: Проверяет обработку ошибки при попытке зарегистрироваться с именем, содержащим цифры.
test_check_elements - Проверяет, что на форме авторизации отображаются основные элементы:
15) Поле ввода номера телефона
16) Поле ввода пароля
17) Таб номер телефона
18) Таб почта
19) Таб Логин
20) Кнопка "Войти"

4. В работе используются методы и техники тест-дизайна:
- Функциональное тестирование - проверка основных функций системы, таких как успешный вход, обработка ошибок при регистрации и авторизации.
- Граничные значения: (например, Проверка смены пароля на предыдущие пароли включает в себя проверку требований к паролю при регистрации, где возможно использование предыдущих паролей.)
- Разбиение на классы эквивалентности: (например, в тестах, которые проверяют успешный вход с номером телефона, email, логином, или в тестах, которые проверяют ошибки при вводе неверных данных или пустых значений)
- Тестирование пользовательского интерфейса (например, в тестах которые проверяют отображение основных элементов на форме авторизации.)

