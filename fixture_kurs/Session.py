# делает только логин и логаут
from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.set_window_size(1052, 841)

        user_field = wd.find_element(By.NAME, "user")
        user_field.clear()
        user_field.send_keys(username)

        pass_field = wd.find_element(By.NAME, "pass")
        pass_field.clear()
        pass_field.send_keys(password)

        wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()