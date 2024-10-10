from sys import executable
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time

driver = webdriver.Chrome()	
		
def test_protrack_2(cabezal, usuario, clave):
	driver.maximize_window()
	driver.get("http://app2.protrack365.com/")
	time.sleep(3)
	usuarios = driver.find_element(By.NAME, "username")
	for i in range(1, 15):
			usuarios.send_keys(Keys.BACKSPACE)
	usuarios.send_keys(usuario)
	time.sleep(3)
	claves = driver.find_element(By.NAME, "passwd")
	for i in range(1, 15):
			claves.send_keys(Keys.BACKSPACE)
	claves.send_keys(clave)
	claves.send_keys(Keys.ENTER)
	time.sleep(3)
	driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/iframe"))
	time.sleep(3)
	try:
		for i in range(1, 15):
			ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
			time.sleep(1)
		elemento = driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div[2]/div/div[4]/div[3]/div/div/div/input")
		elemento.send_keys(cabezal)
		time.sleep(1)
		ActionChains(driver).key_down(Keys.DOWN).key_up(Keys.DOWN).perform()
		time.sleep(2)
		ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
		time.sleep(2)
		#geo = driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/div[2]/div/div[4]/div[3]/div/div/div/input")
		#geo.send_keys("351BDR")
  
		#wait = WebDriverWait(driver, 10)
		#elemento = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[4]/div[3]/div/div/div/input')))
		#elemento.send_keys("351BDR")
		#elemento.send_keys(Keys.ENTER)
		#mapa = self.driver.window_handles
		#mapa = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[4]/div[3]/div/div/div/input")
		#mapa.send_keys("351BDR")
		#mapa.send_keys(Keys.ENTER)
		#mapa = driver.find_element(By.CLASS_NAME, "el-input__inner")//*[@id="deviceBox"]/div[3]/div/div/div/input
		#mapa.send_keys("351BDR")
		#mapa.send_keys(Keys.ENTER)
		try:
			elementos = driver.find_element(By.XPATH, "//*[@id='monitorMap']/div[2]/div[6]/div/div[1]/div/div/div[1]/div[3]").text
			print(elementos)
			elementos = driver.find_element(By.XPATH, "//*[@id='monitorMap']/div[2]/div[6]/div/div[1]/div/div/div[1]/div[4]").text
			print(elementos)
			elementos = driver.find_element(By.XPATH, "//*[@id='monitorMap']/div[2]/div[6]/div/div[1]/div/div/div[1]/div[5]").text
			print(elementos)
			elementos = driver.find_element(By.XPATH, "//*[@id='monitorMap']/div[2]/div[6]/div/div[1]/div/div/div[1]/div[6]").text
			print(elementos)
			elementos = driver.find_element(By.XPATH, "//*[@id='monitorMap']/div[2]/div[6]/div/div[1]/div/div/div[1]/div[7]").text
			print(elementos)
			elementos = driver.find_element(By.XPATH, "//*[@id='monitorMap']/div[2]/div[6]/div/div[1]/div/div/div[1]/div[8]").text
			print(elementos)
		except NoSuchElementException as e:
			print(f'placa no existe {e}' )
	except NoSuchElementException as e:
		print(f'placa no existe {e}' )
	finally:
		print('')
  
  
def tearDown(self):
		self.driver.close()

