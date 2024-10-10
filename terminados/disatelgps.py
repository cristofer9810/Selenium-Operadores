from sys import executable
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


       
def test_disatelgps(cabezal, usuario, clave):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gt.disatelgps.com/index.php")
    time.sleep(3)
    cliente = driver.find_element(By.NAME, "userid")
    cliente.send_keys(usuario)
    time.sleep(3)
    claves = driver.find_element(By.NAME, "passw")
    claves.send_keys(clave)
    claves.send_keys(Keys.ENTER)
    time.sleep(10)
    driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div/div[4]/div[1]/iframe"))
    geo = driver.find_element(By.NAME, "textsearch")
    geo.send_keys(cabezal)
    time.sleep(3)
    geo.send_keys(Keys.ENTER)
    time.sleep(3)
    tabla = driver.find_element(By.ID, "box-table-a")
    filas = driver.find_element(By.CSS_SELECTOR, "tr")
    try:
        elementos = driver.find_element(By.XPATH, "//*[@id='box-table-a']/tbody/tr/td[11]").text
        print(elementos)
        #elementos = driver.find_element(By.XPATH, "///*[@id='box-table-a']/tbody/tr/td[14]").text
        #print(elementos)
        elementos = driver.find_element(By.XPATH, "//*[@id='box-table-a']/tbody/tr/td[15]").text
        print(elementos)
        elementos = driver.find_element(By.XPATH, "//*[@id='box-table-a']/tbody/tr/td[19]").text
        print(elementos)
        elementos = driver.find_element(By.XPATH, "//*[@id='box-table-a']/tbody/tr/td[20]").text
        print(elementos)
        elementos = driver.find_element(By.XPATH, "//*[@id='box-table-a']/tbody/tr/td[21]").text
        print(elementos)
            
    except NoSuchElementException:
        print('placa no existe')
    #find = driver.find_element(By.XPATH, "//*[@id='box-table-a']/tbody/tr/td[9]/a")
    #find.click()
    #time.sleep(3)
        
		
        

if __name__ == '__main__':
	unittest.main()