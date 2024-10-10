from sys import executable
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time



def quitar_letras(cadena, letras_a_quitar):
    nueva_cadena = ""
    for letra in cadena:
        if letra not in letras_a_quitar:
            nueva_cadena += letra
    return nueva_cadena

def test_staging(cabezal, cliente, usuario, clave):
	ubicacion = "no existe"
	cordenadas = "no existe"
	estado = "no existe"
	velocidad = "no existe"
	longitud = "no existe"
	latitud = "no existe"
	bandera = "tue"
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get("https://staging.gps.gt//index.php?loginError=Por+favor+ingrese+su+n%C3%BAmero+de+cliente%2C+usuario+y+clave")
	time.sleep(3)
	cadena_original = cabezal
	letras_a_quitar = "C-"
	cadena_resultante = quitar_letras(cadena_original, letras_a_quitar)
	cabezal = cadena_resultante
	try:
		clientes = driver.find_element(By.NAME, "client")
		clientes.send_keys(cliente)
		time.sleep(1)
		usuarios = driver.find_element(By.NAME, "username")
		usuarios.send_keys(usuario)
		time.sleep(1)
		claves = driver.find_element(By.NAME, "password")
		claves.send_keys(clave)
		claves.send_keys(Keys.ENTER)
		time.sleep(1)
	except NoSuchElementException:
		time.sleep(1)
	try:
		claves = driver.find_element(By.XPATH, "/html/body/div[15]/div[2]/div/div/div[2]/div/button")
		claves.click()							
		""" claves = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]")#/html/body/div[3]/div[2]/div[1]/div[2]/div/a
		claves.click() """
		time.sleep(1)
	except NoSuchElementException:
		claves = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div/a")
		claves.click()
	#mapa = self.driver.window_handles
	placa = driver.find_element(By.XPATH, "//*[@id='fsTable']/tbody/tr[2]/td[2]/input")
	time.sleep(3)
	placa.send_keys(cabezal)
	time.sleep(3)
	try:
		mapa = driver.find_element(By.XPATH, "//html/body/div[1]/div[5]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[1]/img")
		mapa.click()
		time.sleep(3)
		mapa = driver.find_element(By.XPATH, "//*[@id='fsTable']/tbody/tr[4]/td/table/tbody/tr/td[2]/div/div[1]/div/div/table/tbody/tr[2]")
		mapa.click()
		time.sleep(3)
		mapa = driver.find_element(By.XPATH, "//*[@id='leaflet-main-map']/div[4]/div[2]/div/div[1]/div[3]/div[2]")
		mapa.click()
		time.sleep(3)
		mapa = driver.find_element(By.XPATH, "//*[@id='leaflet-main-map']/div[4]/div[2]/div/div[2]/div[2]/div/div[1]")
		mapa.click()
		time.sleep(3)
		#km
		velocidad = driver.find_element(By.XPATH, "//*[@id='leaflet-main-map']/div[4]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div").text
		print(velocidad)
		#ciudad
		ubicacion = driver.find_element(By.XPATH, "//*[@id='leaflet-main-map']/div[4]/div[2]/div/div[2]/div[2]/div/div[1]/div[4]").text
		print(ubicacion)
		#fecha
		fecha = driver.find_element(By.XPATH, "//*[@id='leaflet-main-map']/div[4]/div[2]/div/div[2]/div[2]/div/div[1]/div[3]").text
		print(fecha)
		#cordenadas
		cordenadas = driver.find_element(By.XPATH, "//*[@id='leaflet-main-map']/div[4]/div[2]/div/div[2]/div[2]/div/div[1]/div[5]/div/div/div[1]").text
		print(cordenadas)
		#conductor
		conductor = driver.find_element(By.XPATH, "//*[@id='leaflet-main-map']/div[4]/div[2]/div/div[2]/div[2]/div/div[1]/div[5]/div/div/div[3]/span").text
		print(conductor)
		estado = conductor
		mapa = driver.find_element(By.XPATH, "//html/body/div[2]/div[4]/div[1]/div[1]/div/div[1]")
		mapa.click()
		time.sleep(3)
		mapa = driver.find_element(By.XPATH, "//html/body/div[2]/div[4]/div[1]/div[2]/div/div[2]/div")
		mapa.click()
		time.sleep(3)
		if "no existe" in cordenadas:
			print("no hubo separacion")
			return ubicacion, cordenadas, estado, velocidad, longitud, latitud
		else:
				partes = cordenadas.split(',')
				if len(partes) > 1:
					# La primera parte antes de la coma (sin espacios al principio y al final)
					longitud = partes[0].strip()
					# La segunda parte despues de la coma (sin espacios al principio y al final)
					latitud = partes[1].strip()
					#print("longitud:", longitud)
					#print("latitud:", latitud)
				else:
					print("La frase no contiene una coma.")
		return  ubicacion, cordenadas, estado, velocidad, longitud, latitud
	except NoSuchElementException:
		print("no existe la placa", cabezal)
		return  ubicacion, cordenadas, estado, velocidad, longitud, latitud
	
		

