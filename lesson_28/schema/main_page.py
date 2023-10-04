import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from aqa_py.lesson_28.schema.base_page import BasePage

class Main_Page():

    def __init__(self):
        
    def open_home_page():
        user = "guest"
        passw = "welcome2qauto"
        url = f"https://{user}:{passw}@qauto.forstudy.space/"
        driver = webdriver.Chrome()
        driver.get(url)
        return driver

    def about_button(driver):
        element = driver.find_element(By.XPATH, '//button [@class="btn header-link"]')
        return element

    def check_enable_button (element):
        result = element.is_displayed()
        return result










