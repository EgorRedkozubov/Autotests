from page_object.authorization_page import  authorization_helper
import time
from marks import *
import allure

@allure.feature("Авторизация")
@allure.story("Открываем страницу авторизации, и входим с тестовыми данными на сайт")
@authorization
def test_authorization(browser, user_with_my_personal_number_xd):
    with allure.step("Открываем сайт и ждем появления окна ввода телефона"):
        phone, password = user_with_my_personal_number_xd
        authorization_page = authorization_helper(browser)

        authorization_page.go_to_site()
        switch = 0
        while switch !=0:
            try:
                ready_for_authorization = authorization_page.phone_label()
                if ready_for_authorization is not None:
                    switch = 1
            except Exception:
                continue
    with allure.step("Вводим телефон и переходим на страницу ввода пароля"):
        authorization_page.enter_phone(phone)
        authorization_page.click_on_continue_button()
        time.sleep(1)
    with allure.step("Вводим пароль и логинимся"):
        authorization_page.enter_password(password)
        authorization_page.click_on_login_button()

