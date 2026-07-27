from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from fixture.cont_session import SessionHelper


class ContactHelper:
    def __init__(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        service = Service(ChromeDriverManager().install())
        self.wd = webdriver.Chrome(service=service)
        self.wd.implicitly_wait(10)

        self.session = SessionHelper(self)
        self.contact = self

    def open_home_page(self):
        """Открывает главную страницу"""
        self.wd.get("http://localhost/addressbook/index.php")
        self.wd.set_window_size(1202, 898)

    def open_page(self):
        self.open_home_page()
        return self

    def new_contact(self):
        WebDriverWait(self.wd, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "add new"))
        ).click()

    def fill_contact(self, contact):
        field = self.wd.find_element(By.NAME, "firstname")
        field.click()
        field.clear()
        if contact.firstname is not None:
            field.send_keys(contact.firstname)

        field = self.wd.find_element(By.NAME, "middlename")
        field.click()
        field.clear()
        if contact.middlename is not None:
            field.send_keys(contact.middlename)

        field = self.wd.find_element(By.NAME, "lastname")
        field.click()
        field.clear()
        if contact.lastname is not None:
            field.send_keys(contact.lastname)

        field = self.wd.find_element(By.NAME, "nickname")
        field.click()
        field.clear()
        if contact.nickname is not None:
            field.send_keys(contact.nickname)

        field = self.wd.find_element(By.NAME, "address")
        field.click()
        field.clear()
        if contact.address is not None:
            field.send_keys(contact.address)

        field = self.wd.find_element(By.NAME, "home")
        field.click()
        field.clear()
        if contact.home is not None:
            field.send_keys(contact.home)

        field = self.wd.find_element(By.NAME, "mobile")
        field.click()
        field.clear()
        if contact.mobile is not None:
            field.send_keys(contact.mobile)

        field = self.wd.find_element(By.NAME, "work")
        field.click()
        field.clear()
        if contact.work is not None:
            field.send_keys(contact.work)

        field = self.wd.find_element(By.NAME, "email")
        field.click()
        field.clear()
        if contact.email is not None:
            field.send_keys(contact.email)

        field = self.wd.find_element(By.NAME, "email2")
        field.click()
        field.clear()
        if contact.email2 is not None:
            field.send_keys(contact.email2)

        field = self.wd.find_element(By.NAME, "email3")
        field.click()
        field.clear()
        if contact.email3 is not None:
            field.send_keys(contact.email3)

    def submit_contact(self):
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(71)").click()

    def return_to_home_page(self):
        WebDriverWait(self.wd, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "home"))
        ).click()

    def create_contact(self, contact):
        self.new_contact()
        self.fill_contact(contact)
        self.submit_contact()
        self.return_to_home_page()

    def destroy(self):
        self.wd.quit()