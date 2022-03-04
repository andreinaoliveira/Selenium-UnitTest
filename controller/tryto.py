from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from controller import log

########################################################################################################################
#                                                  FIND BY                                                             #
########################################################################################################################

def findByXPath(driver, strElement, idElement):
    global element
    try:
        log.debug('Buscando ' + strElement)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, idElement))
        )
    except Exception as e:
        log.error('Erro ao identificar ' + strElement)
        print(e)
        return False
    else:
        log.info(strElement + ' Identificado(a)')
        return True

def findByClass(driver, strElement, idElement):
    global element
    try:
        log.degub('Buscando ' + strElement)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, idElement))
        )
    except Exception as e:
        log.error('Erro ao identificar ' + strElement)
        print(e)
        return False
    else:
        log.info(strElement + ' Identificado(a)')
        return True


def findByID(driver, strElement, idElement):
    global element
    try:
        log.degub('Buscando ' + strElement)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, idElement))
        )
    except Exception as e:
        log.error('Erro ao identificar ' + strElement)
        print(e)
        return False
    else:
        log.info(strElement + ' Identificado(a)')
        return True

########################################################################################################################
#                                                Click BY                                                              #
########################################################################################################################
def clickByXPath(driver, strElement, idElement):
    findByXPath(driver, strElement, idElement)
    try:
        element.click()
    except Exception as e:
        log.error('Erro ao clicar em ' + strElement)
        print(e)
        return False
    else:
        log.info(strElement + ' Clicado(a)')
        return True

def clickByClass(driver, strElement, idElement):
    findByClass(driver, strElement, idElement)
    try:
        element.click()
    except Exception as e:
        log.error('Erro ao clicar em ' + strElement)
        print(e)
        return False
    else:
        log.info(strElement + ' Clicado(a)')
        return True

def clickByID(driver, strElement, idElement):
    findByID(driver, strElement, idElement)
    try:
        element.click()
    except Exception as e:
        log.error('Erro ao clicar em ' + strElement)
        print(e)
        return False
    else:
        log.info(strElement + ' Clicado(a)')
        return True

########################################################################################################################
#                                                  SET BY                                                              #
########################################################################################################################
def setByXPath(driver, strElement, idElement, setInfo):
    findByXPath(driver, strElement, idElement)
    try:
        element.send_keys(setInfo)
        if strElement == 'Password':
            element.send_keys(Keys.RETURN)
    except Exception as e:
        log.error('Erro ao escerver ' + strElement)
        print(e)
        return False
    else:
        log.info(strElement + ' Clicado(a)')
        return True

def setByClass(driver, strElement, idElement, setInfo):
    findByClass(driver, strElement, idElement)
    try:
        element.send_keys(setInfo)
        if strElement == 'Password':
            element.send_keys(Keys.RETURN)
    except Exception as e:
        log.error('Erro ao escerver ' + strElement)
        print(e)
        return False
    else:
        log.info(strElement + ' Clicado(a)')
        return True

def setByID(driver, strElement, idElement, setInfo):

    findByID(driver, strElement, idElement)
    try:
        element.send_keys(setInfo)
        if strElement == 'Password':
            element.send_keys(Keys.RETURN)
    except Exception as e:
        log.error('Erro ao escerver ' + strElement)
        print(e)
    else:
        log.info(strElement + ' Clicado(a)')


########################################################################################################################
#                                                  GET BY                                                              #
########################################################################################################################
# Em andamento