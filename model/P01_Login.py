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

    def _check_page_login(self):
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
        e.as_7_CSS_SELECTOR = 'a[href="/"]'

        return e.find(7)

    def check_error_passwordInvalid(self):
        """
        Checa se a mensagem de erro é apresentada.
        :return: boolean
        """
        e = Element(self.driver, '[Login] Reset your password')
        e.as_7_CSS_SELECTOR = 'a[href="/loginHelp"]'
        return e.find(7)

    ####################################################################################################################
    #                                                Click                                                             #
    ####################################################################################################################

    def click_signin_welcome(self):
        """
        Clica no botão Sign In da tela Welcome
        :return: boolean
        """
        e = Element(self.driver, '[Welcome] Sign In button')
        e.as_7_CSS_SELECTOR = 'a[href="/login"]'
        return e.click(7)

    def click_signin_login(self):
        """
        Clica no botão Sign In da tela Login
        :return: boolean
        """
        e = Element(self.driver, '[Login] Sign In button')
        e.as_2_CLASS_NAME = 'login-button'
        return e.click(2)

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

    ####################################################################################################################
    #                                                ACTIONS                                                           #
    ####################################################################################################################

    def login(self, email_or_number, password):
        self.check_page_welcome()
        self.click_signin_welcome()
        self.check_page_login()
        self.set_email(email_or_number)
        self.set_password(password)
        self.click_signin_login()
        return 1