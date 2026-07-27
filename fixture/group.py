from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups(self):
        wd = self.app.wd
        self.app.wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self):
        self.open_groups()
        self.app.wd.find_element(By.NAME, "new").click()

    def fill_forms(self, group):
        # Название группы
        name_field = self.wd.find_element(By.NAME, "group_name")
        name_field.click()
        name_field.clear()
        name_field.send_keys(group.groupName)

        # Заголовок
        header_field = self.wd.find_element(By.NAME, "group_header")
        header_field.click()
        header_field.clear()
        header_field.send_keys(group.headerName)

        # Футер
        footer_field = self.wd.find_element(By.NAME, "group_footer")
        footer_field.click()
        footer_field.clear()
        footer_field.send_keys(group.footerName)

    def submitting(self):
        self.wd.find_element(By.NAME, "submit").click()

    def return_to_group_page(self):
        self.wd.find_element(By.LINK_TEXT, "group page").click()