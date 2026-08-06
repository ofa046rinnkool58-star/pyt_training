from selenium.webdriver.common.by import By

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.LINK_TEXT, "add new").click()
        field = wd.find_element(By.NAME, "firstname")
        field.click()
        field.clear()
        field.send_keys(contact.firstname)

        field = wd.find_element(By.NAME, "middlename")
        field.click()
        field.clear()
        field.send_keys(contact.middlename)

        field = wd.find_element(By.NAME, "lastname")
        field.click()
        field.clear()
        field.send_keys(contact.lastname)

        field = wd.find_element(By.NAME, "nickname")
        field.click()
        field.clear()
        field.send_keys(contact.nickname)

        field = wd.find_element(By.NAME, "address")
        field.click()
        field.clear()
        field.send_keys(contact.address)

        field = wd.find_element(By.NAME, "home")
        field.click()
        field.clear()
        field.send_keys(contact.home)

        field = wd.find_element(By.NAME, "mobile")
        field.click()
        field.clear()
        field.send_keys(contact.mobile)

        field = wd.find_element(By.NAME, "work")
        field.click()
        field.clear()
        field.send_keys(contact.work)

        field = wd.find_element(By.NAME, "email")
        field.click()
        field.clear()
        field.send_keys(contact.email)

        field = wd.find_element(By.NAME, "email2")
        field.click()
        field.clear()
        field.send_keys(contact.email2)

        field = wd.find_element(By.NAME, "email3")
        field.click()
        field.clear()
        field.send_keys(contact.email3)

        wd.find_element(By.CSS_SELECTOR, "input:nth-child(71)").click()
        wd.find_element(By.LINK_TEXT, "home").click()