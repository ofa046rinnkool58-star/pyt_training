from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Application:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.wd = webdriver.Chrome(service=service)
        self.vars = {}
        self.wd.implicitly_wait(10)

    def logout(self):
        # logout
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_group_page(self):
        # return group page
        self.wd.find_element(By.LINK_TEXT, "group page").click()

    def submitting(self):
        # submit
        self.wd.find_element(By.NAME, "submit").click()

    def fill_forms(self, group):
        # fill forms
        self.wd.find_element(By.NAME, "group_name").click()
        self.wd.find_element(By.NAME, "group_name").clear()  # Добавлено
        self.wd.find_element(By.NAME, "group_name").send_keys(group.groupName)

        self.wd.find_element(By.NAME, "group_header").click()
        self.wd.find_element(By.NAME, "group_header").clear()  # Добавлено
        self.wd.find_element(By.NAME, "group_header").send_keys(group.headerName)

        self.wd.find_element(By.NAME, "group_footer").click()
        self.wd.find_element(By.NAME, "group_footer").clear()  # Добавлено
        self.wd.find_element(By.NAME, "group_footer").send_keys(group.footerName)

    def new_group_creation(self):
        self.open_groups()
        # new group creation
        self.wd.find_element(By.NAME, "new").click()

    def open_groups(self):
        # open groups
        self.wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        # login
        self.open_home_page()
        self.wd.set_window_size(1052, 841)

        user_field = self.wd.find_element(By.NAME, "user")
        user_field.clear()
        user_field.send_keys(username)

        self.wd.find_element(By.NAME, "pass").clear()
        self.wd.find_element(By.NAME, "pass").send_keys(password)

        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        # homepage
        self.wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()