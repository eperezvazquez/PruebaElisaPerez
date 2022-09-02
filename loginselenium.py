import time
# import outlook
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("https://ev1.utec.edu.uy/moodle/")
elemento1 = driver.find_element(By.ID, "inputName")
elemento1.clear()
elemento1.send_keys("elisa.perez")

elemento2 = driver.find_element(By.ID, "inputPassword")
elemento2.clear()
elemento2.send_keys("E1346903z@")

driver.find_element(By.ID, "submit").click()

time.sleep(20)

driver.close()

#https://selenium-python.readthedocs.io/getting-started.html

#prueben la misma y vean (con F12 en el navegador) los datos que les permite identificar  los campos.
#Como prueba seleccionen otra web e intenten realizar el mismo procedimiento.