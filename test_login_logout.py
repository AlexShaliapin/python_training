from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_login_logout():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def open_home_page(self):
        # open home page
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.set_window_size(1440, 821)

    def login(self, username, password):
        # login
        self.open_home_page()
        self.driver.find_element(By.XPATH, "//input[@id=\'username\']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id=\'password\']").send_keys(password)

    def submit_login(self):
        # submit login
        self.driver.find_element(By.XPATH, "//button[@id=\'submit\']").click()

    def logout(self):
        # logout
        self.driver.find_element(By.XPATH, "//a[contains(text(),\'Log out\')]").click()

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_logout(self):
        self.open_home_page()
        self.login(username="student", password="Password123")
        self.submit_login()
        self.logout()
        