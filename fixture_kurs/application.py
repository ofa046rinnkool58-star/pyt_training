from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fixture_kurs.Session import SessionHelper
from fixture_kurs.group import GroupHelper


class Application:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.wd = webdriver.Chrome(service=service)
        self.vars = {}
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self) # делает только логин и логаут
        self.group = GroupHelper(self) # делает все кроме логина и логаута

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/index.php")

    def open_groups(self):
        self.wd.find_element(By.LINK_TEXT, "groups").click()
        self.open_groups()

    def new_group_creation(self):
        self.wd.find_element(By.NAME, "new").click()

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

    def destroy(self):
        self.wd.quit()