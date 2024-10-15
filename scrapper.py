"""Importas as bibliotecas necessárias"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

driver = webdriver.Chrome()

"""Pega a URL da página"""
driver.get('https://www.sympla.com.br/eventos/brasilia-df?s=tecnologia')

"""Faz um loop que pega os dados da página a cada 10 segundos"""
while True:
    titulos     = []
    datas       = []
    enderecos   = []

    """Coleta os títulos dos eventos dentro da página e insere dentro de uma lista"""
    for titulo in driver.find_elements(By.CLASS_NAME, 'EventCardstyle__EventTitle-sc-1rkzctc-7'):
        titulos.append(titulo.text)

    """Coleta a data dos eventos dentro da página e insere dentro de uma lista"""
    for data in driver.find_elements(By.CLASS_NAME, 'sc-1sp59be-0'):
        datas.append(data.text)

    """Coleta os endereços dos eventos dentro da página e insere dentro de uma lista"""
    for endereco in driver.find_elements(By.CLASS_NAME, 'EventCardstyle__EventLocation-sc-1rkzctc-8'):
        enderecos.append(endereco.text.replace("- ,", ""))

    """Pega os dados das listas e tranforma em um arquivo CSV."""
    arquivo = pd.DataFrame({'Titulos': titulos, 'datas': datas, 'enderecos': enderecos})
    arquivo.to_csv('EventosTec.csv', index=False)
    print(arquivo)
    sleep(10)
