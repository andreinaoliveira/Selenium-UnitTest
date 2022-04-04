from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from controller import log

class Element:
    def __init__(self, driver, name):
        """
        Instanciar um elemento web. Necessário atribuir valor a um dos atributos 'instancia.as_'
        :param driver: Webdriver
        :param name: Apelido
        """
        self.driver = driver
        self.name = name
        self.as_id = None
        self.as_class = None
        self.as_css = None
        self.as_xpath = None
        self.as_text = None

    ####################################################################################################################
    #                                                  FIND BY                                                         #
    ####################################################################################################################

    def find_by_id(self):
        """
        Encontra um elemento web.
        :return: boolean
        """
        global element
        try:
            log.degub('Buscando ' + self.name)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.as_id))
            )
        except Exception as e:
            log.error('Erro ao identificar ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Identificado(a)')
            return True

    def find_by_class(self):
        """
        Encontra um elemento web.
        :return: boolean
        """
        global element
        try:
            log.degub('Buscando ' + self.name)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.as_class))
            )
        except Exception as e:
            log.error('Erro ao identificar ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Identificado(a)')
            return True

    def find_by_css(self):
        """
        Encontra um elemento web.
        :return: boolean
        """
        global element
        try:
            log.degub('Buscando ' + self.name)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.as_css))
            )
        except Exception as e:
            log.error('Erro ao identificar ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Identificado(a)')
            return True

    def find_by_xpath(self):
        """
        Encontra um elemento web.
        :return: boolean
        """
        global element
        try:
            log.degub('Buscando ' + self.name)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.as_xpath))
            )
        except Exception as e:
            log.error('Erro ao identificar ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Identificado(a)')
            return True

    def find_by_text(self):
        """
        Encontra um elemento web.
        :return: boolean
        """
        global element
        try:
            log.degub('Buscando ' + self.name)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.as_text))
            )
        except Exception as e:
            log.error('Erro ao identificar ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Identificado(a)')
            return True

    ####################################################################################################################
    #                                                CLICK BY                                                          #
    ####################################################################################################################

    def _click(self):
        try:
            element.click()
        except Exception as e:
            log.error('Erro ao clicar em ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Clicado(a)')
            return True

    def click_by_id(self):
        """
        Clica em um elemento web.
        :return: boolean
        """
        Element.find_by_id(self)
        return Element._click(self)

    def click_by_class(self):
        """
        Clica em um elemento web.
        :return: boolean
        """
        Element.find_by_class(self)
        return Element._click(self)

    def click_by_css(self):
        """
        Clica em um elemento web.
        :return: boolean
        """
        Element.find_by_css(self)
        return Element._click(self)

    def click_by_xpath(self):
        """
        Clica em um elemento web.
        :return: boolean
        """
        Element.find_by_xpath(self)
        return Element._click(self)

    def click_by_text(self):
        """
        Clica em um elemento web.
        :return: boolean
        """
        Element.find_by_text(self)
        return Element._click(self)

    ####################################################################################################################
    #                                                  SET BY                                                          #
    ####################################################################################################################

    def _set(self, info):
        try:
            element.send_keys(info)
        except Exception as e:
            log.error('Erro ao escerver ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Inserido(a)')
            return True

    def set_by_id(self, info):
        """
        Insere uma informação em um elemento web.
        :param info: informação
        :return: boolean
        """
        Element.find_by_id(self)
        return Element._set(self, info)

    def set_by_class(self, info):
        """
        Insere uma informação em um elemento web.
        :param info: informação
        :return: boolean
        """
        Element.find_by_class(self)
        return Element._set(self, info)

    def set_by_css(self, info):
        """
        Insere uma informação em um elemento web.
        :param info: informação
        :return: boolean
        """
        Element.find_by_css(self)
        return Element._set(self, info)

    def set_by_xpath(self, info):
        """
        Insere uma informação em um elemento web.
        :param info: informação
        :return: boolean
        """
        Element.find_by_xpath(self)
        return Element._set(self, info)

    def set_by_text(self, info):
        """
        Insere uma informação em um elemento web.
        :param info: informação
        :return: boolean
        """
        Element.find_by_text(self)
        return Element._set(self, info)

    ####################################################################################################################
    #                                                  GET BY                                                          #
    ####################################################################################################################
    # Em andamento
