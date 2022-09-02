import time
# import outlook
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://localhost:8184/")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

elemento2=driver.find_element(By.NAME,"pass")
elemento2.clear()
elemento2.send_keys("password")

driver. find_element(By.CLASS_NAME,"button").click()
driver.get("http://localhost:8184/")


elemento3=driver.find_element(By.NAME,"Subject")
elemento3.clear()
elemento3.send_keys("Ingresar algo en campo ticket")

driver. find_element(By.PARTIAL_LINK_TEXT,"submit").click()

time.sleep(10)

driver.close()


#User ROOT y password password tracker.
#https://selenium-python.readthedocs.io/getting-started.html
#https://unipython.com/localizando-elementos-selenium/
#prueben la misma y vean (con F12 en el navegador) los datos que les permite identificar  los campos.
#Como prueba seleccionen otra web e intenten realizar el mismo procedimiento.
#login_form = driver.find_element_by_id('loginForm') web &lt;form id="loginForm"&gt;
#find_elements_by_name  username = driver.find_element_by_name('username') web &lt;input name="username" type="text" /&gt;
#find_elements_by_xpath 
#find_elements_by_link_text  continue_link = driver.find_element_by_link_text('Continuar') web &lt;a href="continue.html"&gt;Continuar&lt;/a&gt;
#find_elements_by_partial_link_text continue_link = driver.find_element_by_partial_link_text('Conti')
#find_elements_by_tag_name heading1 = driver.find_element_by_tag_name('h1') web &lt;h1&gt;Bienvenido&lt;/h1&gt; heading1 = driver.find_element_by_tag_name('h1')
#find_elements_by_class_name content = driver. find_element_by_class_name (' content') &lt;html&gt;
#&lt;body&gt;
#&lt;p class="content"&gt;El contenido va aqui.&lt;/p&gt;
#&lt;/body&gt;
#&lt;html&gt;
#find_elements_by_css_selector 	content = driver. find_element_by_css_selector (' p. content')