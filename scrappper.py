from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Abre a URL da página
driver.get('https://www.sympla.com.br/eventos/brasilia-df?s=tecnologia')

# Listas para armazenar os dados
titulos = []
datas = []
enderecos = []

# Função que coleta os dados da página e os adiciona às listas
def coletar_dados():
    #Coleta os títulos dos eventos dentro da página e insere dentro de uma lista
    for titulo in driver.find_elements(By.CLASS_NAME, 'EventCardstyle__EventTitle-sc-1rkzctc-7'):
        titulos.append(titulo.text)

    #Coleta a data dos eventos dentro da página e insere dentro de uma lista
    for data in driver.find_elements(By.CLASS_NAME, 'sc-1sp59be-0'):
        datas.append(data.text)

    #Coleta os endereços dos eventos dentro da página e insere dentro de uma lista
    for endereco in driver.find_elements(By.CLASS_NAME, 'EventCardstyle__EventLocation-sc-1rkzctc-8'):
        if endereco:
            enderecos.append(endereco.text.replace("- ,", ""))
        else:
            enderecos.append(" ")

# Função recursiva para seguir a paginação
def paginar():

    # Verifica se o botão de "Próxima Página" está presente
    botao = ""
    botao = driver.find_elements(By.CSS_SELECTOR, '.DesktopPaginatorstyle__PaginationItem-sc-1g1li4n-1.DesktopPaginatorstyle__PrevNext-sc-1g1li4n-2.hNyJjx')

    # Se o botão for encontrado, coleta os dados da página e clica no botão para ir para a próxima página
    if botao:
        coletar_dados()  # Coleta os dados da página atual
        botao[0].click()  # Clica no botão de "Próxima Página"
        sleep(2)  # Espera 2 segundos para o próximo carregamento
        paginar()  # Chama a função recursivamente para a próxima página
    else:
        # Gera um arquivo CSV com os dados coletados
        arquivo = pd.DataFrame({
            'Titulos': titulos,
            'Datas': datas,
            'Enderecos': enderecos
        })
        titulos.clear
        datas.clear
        enderecos.clear
        arquivo.to_csv('EventosTec.csv', sep=';', index=False)
        print("Dados salvos no arquivo CSV: EventosTec.csv")
        # Se o botão não for encontrado, espera 1800 segundos e começa novamente
        print("Dados coletados, aguardando 30 minutos para extrair novamente...")
        sleep(10)
        paginar()  

# Inicia o processo de paginação e coleta de dados
paginar()

