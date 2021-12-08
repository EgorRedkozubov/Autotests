import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path=r"C:\Users\egor.redkozubov\Desktop\tests_ui\seldriver\chromedriver.exe")
    yield driver
    driver.quit()

