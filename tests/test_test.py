from selenium import webdriver
import os


os.environ['PATH'] += r"C:\Users\egor.redkozubov\Desktop\tests_ui\seldriver"
def test_driver(driver):
    print(driver)
    # driver.get("https:google.com")