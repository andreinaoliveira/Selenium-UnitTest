import os
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from controller import log

class Element:
    def __init__(self, driver, name):
        """
        Instanciar um elemento web. Necessário atribuir valor a um dos atributos 'instancia.as_...'
        :param driver: Webdriver
        :param name: Apelido
        """
        self.driver = driver
        self.name = name
        self.element = None
        self.as_1_ID = None
        self.as_2_CLASS_NAME = None
        self.as_3_NAME = None
        self.as_4_TAG_NAME = None
        self.as_5_LINK_TEXT = None
        self.as_6_PARTIAL_LINK_TEXT = None
        self.as_7_CSS_SELECTOR = None
        self.as_8_XPATH = None

    ####################################################################################################################
    #                                                  FIND BY                                                         #
    ####################################################################################################################

    def _code(self, code):
        """
        Recebe o código e direciona para a ação respectiva de localizar um elemento e armazena em self.element da classe
        :param code: Tipo do elemento. Codigo localizado em 'as_COD_...'
        :return: None
        """
        if code == 1:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.as_1_ID))
            )
        elif code == 2:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.as_2_CLASS_NAME))
            )
        elif code == 3:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, self.as_3_NAME))
            )
        elif code == 4:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, self.as_4_TAG_NAME))
            )
        elif code == 5:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, self.as_5_LINK_TEXT))
            )
        elif code == 6:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.as_6_PARTIAL_LINK_TEXT))
            )
        elif code == 7:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.as_7_CSS_SELECTOR))
            )
        elif code == 8:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.as_8_XPATH))
            )
        else:
            log.error('Código informado em find() fora do range ou inválido.')
            os.system("pause")
            sys.exit()

    def find(self, code):
        """
        Encontra um elemento web.
        :param code: Tipo do elemento. Codigo localizado em 'as_COD_...'
        :return: boolean
        """
        try:
            log.degub('Buscando ' + self.name)
            self._code(code)
        except Exception as e:
            log.error('Erro ao identificar ' + self.name)
            return False
        else:
            log.info(self.name + ' Identificado(a)')
            return True

    ####################################################################################################################
    #                                                CLICK BY                                                          #
    ####################################################################################################################

    def click(self, code):
        """
        Clica em um elemento web.
        :param code: Tipo do elemento. Codigo localizado em 'as_COD_...'
        :return: boolean
        """
        Element.find(self, code)
        try:
            self.element.click()
        except Exception as e:
            log.error('Erro ao clicar em ' + self.name)
            return False
        else:
            log.info(self.name + ' Clicado(a)')
            return True

    ####################################################################################################################
    #                                                  SET BY                                                          #
    ####################################################################################################################

    def set(self, code, info):
        """
        Insere uma informação em um elemento web.
        :param code: Tipo do elemento. Codigo localizado em 'as_COD_...'
        :param info: informação
        :return: boolean
        """
        Element.find(self, code)
        try:
            self.element.send_keys(info)
        except Exception as e:
            log.error('Erro ao escerver ' + self.name)
            return False
        else:
            log.info(self.name + ' Inserido(a)')
            return True

    ####################################################################################################################
    #                                                  GET BY                                                          #
    ####################################################################################################################
    # Em andamento
