from controller.webdriver import Element

def set_email(driver, email_or_number):
    """
    Insere o email ou telefone
    :param driver:
    :param email_or_number:
    :return: boolean
    """
    e = Element(driver, 'email')
    e.as_id = 'id_userLoginId'
    return e.set_by_id(email_or_number)

def set_password(driver, password):
    """
    Insere senha
    :param driver: webdriver
    :param password: senha
    :return:
    """
    p = Element(driver, 'password')
    p.as_id = 'id_password'
    return p.set_by_id(password)

def click_sigin_welcome(driver):
    """
    Clica no botão Sign In da tela Welcome
    :param driver: webdriver
    :return: boolean
    """
    s = Element(driver, 'botão sign in de Welcome')
    s.as_class = 'redButton'
    return s.click_by_xpath()

def click_signin_login(driver):
    """
    Clica no botão Sign In da tela Login
    :param driver: webdriver
    :return: boolean
    """
    s = Element(driver, 'botão sign in de Login')
    s.as_class = 'login-button'
    return s.click_by_xpath()