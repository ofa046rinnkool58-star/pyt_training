from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fixture.Session import SessionHelper
from fixture.group import GroupHelper

class Cont_application:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.wd = webdriver.Chrome(service=service)
        self.vars = {}
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_page(self):
        self.driver.get("http://localhost/addressbook/index.php")
        self.driver.set_window_size(1202, 898)

