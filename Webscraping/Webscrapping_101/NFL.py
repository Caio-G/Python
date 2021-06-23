import time
from bs4 import BeautifulSoup
import json
import pandas as pd
from selenium import webdriver

# Pegar o conteúdo
rankingtop10 ={}

categorias={
    'Passes':{'cat':'passing','stt':'passingyards','label':'Pass Yds'},
    'Tackles':{'cat':'tackles','stt':'defensivecombinetackles','label':'Comb'},
    'Corridas':{'cat':'rushing','stt':'rushingyards','label':'Rush Yds'},
    'Recepções':{'cat':'receiving','stt':'receivingyards','label':'Rec'},
    'Interceptações':{'cat':'interceptions','stt':'defensiveinterceptions','label':'INT'},
}

def buildrank(type):
    cat = categorias[type]['cat']
    stt = categorias[type]['stt']
    label = categorias[type]['label']

    url = f"https://www.nfl.com/stats/player-stats/category/{cat}/2020/REG/all/{stt}/DESC"
    driver.get(url)

    element = driver.find_element_by_xpath("//*[@id='main-content']/section[3]/div/div/div/div/table")
    html_content = element.get_attribute('outerHTML')
    
    # Parsear    
    soup = BeautifulSoup(html_content,'html.parser')
    table = soup.find(name='table')

    # Estruturar
    df_full = pd.read_html(str(table))[0].head(10)
    df = df_full[['Player',label]]
    # Transformar os dados em um dicionário
    return df.to_dict('records')


driver = webdriver.Edge()
for k in categorias:
        rankingtop10[k]=buildrank(k)

driver.quit()

# Converter e Salvar em JSON

js = json.dumps(rankingtop10)
fp = open('rankingNFL.json','w')
fp.write(js)
fp.close()