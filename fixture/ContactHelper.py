from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ContactHelper:
    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def open_page(self):
        """Открывает главную страницу"""
        self.wd.get("http://localhost/addressbook/index.php")
        self.wd.set_window_size(1202, 898)

    def new_contact(self):
        """Переходит к созданию нового контакта"""
        WebDriverWait(self.wd, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "add new"))
        ).click()

    def fill_contact(self, contact):
        """Заполняет форму контакта"""
        # Заполняем имя
        field = self.wd.find_element(By.NAME, "firstname")
        field.click()
        field.clear()
        if contact.firstname is not None:
            field.send_keys(contact.firstname)

        # Заполняем отчество
        field = self.wd.find_element(By.NAME, "middlename")
        field.click()
        field.clear()
        if contact.middlename is not None:
            field.send_keys(contact.middlename)

        # Заполняем фамилию
        field = self.wd.find_element(By.NAME, "lastname")
        field.click()
        field.clear()
        if contact.lastname is not None:
            field.send_keys(contact.lastname)

        # Заполняем никнейм
        field = self.wd.find_element(By.NAME, "nickname")
        field.click()
        field.clear()
        if contact.nickname is not None:
            field.send_keys(contact.nickname)

        # Заполняем адрес
        field = self.wd.find_element(By.NAME, "address")
        field.click()
        field.clear()
        if contact.address is not None:
            field.send_keys(contact.address)

        # Заполняем домашний телефон
        field = self.wd.find_element(By.NAME, "home")
        field.click()
        field.clear()
        if contact.home is not None:
            field.send_keys(contact.home)

        # Заполняем мобильный телефон
        field = self.wd.find_element(By.NAME, "mobile")
        field.click()
        field.clear()
        if contact.mobile is not None:
            field.send_keys(contact.mobile)

        # Заполняем рабочий телефон
        field = self.wd.find_element(By.NAME, "work")
        field.click()
        field.clear()
        if contact.work is not None:
            field.send_keys(contact.work)

        # Заполняем email
        field = self.wd.find_element(By.NAME, "email")
        field.click()
        field.clear()
        if contact.email is not None:
            field.send_keys(contact.email)

        # Заполняем email2
        field = self.wd.find_element(By.NAME, "email2")
        field.click()
        field.clear()
        if contact.email2 is not None:
            field.send_keys(contact.email2)

        # Заполняем email3
        field = self.wd.find_element(By.NAME, "email3")
        field.click()
        field.clear()
        if contact.email3 is not None:
            field.send_keys(contact.email3)

    def submit_contact(self):
        """Сохраняет контакт"""
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(71)").click()

    def return_to_home_page(self):
        """Возвращается на главную страницу"""
        WebDriverWait(self.wd, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "home"))
        ).click()

    def create_contact(self, contact):
        """Создает новый контакт (полный цикл)"""
        self.new_contact()
        self.fill_contact(contact)
        self.submit_contact()
        self.return_to_home_page()

    def destroy(self):
        self.wd.quit()