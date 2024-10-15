from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.sympla.com.br/eventos/brasilia-df?s=tecnologia')

while True:
    titulos     = []
    datas       = []
    enderecos   = []

    for titulo in driver.find_elements(By.CLASS_NAME, 'EventCardstyle__EventTitle-sc-1rkzctc-7'):
        titulos.append(titulo.text)


    for data in driver.find_elements(By.CLASS_NAME, 'sc-1sp59be-0'):
        datas.append(data.text)


    for endereco in driver.find_elements(By.CLASS_NAME, 'EventCardstyle__EventLocation-sc-1rkzctc-8'):
        enderecos.append(endereco.text.replace("- ,", ""))

    print(len(titulos))
    print(len(datas))
    print(len(enderecos))

    arquivo = pd.DataFrame({'Titulos': titulos, 'datas': datas, 'enderecos': enderecos})
    arquivo.to_csv('EventosTec.csv', index=False)
    print(arquivo)
    sleep(10)