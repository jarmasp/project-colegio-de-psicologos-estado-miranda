from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def validar_fpv(driver = webdriver.Firefox(), url="http://www.fpv.org.ve/site/index_b.php?xZw=xee2i"):

    driver.get(url)

    time.sleep(3)

    select = Select(driver.find_element('name', 'opcion_busqueda'))

    # select by visible text
    select.select_by_visible_text('No. de FPV')

    # select by value 
    select.select_by_value('2')

    fpv = input('Escribe tu FPV: ')

    inputElement = driver.find_element('id', 'nro_fpv')
    inputElement.send_keys(fpv)

    driver.find_element('id', 'btn_buscar').click()

    time.sleep(3)

    rows = driver.find_elements('xpath', "//table/tbody/tr")

    for row in rows:
        cols = row.find_elements('xpath', "./*") # Gets all the column elements with tag name "th" or "td" within the element row.
        temp = []
        for col in cols:
            temp.append(col.text)

    try:
        temp = temp[3]
        temp = temp.replace('.','')
        print(temp)
    except:
        temp = temp[0]
        print(temp)
        print(type(temp))

    if fpv == temp:
        print('verified')
    elif 'No se logro ningún resultado con los criterios usados' == temp:
        print('No se encontro su fpv en la base de datos de la federacion')
    else:
        print('AAAAAAAAAAA')