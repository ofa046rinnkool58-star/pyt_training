from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from kurs.fixture_kurs.Session import SessionHelper
from kurs.fixture_kurs.group import GroupHelper


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

    def destroy(self):
        self.wd.quit()