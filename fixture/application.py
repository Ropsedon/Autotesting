from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application(object):

    def __init__(self):
        # executable_path - необходимая хрень под Windows
        self.driver = webdriver.Firefox(executable_path=r'D:\DevSpace\Autotesting\driver\geckodriver.exe')
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://127.0.0.1/addressbook/")

    def destroy(self):
        self.driver.quit()

