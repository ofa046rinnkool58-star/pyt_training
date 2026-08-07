from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form()
        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.LINK_TEXT, "group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        self.select_first_group()
        wd.find_element(By.NAME, "delete").click()
        wd.find_element(By.LINK_TEXT, "group page").click()

    def change_first_group(self, new_group_data):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        self.select_first_group()
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element(By.NAME, "update").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.groupName)
        self.change_field_value("group_header", group.headerName)
        self.change_field_value("group_footer", group.footerName)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            name_field = wd.find_element(By.NAME, field_name)
            name_field.click()
            name_field.clear()
            name_field.send_keys(text)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()