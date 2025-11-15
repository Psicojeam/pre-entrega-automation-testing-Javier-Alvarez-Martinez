from page.login_page import LoginPage

def test_login( driver ):
    # Crear primero objeto para luego instanciarlo
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login()