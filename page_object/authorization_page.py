from page_object.base_app import base_page
from selenium.webdriver.common.by import By


class authorization_locators:
    LOCATOR_PHONE_LABEL = (By.CLASS_NAME, "form-label")
    LOCATOR_PHONE_FIELD = (By.ID, "phone")
    LOCATOR_CONTINUE_BUTTON = (By.CLASS_NAME, "btn-continue")
    LOCATOR_POPUP = (By.CLASS_NAME, 'boottoast-content')
    LOCATOR_PASSWORD_FIELD = (By.ID, 'password')
    LOCATOR_LOGIN_BUTTON_XPATH = (By.XPATH, '//*[@id="password_block"]/div[3]/div[2]/button')


class authorization_helper(base_page):
    def click_on_continue_button(self):
        continue_button = self.find_element(authorization_locators.LOCATOR_CONTINUE_BUTTON,time=2)
        continue_button.click()
        return continue_button

    def click_on_login_button(self):
        login_button = self.find_element(authorization_locators.LOCATOR_LOGIN_BUTTON_XPATH, time=2)
        login_button.click()
        return login_button

    def enter_phone(self, phone):
        phone_field = self.find_element(authorization_locators.LOCATOR_PHONE_FIELD)
        phone_field.send_keys(phone)
        return phone_field

    def enter_password(self, password):
        password_field = self.find_element(authorization_locators.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(password)
        return password_field

    def phone_label(self):
        return self.find_element(authorization_locators.LOCATOR_PHONE_LABEL,time=2)

    def popup(self):
        return self.find_element(authorization_locators.LOCATOR_POPUP,time=2)