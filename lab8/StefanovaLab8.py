# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class StefanovaLab8(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.austincc.edu/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_stefanova_lab8(self):
        driver = self.driver
        driver.get(self.base_url + "/calendars/academic-calendar")
        driver.find_element_by_xpath("//img[contains(@src,'http://www.austincc.edu/sites/default/files/menuicon.jpg')]").click()
        driver.find_element_by_css_selector("li.leaf.menu-mlid-8397 > a").click()
        driver.find_element_by_link_text("Assessment").click()
        driver.find_element_by_link_text("Libraries").click()
        driver.find_element_by_link_text("Career Center").click()
        driver.find_element_by_link_text("Departments & Divisions").click()
        Select(driver.find_element_by_id("edit-field-instructional-division-value")).select_by_visible_text("Adult Education")
        Select(driver.find_element_by_id("edit-field-instructional-title-value")).select_by_visible_text("Dean")
        driver.find_element_by_link_text("Tasha Davis").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
