import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time

rankingstats = {}
finalrank = {}

#Pegar o conteúdo
url = 'https://interativos.globoesporte.globo.com/estatisticas/atletas/'
#Parsear
driver = webdriver.Edge()
driver.get(url)
def buildrank(x):
    element = driver.find_element_by_xpath('/html/body/main/div[3]/div/section[1]/ul/li[1]')
    html_content = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_content,'html.parser')
    li = soup.find('li')
    clube = li.find('div',class_="ranking__escudo").text
    Jogador = li.find('div',class_="ranking__nome").text
    pos = li.find('div',class_="ranking__posicao").text
    jogos = li.find_all('span',class_="ranking__value")[1].text
    valor = li.find_all('span',class_="ranking__value")[2].text

    df= f"Time : {clube.strip()}\nJogador : {Jogador}\nPosição : {pos}\nJogos: {jogos}\nGols: {valor}"
    return df

for k in rankingstats:
    finalrank[k] = buildrank(k)

driver.quit()
#Salvar
