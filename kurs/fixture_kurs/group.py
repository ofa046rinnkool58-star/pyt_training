from selenium.webdriver.common.by import By

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()
        # Название группы
        name_field = wd.find_element(By.NAME, "group_name")
        name_field.click()
        name_field.clear()
        name_field.send_keys(group.groupName)
        # Заголовок
        header_field = wd.find_element(By.NAME, "group_header")
        header_field.click()
        header_field.clear()
        header_field.send_keys(group.headerName)
        # Футер
        footer_field = wd.find_element(By.NAME, "group_footer")
        footer_field.click()
        footer_field.clear()
        footer_field.send_keys(group.footerName)
        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.LINK_TEXT, "group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        #select_first_group
        wd.find_element(By.NAME, "selected[]").click()
        #submit deletion
        wd.find_element(By.NAME, "delete").click()
        wd.find_element(By.LINK_TEXT, "group page").click()

    def change_group(self, group):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "edit").click()
        name_field = wd.find_element(By.NAME, "group_name")
        name_field.click()
        name_field.clear()
        name_field.send_keys(group.groupName)
        # Заголовок
        header_field = wd.find_element(By.NAME, "group_header")
        header_field.click()
        header_field.clear()
        header_field.send_keys(group.headerName)
        # Футер
        footer_field = wd.find_element(By.NAME, "group_footer")
        footer_field.click()
        footer_field.clear()
        footer_field.send_keys(group.footerName)
        wd.find_element(By.NAME, "update").click()