from sys import executable
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
import time

    
driver = webdriver.Chrome()


def test_mygeotab(cabezal, usuario, clave):
    ubicacion = "no existe"
    cordenadas = "no existe"
    estado = "no existe"
    velocidad = "no existe"
    longitud = "no existe"
    latitud = "no existe"
    bandera = "tue"
    driver.maximize_window()
    driver.get("https://my.geotab.com/#map,liveVehicleIds:!(b989)")
    time.sleep(3)
    cliente = driver.find_element(By.NAME, "login")
    cliente.send_keys(usuario)
    cliente.send_keys(Keys.ENTER)
    time.sleep(3)
    claves = driver.find_element(By.XPATH, "//*[@id='userPasswordId']")
    claves.send_keys(clave)
    claves.send_keys(Keys.ENTER)
    time.sleep(10)
    #wait = WebDriverWait(driver, 10)
    #geo = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='id9309173088884064']/span/span")))5027388489288533
    #geo.click()
    vehic = driver.find_element(By.XPATH, "/html/body/nav/div[3]/div[1]/ul/li[5]/a")
    vehic.click()
    time.sleep(3) 
    river = driver.find_element(By.XPATH, "//*[@id='devices_SearchId']")
    river.send_keys(cabezal)
    time.sleep(3)
    #//*[@id="devices_emptyList"]/div
    try:
        find = driver.find_element(By.XPATH, "//*[@id='devices_emptyList']/div")
        return ubicacion, cordenadas, estado, velocidad, longitud, latitud
    except NoSuchElementException:
        find = driver.find_element(By.XPATH, "//*[@id='devices_BuilderId']/div/div[1]/table/tbody/tr/td/div/div/div/div[1]/a")
        find.click()
        time.sleep(3)
    try:
        
        findi = driver.find_element(By.XPATH, "//*[@id='liveMap_detailsPanel']/div/div[1]/ul/li/button")
        findi.click()
        time.sleep(3)
        bandera = "hola"
        ubicacion = driver.find_element(By.XPATH, "/html/body/main/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/dl/div[1]/dd").text
        print(ubicacion)
        cordenadas = driver.find_element(By.XPATH, "/html/body/main/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/dl/div[2]/dd").text
        print(cordenadas)
        estado = driver.find_element(By.XPATH, "/html/body/main/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/dl/div[3]/dd").text
        print(estado)
        velocidad = driver.find_element(By.XPATH, "/html/body/main/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/dl/div[4]/dd").text
        print(velocidad)
        parametros = driver.find_element(By.XPATH, "/html/body/main/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/dl/div[1]/dd/text()[2]").text
        print(parametros)
        # Dividir la frase en palabras utilizando la coma como delimitador
        partes = cordenadas.split(',')
        # La primera parte antes de la coma (sin espacios al principio y al final)
        longitud = partes[1].strip()
        # La segunda parte despues de la coma (sin espacios al principio y al final)
        latitud = partes[2].strip()
        #print("longitud:", longitud)
        #print("latitud:", latitud)
        return ubicacion, cordenadas, estado, velocidad, longitud, latitud
    except NoSuchElementException:
        if "hola" in bandera:
            velocidad = 0
            partes = ubicacion.split(',')
            print(partes)
            if "no existe" in ubicacion:
                print("no hubo separacion")
                return ubicacion, cordenadas, estado, velocidad, longitud, latitud
            else:
                if len(partes) > 1:
                    # La primera parte antes de la coma (sin espacios al principio y al final)
                    longitud = partes[1].strip()
                    # La segunda parte despues de la coma (sin espacios al principio y al final)
                    latitud = partes[2].strip()
                    #print("longitud:", longitud)
                    #print("latitud:", latitud)
                else:
                    print("La frase no contiene una coma.")
            return ubicacion, cordenadas, estado, velocidad, longitud, latitud
        else:
            print('placa no existe')
            return ubicacion, cordenadas, estado, velocidad, longitud, latitud
    #geo.send_keys(Keys.ARROW_DOWN)
    

        
  
        
       