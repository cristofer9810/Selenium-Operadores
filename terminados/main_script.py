from selenium import webdriver
from excel_reader import ExcelReader
from startrack import test_staging
from disatelgps import test_disatelgps
from mygeotab import test_mygeotab
from protrack365 import test_protrack_2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.alert import Alert
import threading
from reportlab.pdfgen import canvas
from concurrent.futures import ThreadPoolExecutor
import pdfkit
import jinja2 
from datetime import datetime

# 1. pip install reportlab            2. pip install selenium

def process_data(data):
    # Aqui puedes realizar cualquier procesamiento adicional de los datos de 11 a 10 minutos
    for row in data:
        print("Procesando datos:", row)

def main():
    excel_file_path = 'C:\\Users\\Public\\oet\\GPS\\operadores\\prueba.xlsx'
    sheet_name = 'Unidades'

    excel_reader = ExcelReader(excel_file_path, sheet_name)
    data = excel_reader.read_data()

    # Inicializar el navegador web con Selenium
    try:
        # Hacer algo con los datos utilizando Selenium
        for row in data:
            # Supongamos que row[0] es el dato que quieres usar
            cabezal = row[0]
            gps = row[1]
            url = row[2]
            cliente = row[3]
            usuario = row[4]
            clave = row[5]
            integrado = row[6]
            if "STARTRACK" in gps:
                print("*****************esto es un STARTRACK********************")
                print(cabezal)
                print(gps)
                print(url)
                print(cliente)
                print(usuario)
                print(clave)
                print(integrado)
                ubicacion, cordenadas, estado, velocidad, longitud, latitud = test_staging(cabezal, cliente, usuario, clave)
                today_date = datetime.today().strftime("%d %m, %Y")
                #resumen, comparendo, multas, acuerdos, cedula, total, datos_fila, dato_usuario, result_dict = test_simitPerson 
                """ texto = {'ubicacion': ubicacion, 'cordenadas': cordenadas, 'estado': estado, 'velocidad': velocidad,
                        'longitud': longitud, 'latitud': latitud, 'cabezal': cabezal, 'today_date': today_date} 
                template_loader = jinja2.FileSystemLoader('C:\\Users\\Public\\oet\\GPS\\operadores\\terminados\\plantilla')
                template_env = jinja2.Environment(loader=template_loader)
                html_template = 'plantilla.html'
                template = template_env.get_template(html_template)
                output_text = template.render(texto)
                config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
                output_pdf = cabezal+'pdf_generado.pdf'
                pdfkit.from_string(output_text, output_pdf, configuration=config, css='./plantilla/reporte.css') """
                print("*****************termina datos STARTRACK********************")
            elif "PROTRACK" in gps:
                print("*****************esto es un Protrack********************")
                print(cabezal)
                print(gps)
                print(url)
                print(cliente)
                print(usuario)
                print(clave)
                print(integrado)
                #resultado = test_protrack_2(cabezal, usuario, clave)
                print("*****************termina datos STARTRACK********************")
            elif "DISATEL" in gps:
                print("*****************esto es un DISATEL********************")
                print(cabezal)
                print(gps)
                print(url)
                print(cliente)
                print(usuario)
                print(clave)
                print(integrado)
                #resultados = test_disatelgps(cabezal, usuario, clave)
                print("*****************termina datos STARTRACK********************")
            elif "GEOTAB" in gps:
                print("*****************esto es un GEOTAB********************")
                print(cabezal)
                print(gps)
                print(url)
                print(cliente)
                print(usuario)
                print(clave)
                print(integrado)
                #resultadose = test_mygeotab(cabezal, usuario, clave)
                print("*****************termina datos GEOTAB********************")
            # driver.get(row[0])
            pass

        # Llamar a otra funcion para procesar los datos
        #process_data(data)

    finally:
        #ok
        print('')


def otroMain():
    excel_file_path = 'C:\\Users\\Public\\oet\\GPS\\operadores\\prueba.xlsx'
    sheet_name = 'Unidades'

    excel_reader = ExcelReader(excel_file_path, sheet_name)
    data = excel_reader.read_data()

    # Inicializar el navegador web con Selenium
    try:
        # Hacer algo con los datos utilizando Selenium
        for row in data:
            # Supongamos que row[0] es el dato que quieres usar
            cabezal = row[0]
            gps = row[1]
            url = row[2]
            cliente = row[3]
            usuario = row[4]
            clave = row[5]
            integrado = row[6]
            if "STARTRACK" in gps:
                print("*****************esto es un STARTRACK********************")
                print(cabezal)
                print(gps)
                print(url)
                print(cliente)
                print(usuario)
                print(clave)
                print(integrado)
                #resultado = test_staging(cabezal, cliente, usuario, clave)
                print("*****************termina datos STARTRACK********************")
            elif "PROTRACK" in gps:
                print("*****************esto es un Protrack********************")
                print(cabezal)
                print(gps)
                print(url)
                print(cliente)
                print(usuario)
                print(clave)
                print(integrado)
                #resultado = test_protrack_2(cabezal, usuario, clave)
                print("*****************termina datos STARTRACK********************")
            elif "DISATEL" in gps:
                print("*****************esto es un DISATEL********************")
                print(cabezal)
                print(gps)
                print(url)
                print(cliente)
                print(usuario)
                print(clave)
                print(integrado)
                #resultados = test_disatelgps(cabezal, usuario, clave)
                print("*****************termina datos STARTRACK********************")
            elif "GEOTAB" in gps:
                print("*****************esto es un GEOTAB********************")
                print(cabezal)
                print(gps)
                print(url)
                print(cliente)
                print(usuario)
                print(clave)
                print(integrado)
                ubicacion, cordenadas, estado, velocidad, longitud, latitud = test_mygeotab(cabezal, usuario, clave)
                today_date = datetime.today().strftime("%d %m, %Y")
                #resumen, comparendo, multas, acuerdos, cedula, total, datos_fila, dato_usuario, result_dict = test_simitPerson 
                """ texto = {'ubicacion': ubicacion, 'cordenadas': cordenadas, 'estado': estado, 'velocidad': velocidad,
                        'longitud': longitud, 'latitud': latitud, 'cabezal': cabezal, 'today_date': today_date} 
                template_loader = jinja2.FileSystemLoader('C:\\Users\\Public\\oet\\GPS\\operadores\\terminados\\plantilla')
                template_env = jinja2.Environment(loader=template_loader)
                html_template = 'plantilla.html'
                template = template_env.get_template(html_template)
                output_text = template.render(texto)
                config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
                output_pdf = cabezal+'_pdf_generado.pdf'
                pdfkit.from_string(output_text, output_pdf, configuration=config, css='./plantilla/reporte.css') """
                print("*****************termina datos GEOTAB********************")
            # driver.get(row[0])
            pass

        # Llamar a otra funcion para procesar los datos
        #process_data(data)

    finally:
        #ok
        print('')

if __name__ == "__main__":
    #main()
    # Crea dos threads, uno para cada prueba
    with ThreadPoolExecutor(max_workers=4) as executor:
            # Ejecutar las dos automatizaciones al mismo tiempo
            future1 = executor.submit(main)
            future2 = executor.submit(otroMain)
            future3 = executor.submit(main)
            future4 = executor.submit(otroMain)
            future1.result()
            future2.result()
            future3.result()
            future4.result()