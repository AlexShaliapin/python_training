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
    self.driver.find_element(By.NAME, "first_name").send_keys("qq")
    self.driver.find_element(By.NAME, "last_name").send_keys("ww")
    self.driver.find_element(By.CSS_SELECTOR, ".city").send_keys("ee")
    self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("rr")
    self.driver.find_element(By.CSS_SELECTOR, "#submit_button").click()
  
