from controller import tryto

def setEmail(driver, getEmailOrNumber):
    """
    Insere o email/telefone em 'Email ou número de telefone'
    :param driver: webdriver
    :param getEmailOrNumber: Email ou número de telefone
    :return: boolean
    """
    return tryto.setByXPath(driver, 'Campo Email ou numero de telefone', '//*[@id="id_userLoginId"]', getEmailOrNumber)

def setPassword(driver, getPassword):
    """
    Insere a senha em 'Senha'
    :param driver: webdriver
    :param getPassword: Senha
    :return: boolean
    """
    return tryto.setByXPath(driver, 'Campo Senha', '//*[@id="id_password"]"]', getPassword)