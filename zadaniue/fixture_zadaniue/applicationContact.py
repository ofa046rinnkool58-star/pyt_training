from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from zadaniue.fixture_zadaniue.SessionContact import SessionHelper
from zadaniue.fixture_zadaniue.contact import ContactHelper


class ApplicationContact:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.wd = webdriver.Chrome(service=service)
        self.vars = {}
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self) #через помощника обратиться к другому помощнику
        self.contact = ContactHelper(self)

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()