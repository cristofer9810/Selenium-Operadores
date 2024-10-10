from sys import executable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from excel_reader import ExcelReader

def process_data(data):
    # Aqui puedes realizar cualquier procesamiento adicional de los datos de 11 a 10 minutos
    for row in data:
        print("Procesando datos:", row)
       
def test_satrack():
    excel_file_path = 'C:\\Users\\Public\\oet\\GPS\\Archivo_Pruebas.xlsx'
    sheet_name = 'Satrack'

    excel_reader = ExcelReader(excel_file_path, sheet_name)
    data = excel_reader.read_data()
    for row in data:
        placa = row[0]
        gps = row[1]
        operador = row[2]
        url = row[3]
        usuario = row[4]
        clave = row[5]
        try:
            driver = webdriver.Chrome()
            driver.get("https://login.satrack.com/login?lng=es&ctry=CO")
            driver.maximize_window()
            time.sleep(3)
            satrack = driver.find_element(By.ID, "txt_login_username")
            satrack.send_keys(usuario)
            time.sleep(3)
            satrack = driver.find_element(By.ID, "txt_login_password")
            satrack.send_keys(clave)
            satrack.send_keys(Keys.ENTER)
            time.sleep(10)
            try:
                satrack = driver.find_element(By.ID, "txtCompleteSearch")
                satrack.send_keys(placa)
                satrack.send_keys(Keys.ENTER)
                time.sleep(3)
                satrack = driver.find_element(By.XPATH, "/html/body/div[1]/div[16]/location-container-ui-root/location-container-ui-app-container/div[1]/div/div[1]/div/mf-sidenav-izquierdo/div[1]/satrack-location/div/div/satrack-vehicle-list/div/cdk-virtual-scroll-viewport/div[1]/div/div")
                satrack.click()
                time.sleep(3)
                try:
                    direccion = driver.find_element(By.ID, "iw-vehicle-address").text
                    print(direccion)
                except NoSuchElementException:
                    print('no existe direccion')
                try:
                    estado = driver.find_element(By.ID, "iw-vehicle-state").text
                    print(estado)
                except NoSuchElementException:
                    print('no existe estado')
                try:
                    velocidad = driver.find_element(By.ID, "iw-vehicle-speed").text
                    print(velocidad)
                except NoSuchElementException:
                    print('no existe velocidad')
                try:
                    sentido = driver.find_element(By.ID, "iw-vehicle-heading").text
                    print(sentido)
                except NoSuchElementException:
                    print('no existe sentido')
                try:
                    lat_long = driver.find_element(By.ID, "iw-vehicle-position").text
                    print(lat_long)
                except NoSuchElementException:
                    print('no existe longitud-latitud')
            except NoSuchElementException:
                print('placa no existe')
            #find = driver.find_element(By.XPATH, "//*[@id='box-table-a']/tbody/tr/td[9]/a")
            #find.click()
            #time.sleep(3)
        except NoSuchElementException:
            print('no existe cuenta')    
if __name__ == '__main__':
	test_satrack()