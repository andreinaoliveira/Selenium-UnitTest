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

    def test_CT03_InvalidPassword(self):
        format.titleTest("CT03 - Senha inválida")
        self.login.login('teste@gmail.com', 'Teste@1234')
        self.assertTrue(self.login.check_error_passwordInvalid())

    def test_CT04_InvalidAccount(self):
        format.titleTest("CT04 - Usuário inválido")
        self.login.login('testeSelenium@gmail.com', 'Teste@1234')
        self.assertTrue(self.login.check_error_userInvalid())

    def test_CT05_ValidUser(self):
        format.titleTest("CT05 - Usuário Válido")
        email = input('Informe um e-mail váido: ')
        senha = input('Informe uma senha válida: ')
        print()
        self.login.login(email, senha)
        self.assertTrue(self.login.check_page_profiles())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()