import time

from selenium import webdriver
from controller import format
from model import login
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
        self.driver.get('https://www.netflix.com/br-en/')

    def test_CT01_AccessWelcome(self):
        format.titleTest("CT01 - Acessar tela de Boas Vindas")
        self.assertTrue(login.check_page_welcome(self.driver))

    def test_CT02_AccessLogin(self):
        format.titleTest("CT02 - Acessar tela de login")
        login.click_signin_welcome(self.driver)
        self.assertTrue(login.check_page_login(self.driver))

    def test_CT03_InvalidAccount(self):
        format.titleTest("CT03 - User e Password inválidos")
        login.click_signin_welcome(self.driver)
        login.set_email(self.driver, 'testeSelenium@gmail.com')
        login.set_password(self.driver, 'Teste@1234')
        login.click_signin_login(self.driver)
        self.assertTrue(login.check_userInvalid(self.driver))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()