from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class CommonFuntion():
    def __init__(self,driver):
        self.driver = driver
    def login(self):
        self.driver.get('https://www.atstudy.com/')
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10,1).until(EC.visibility_of_element_located((By.XPATH,'//span[text()="登录"]'))).click()
        WebDriverWait(self.driver, 10,1).until(EC.visibility_of_element_located((By.XPATH, '//p[text()="密码登录"]'))).click()
        WebDriverWait(self.driver, 10,1).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="请输入手机号码"]'))).send_keys(17629299956)
        WebDriverWait(self.driver, 10,1).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="请输入密码"]'))).send_keys('zmm441432352@')
        WebDriverWait(self.driver, 10,1).until(EC.visibility_of_element_located((By.XPATH, '//span[text()="登录"]'))).click()


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=r'..\source_code\chromedriver.exe')
    demo = CommonFuntion(driver)
    demo.login()

