from page_object.authorization_page import  authorization_helper
import time


def test_authorization(browser, user_with_my_personal_number_xd):
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
    authorization_page.enter_phone(phone)
    authorization_page.click_on_continue_button()
    time.sleep(2)
    authorization_page.enter_password(password)
    authorization_page.click_on_login_button()

