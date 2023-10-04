import pytest
from selenium import webdriver
from aqa_py.lesson_28.schema.main_page import Main_Page
def test_check_enable_button ():
    page = Main_Page()
    page.open_home_page()
    page.about_button()
    page.check_enable_button()


