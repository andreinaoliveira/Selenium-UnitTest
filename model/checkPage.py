from controller.webdriver import Element


def welcome(driver):
    """
    Checa se o navegador está na página.
    :param driver: webdriver
    :return: boolean
    """
    w = Element(driver, 'Bem vindo')
    w.as_class = 'our-story-card-title'
    return w.find_by_class()
