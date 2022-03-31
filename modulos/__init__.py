from selenium import webdriver
from selenium.webdriver.common.by import By


def conta_anuncios(palavra_chave):
    """
    :param palavra_chave: Nome do produto e ou palavra chave para encontrar tal
    :return: o valor referente há quantidade de anuncios encontrados no ML (em forma de string)
    """
    navegador = webdriver.Chrome()
    navegador.get('https://www.mercadolivre.com.br/')
    navegador.delete_all_cookies()
    #localizando o campo de busca
    campo_busca = navegador.find_element(by=By.XPATH, value='//*[@id="cb1-edit"]')
    campo_busca.clear()
    #inserindo a variavel com o nome do produto/palavra chave e buscando
    campo_busca.send_keys(palavra_chave)
    campo_busca.send_keys(u'\ue007')
    #localizando a quantidade de anuncios
    valor = navegador.find_element(by=By.CLASS_NAME, value="ui-search-search-result__quantity-results").text
    navegador.close()
    return valor.replace('resultado', '')
