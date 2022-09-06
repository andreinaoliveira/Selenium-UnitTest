from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from controller import format
from model.P01_Login import Login
import unittest

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://www.netflix.com/br/')
        self.login = Login(self.driver)

    def test_CT01_AccessWelcome(self):
        format.titleTest("CT01 - Acessar tela de Boas Vindas")
        self.assertTrue(self.login.check_page_welcome())

    def test_CT02_AccessLogin(self):
        format.titleTest("CT02 - Acessar tela de login")
        self.login.click_signin_welcome()
        self.assertTrue(self.login.check_page_login())

    def test_CT03_InvalidPassword(self):
        format.titleTest("CT03 - Senha inválida")
        self.login.click_signin_welcome()
        self.login.set_email('teste@gmail.com')
        self.login.set_password('Teste@1234')
        self.login.click_signin_login()
        self.assertTrue(self.login.check_error_passwordInvalid())

    def test_CT04_InvalidAccount(self):
        format.titleTest("CT04 - Usuário inválido")
        self.login.click_signin_welcome()
        self.login.set_email('testeSelenium@gmail.com')
        self.login.set_password('Teste@1234')
        self.login.click_signin_login()
        self.assertTrue(self.login.check_error_userInvalid())

    def test_CT05_ValidUser(self):
        format.titleTest("CT05 - Usuário Válido")
        self.login.click_signin_welcome()

        email = input('Informe um e-mail váido: ')
        senha = input('Informe uma senha válida: ')

        self.login.set_email(email)
        self.login.set_password(senha)
        self.login.click_signin_login()
        self.assertTrue(self.login.check_page_profiles())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()