from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test1(self):
    self.driver.get("https://suninjuly.github.io/simple_form_find_task.html")
    self.driver.set_window_size(1440, 821)
    self.driver.find_element(By.XPATH, "//input[@name=\'first_name\']").click()
    self.driver.find_element(By.XPATH, "//input[@name=\'first_name\']").send_keys("qqq")
    self.driver.find_element(By.XPATH, "//input[@name=\'last_name\']").click()
    self.driver.find_element(By.XPATH, "//input[@name=\'last_name\']").send_keys("www")
    self.driver.find_element(By.XPATH, "//input[@name=\'firstname\']").click()
    self.driver.find_element(By.XPATH, "//input[@name=\'firstname\']").send_keys("eee")
    self.driver.find_element(By.XPATH, "//input[@id=\'country\']").click()
    self.driver.find_element(By.XPATH, "//input[@id=\'country\']").send_keys("rrr")
    self.driver.find_element(By.XPATH, "//button[@id=\'submit_button\']").click()
  
