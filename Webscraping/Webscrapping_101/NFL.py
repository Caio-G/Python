import time
from bs4 import BeautifulSoup
import json
import pandas as pd
from selenium import webdriver

# pegar o conteúdo
rankingtop10 ={}

categorias={
    'Passes':{'cat':'passing','stt':'passingyards','label':'Pass Yds'},
    'Tackles':{'cat':'tackles','stt':'defensivecombinetackles','label':'Comb'},
    'Corridas':{'cat':'rushing','stt':'rushingyards','label':'Rush Yds'},
    'Recepções':{'cat':'receiving','stt':'receivingyards','label':'Rec'},
    'Interceptações':{'cat':'interceptions','stt':'defensiveinterceptions','label':'INT'},
}

driver = webdriver.Edge()

def buildrank(type):
    cat = categorias[type]['cat']
    stt = categorias[type]['stt']
    label = categorias[type]['label']

    url = f"https://www.nfl.com/stats/player-stats/category/'{cat}'/2020/REG/all/'{stt}'/DESC"
    driver.get(url)

    element = driver.find_element_by_xpath("//*[@id='main-content']/section[3]/div/div/div/div/table")
    html_content = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_content,'html.parser')
    table = soup.find(name='table')

    df_full = pd.read_html(str(table))[0].head(10)
    df = df_full[['Player',label]]

    return
# Parsear
# Estruturar
# Transformar
# Salvar