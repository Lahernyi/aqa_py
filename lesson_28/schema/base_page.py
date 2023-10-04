from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, ):
        pass

    def open_home_page(self):
        user = "guest"
        passw = "welcome2qauto"
        url = f"https://{user}:{passw}@qauto.forstudy.space/"
        driver = webdriver.Chrome()
        driver.get(url)


    def is_element_present(self, driver, elem):
        try:
            driver.find_element(By. XPATH, elem)
        except NoSuchElementException:
            return False
        return True

    def get_element(self, driver, elem):
        try:
            element = driver.find_element(By.XPATH, elem)
        except NoSuchElementException:
            return False
        return element