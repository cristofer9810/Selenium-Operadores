from sys import executable
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.alert import Alert

class gps_unittest(unittest.TestCase):
       
    def test_satrack(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.detektor.com.co/login-plataforma")
        time.sleep(3)
        cliente = driver.find_element(By.ID, "username")
        cliente.send_keys("TLM011")
        time.sleep(3)
        clave = driver.find_element(By.ID, "password")
        clave.send_keys("TLM011")
        clave.send_keys(Keys.ENTER)
        time.sleep(10)
        try:
            clave = driver.find_element(By.ID, "idBtnProductSkytrack")
            clave.click()
            time.sleep(3)
            # Esperar a que se abra la nueva pesta?a (puedes usar WebDriverWait)
            WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)
            # Obtener la manija de la nueva pesta?a, el numero uno indica la posicion de la pestana 
            nueva_ventana = driver.window_handles[1]
            # Cambiar al contexto de la nueva pesta?a
            driver.switch_to.window(nueva_ventana)
            time.sleep(3)
            placa = driver.find_element(By.ID, "mostrar-menu")
            placa.click()
            time.sleep(2)
            placa = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/a/table/tbody/tr/td/form/input[1]")
            placa.send_keys("TLM011")
            time.sleep(2) 
            placa = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/a/table/tbody/tr/td/form/input[3]")
            placa.click()
            time.sleep(2)
            placa = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/a/table/tbody/tr/td/form/input[2]")
            placa.click()
            time.sleep(2)
            placa = driver.find_element(By.XPATH, "//*[@id='menu_0_5']/tbody/tr/td[2]")
            placa.click()
            time.sleep(2)
            placa = driver.find_element(By.XPATH, "//*[@id='menu_1_1']/tbody/tr/td[2]")
            placa.click()
            time.sleep(2)
            driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[3]/td/table/tbody/tr/td/div[1]/iframe"))
            placa = driver.find_element(By.XPATH, "//*[@id='filtro']/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td/input[1]")
            placa.click()
            time.sleep(2)
            """ ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
            time.sleep(2)
            ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
            time.sleep(2)
            ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
            time.sleep(2)
            ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
            time.sleep(2)
            ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
            time.sleep(2) """
            #latitud
            driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/form[1]/center/div[1]/iframe"))
            elemento = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[1]/td[3]").text
            print(elemento)
            #longitud
            elemento = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[1]/td[4]").text
            print(elemento)
            #velocidad
            elemento = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[1]/td[5]").text
            print(elemento)
            #ubicacion
            elemento = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[1]/td[7]").text
            print(elemento)
        except NoSuchElementException:
            print('placa no existe')
        #find = driver.find_element(By.XPATH, "//*[@id='box-table-a']/tbody/tr/td[9]/a")
        #find.click()
        #time.sleep(3)
        """ ventana_emergente = driver.window_handles[0]
            driver.switch_to.window(ventana_emergente)
            placa = driver.find_element(By.NAME, "opcion")
            placa.click()
            print("paso esto")
            time.sleep(2)
            ventana_principal = driver.window_handles[1]
            driver.switch_to.window(ventana_principal) """
    def tearDown(self) -> None:
         return super().tearDown()
        
if __name__ == '__main__':
	unittest.main()