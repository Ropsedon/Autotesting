# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
    
    def test_add_group(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_group(driver, Group(name="sdfafas", header="asdfsa", footer="asdfsadf"))
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.login(driver, username="admin", password="secret")
        self.create_group(driver, Group(name="", header="", footer=""))
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, driver):
        # Return to groups page
        driver.find_element_by_link_text("groups").click()

    def create_group(self, driver, group):
        self.open_groups_page(driver)
        # Init group creation
        driver.find_element_by_name("new").click()
        # Fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page(driver)

    def open_groups_page(self, driver):
        driver.find_element_by_link_text("groups").click()

    def login(self, driver, username, password):
        self.open_home_page(driver)
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_id("LoginForm").submit()

    def open_home_page(self, driver):
        driver.get("http://127.0.0.1/addressbook/")
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
