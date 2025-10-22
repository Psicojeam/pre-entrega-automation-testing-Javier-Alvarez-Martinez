from selenium import webdriver 
import time 

driver = webdriver.Chifome() # O Firefox(), Edge()
driver.get("https://www.google.com") 
print("Titulo:", driver.title)
time.sleep(5) 
driver.quit()