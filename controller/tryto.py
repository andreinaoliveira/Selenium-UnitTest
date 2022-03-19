from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from controller import log

class Element:
    def __init__(self, driver, name):
        self.driver = driver
        self.name = name
        self.id_reference = None
        self.class_reference = None
        self.css_reference = None
        self.xpath_reference = None
        # self.id_element = reference if type == 'id' else None
        # self.class_element = reference if type == 'class' else None
        # self.css_element = reference if type == 'css' else None
        # self.xpath_element = reference if type == 'xpath' else None

    # @classmethod
    # def set_id(cls, set_driver, set_name, set_id):
    #    return cls(set_driver, set_name, 'id', set_id)

    ####################################################################################################################
    #                                                  FIND BY                                                         #
    ####################################################################################################################

    def find_by_id(self):
        global element
        try:
            log.degub('Buscando ' + self.name)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.id_reference))
            )
        except Exception as e:
            log.error('Erro ao identificar ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Identificado(a)')
            return True

    def find_by_class(self):
        global element
        try:
            log.degub('Buscando ' + self.name)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.class_reference))
            )
        except Exception as e:
            log.error('Erro ao identificar ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Identificado(a)')
            return True

    def find_by_xpath(self):
        global element
        try:
            log.degub('Buscando ' + self.name)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_reference))
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

    def clickByID(self):
        Element.find_by_xpath()
        try:
            element.click()
        except Exception as e:
            log.error('Erro ao clicar em ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Clicado(a)')
            return True

    def clickByClass(self):
        Element.find_by_xpath()
        try:
            element.click()
        except Exception as e:
            log.error('Erro ao clicar em ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Clicado(a)')
            return True

    def click_by_xpath(self):
        Element.find_by_xpath()

        try:
            element.click()
        except Exception as e:
            log.error('Erro ao clicar em ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Clicado(a)')
            return True

    ####################################################################################################################
    #                                                  SET BY                                                          #
    ####################################################################################################################

    def set_by_xpath(self, set_info):
        Element.find_by_xpath()
        try:
            element.send_keys(set_info)
            if self.name == 'Password':
                element.send_keys(Keys.RETURN)
        except Exception as e:
            log.error('Erro ao escerver ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Clicado(a)')
            return True


    def setByClass(self, set_info):
        Element.find_by_xpath()
        try:
            element.send_keys(set_info)
            if self.name == 'Password':
                element.send_keys(Keys.RETURN)
        except Exception as e:
            log.error('Erro ao escerver ' + self.name)
            print(e)
            return False
        else:
            log.info(self.name + ' Clicado(a)')
            return True


    def setByID(self, set_info):
        Element.find_by_xpath()
        try:
            element.send_keys(set_info)
            if self.name == 'Password':
                element.send_keys(Keys.RETURN)
        except Exception as e:
            log.error('Erro ao escerver ' + self.name)
            print(e)
        else:
            log.info(self.name + ' Clicado(a)')

########################################################################################################################
#                                                  GET BY                                                              #
########################################################################################################################
# Em andamento
