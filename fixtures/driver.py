import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    return driver