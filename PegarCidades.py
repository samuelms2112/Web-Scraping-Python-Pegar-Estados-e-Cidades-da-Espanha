from sqlite3 import Row
import pandas as pd
import numpy as np
import urllib.request
from bs4 import BeautifulSoup

tabela = pd.read_excel("#Estados.xlsx", index_col=0)
array_tabela = np.asarray(tabela)



for a in array_tabela:

    wiki = "https://pt.wikipedia.org"+a[1]
    page = urllib.request.urlopen(wiki)
    soup = BeautifulSoup(page, 'html.parser')
    all_table = soup.find_all('table')
    table = soup.find('table', class_='wikitable')
    A=[]
    B=[]
    for row in table.findAll("tr"): #para tudo que estiver em <tr>
        cells = row.findAll('td') #variável para encontrar <td>
        if len(cells)==2: #número de colunas
            A.append(cells[0].find(text=True)) #iterando sobre cada linha
            B.append(a[0]) #iterando sobre cada linha
        df = pd.DataFrame()

        df['Estado']= B
        df['Cidade']= A
    
    excel = pd.ExcelWriter(a[0]+'.xlsx', engine='xlsxwriter')
    df.to_excel(excel, sheet_name='Cidades')
    excel.save()
    print(a[0]+'.xlsx criado');    
    