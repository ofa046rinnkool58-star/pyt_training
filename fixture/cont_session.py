from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Cont_sessionHelper:
    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def login(self, login, password):
        wd = self.app.wd
        self.wd.find_element(By.NAME, "user").send_keys("%s" % login)
        self.wd.find_element(By.NAME, "pass").click()
        self.wd.find_element(By.NAME, "pass").send_keys("%s" % password)
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def save_and_logout(self):
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(71)").click()

        WebDriverWait(self.wd, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "home"))
        ).click()

        self.wd.find_element(By.LINK_TEXT, "Logout").click()