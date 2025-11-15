from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#import time EN LUGAR DE IMPORTAR TIME, IMPORTO WEBDRIVERWAIT Y EXPECTED_CONDITIONS Y LO USO PARA CAMPOS CRITICOS COMO LOGIN; PRODUCTOS; ETC:

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL='https://www.saucedemo.com/'
USERNAME='standard_user'
PASSWORD='secret_sauce'


def get_driver():
    #options = Options
    #options.add_argument('--start-maximized')

    # instalacion del driver

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

# AQUI EL implicity_wait ESTA DENTRO DE WEB DRIVER, SOLO TENGO QUE LLAMARLO Y VA DESPUES DE get_driver Y APLICA A TODOS LOS PORCESOS ESE TIEMPO-, EN EL CASO DE HACERLO DISTINTO IMPORTO LOS 2 MODULOS DE SELENIUM QUE ESTAN MAS ARRIBA

    #time.sleep(5)
    driver.implicitly_wait(5)
    return driver





