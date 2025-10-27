from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#import time EN LUGAR DE IMPORTAR TIME IMPORTO WEBDRIVERWAIT Y EXPECTED_CONDITIONS Y LO USO PARA CAMPOS CRITICOS COMO LOGIN; PRODUCTOS; ETC:

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


    #time.sleep(5)
    driver.implicitly_wait(5)
    return driver


def login_saucedemo( driver ):

    driver.get(URL)

    #time.sleep(7)

    #INGRESAR LAS CREDENCIALES 

    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable ((By.NAME, 'user-name'))
    ).send_keys(USERNAME)

    #driver.find_element(By.NAME,'user-name').send_keys(USERNAME)
    driver.find_element(By.NAME,'password').send_keys(PASSWORD)
    driver.find_element(By.ID,'login-button').click()

    driver.save_screenshot('CapturaPantalla.png')

    #time.sleep(7)



