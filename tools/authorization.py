import time



def authorization(driver, user_with_my_personal_number_xd):
    driver.get("https://lk.test.izanyat.ru/")
    form_label = None
    while form_label== None:
        try:
            form_label = driver.find_element_by_class_name('form-label')
        except Exception:
            continue
    login, password = user_with_my_personal_number_xd
    if form_label.text != 'Номер мобильного телефона':
        print('wrong text')
        driver.quit

    login_form = driver.find_element_by_id('phone')
    login_form.send_keys(login)
    btn_continue = driver.find_element_by_class_name('btn-continue')
    btn_continue.click()
    popup = None
    while popup is None:
        try:
            popup = driver.find_element_by_class_name('boottoast-content')
        except Exception:
            pass


    password_form = None

    while password_form is None:
        try:
            password_form = driver.find_element_by_id('password')
            password_form.send_keys(password)
        except Exception:
            continue
    btn_continue = driver.find_element_by_xpath('//*[@id="password_block"]/div[3]/div[2]/button')
    btn_continue.click()
