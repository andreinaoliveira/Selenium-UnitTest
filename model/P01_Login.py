from controller.webdriver import Element

class Login:
    def __init__(self, driver):
        self.driver = driver
    ####################################################################################################################
    #                                                  CHECK                                                           #
    ####################################################################################################################

    def check_page_welcome(self):
        """
        Checa se o navegador está na página.
        :return: boolean
        """
        p = Element(self.driver, '[Welcome] Page')
        p.as_2_CLASS_NAME = 'our-story-card-title'
        return p.find(2)

    def check_page_login(self):
        """
        Checa se o navegador está na página.
        :return: boolean
        """
        p = Element(self.driver, '[Login] Page')
        p.as_2_CLASS_NAME = 'hybrid-login-form-main'
        return p.find(2)

    def check_page_profiles(self):
        """
        Checa se o navegador está na página.
        :return: boolean
        """
        p = Element(self.driver, '[Login] Profiles')
        p.as_2_CLASS_NAME = 'profile-gate-label'
        return p.find(2)

    def check_error_userInvalid(self):
        """
        Checa se a mensagem de erro é apresentada.
        :return: boolean
        """
        e = Element(self.driver, '[Login] Create a new account')
        e.as_5_LINK_TEXT = 'create a new account'
        return e.find(5)

    def check_error_passwordInvalid(self):
        """
        Checa se a mensagem de erro é apresentada.
        :return: boolean
        """
        e = Element(self.driver, '[Login] Reset your password')
        e.as_6_PARTIAL_LINK_TEXT = 'reset your password'
        return e.find(6)

    ####################################################################################################################
    #                                                Click                                                             #
    ####################################################################################################################

    def click_signin_welcome(self):
        """
        Clica no botão Sign In da tela Welcome
        :param driver: webdriver
        :return: boolean
        """
        s = Element(self.driver, '[Welcome] Sign In button')
        s.as_5_LINK_TEXT = 'Sign In'
        return s.click(5)

    def click_signin_login(self):
        """
        Clica no botão Sign In da tela Login
        :param driver: webdriver
        :return: boolean
        """
        s = Element(self.driver, '[Login] Sign In button')
        s.as_2_CLASS_NAME = 'login-button'
        return s.click(2)

    ####################################################################################################################
    #                                                  SET                                                             #
    ####################################################################################################################

    def set_email(self, email_or_number):
        """
        Insere o email ou telefone
        :param email_or_number: e-mail ou número
        :return: boolean
        """
        e = Element(self.driver, '[Login] Email')
        e.as_1_ID = 'id_userLoginId'
        return e.set(1, email_or_number)

    def set_password(self, password):
        """
        Insere senha
        :param password: senha
        :return: boolean
        """
        p = Element(self.driver, '[Login] Password')
        p.as_1_ID = 'id_password'
        return p.set(1, password)
