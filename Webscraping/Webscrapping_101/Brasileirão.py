import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time


#Pegar o conteúdo
url = 'https://interativos.globoesporte.globo.com/estatisticas/atletas/'
#Parsear
driver = webdriver.Edge()
driver.get(url)
element = driver.find_element_by_xpath('/html/body/main/div[3]/div/section[1]/ul/li[1]')
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content,'html.parser')
li = soup.find(name='section')

df= pd.read_html(str(li))
print(df)
#Estruturar
driver.quit()
#Salvar
