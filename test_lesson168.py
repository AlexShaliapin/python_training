from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLesson168():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_lesson168(self):
    self.driver.get("https://suninjuly.github.io/find_xpath_form")
    self.driver.set_window_size(1440, 822)
    self.driver.find_element(By.XPATH, "//input[@name=\'first_name\']").send_keys("first name")
    self.driver.find_element(By.XPATH, "//input[@name=\'last_name\']").send_keys("last name")
    self.driver.find_element(By.XPATH, "//input[@name=\'firstname\']").send_keys("city")
    self.driver.find_element(By.XPATH, "//input[@id=\'country\']").send_keys("country")
    self.driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()



