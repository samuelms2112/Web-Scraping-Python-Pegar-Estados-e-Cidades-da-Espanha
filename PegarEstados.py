#importe a biblioteca usada para consultar uma URL
import urllib.request

#importe as funções BeautifulSoup para analisar os dados retornados do site
from bs4 import BeautifulSoup

#especifique o URL
wiki = "https://pt.wikipedia.org/wiki/Prov%C3%ADncias_da_Espanha"

#Consulte o site e retorne o html para a variável 'page'
page = urllib.request.urlopen(wiki)

#Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
soup = BeautifulSoup(page, 'html.parser')

#Insira a tag <li> e adicione sua classe
all_table = soup.find_all('table')
table = soup.find('table', class_='wikitable')


#gerando a lista em colunas
A=[]
B=[]

for row in table.findAll("tr"): #para tudo que estiver em <tr>
    cells = row.findAll('td') #variável para encontrar <td>
    if len(cells)==4: #número de colunas
        A.append(cells[0].find(text=True)) #iterando sobre cada linha
        B.append(cells[3].find('a').get('href'))

#importe o pandas para converter a lista em uma planilha
import pandas as pd

df = pd.DataFrame()

df['Estado']=A
df['Link']=B

df

excel = pd.ExcelWriter('#Estados.xlsx', engine='xlsxwriter')
df.to_excel(excel, sheet_name='Estados')
excel.save()

print('#Estados.xlsx Criado')