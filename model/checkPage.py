from controller import webdriver

def welcome(driver):
    return tryto.findByXPath(driver, 'Bem vindo',
                             '//*[@id="appMountPoint"]/div/div/div/div/div/div[2]/div[1]/div[2]/h1')