from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def login(self, username, password):
        self.app.open_home_page()
        self.wd.set_window_size(1052, 841)

        user_field = self.wd.find_element(By.NAME, "user")
        user_field.clear()
        user_field.send_keys(username)

        pass_field = self.wd.find_element(By.NAME, "pass")
        pass_field.clear()
        pass_field.send_keys(password)

        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()