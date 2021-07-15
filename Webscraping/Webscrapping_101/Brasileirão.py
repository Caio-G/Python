import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import json

rankingstats = {
        'Artilheiros':{
            'xpath':'//*[@id="fittPageContainer"]/div[3]/div/div[1]/section/div/section/div/div[1]/section/div/div[2]/div/div[2]/table',
            'dado':'Gols'        },
        'Garçons':{
            'xpath':'//*[@id="fittPageContainer"]/div[3]/div/div[1]/section/div/section/div/div[2]/section/div/div[2]/div/div[2]/table',
            'dado':'Assistencias'
        }
    }
finalrank = {}

#Pegar o conteúdo
url = 'https://www.espn.com.br/futebol/estatisticas/_/liga/BRA.1/vista/gols'
#Parsear
driver = webdriver.Edge()
driver.get(url)
def buildrank(x):
    xpath = rankingstats[x]['xpath']
    dado = rankingstats[x]['dado']
    element = driver.find_element_by_xpath(str(xpath))
    html_content = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_content,'html.parser')
    tabela = soup.find('table')

    pd_full = pd.read_html(str(tabela))[0].head(10)

    pd_full.columns=['POS','Jogador','Clube','Pontos',dado]
    pd_full = pd_full.fillna('-')
    print(pd_full)

    return pd_full.to_dict('records')

for k in rankingstats:
    finalrank[k] = buildrank(k)

driver.quit()
#Salvar

js = json.dumps(finalrank)
fp = open('statsbras.json','w')
fp.write(js)
fp.close()