import requests, urllib.request
import os, sys
from tqdm import *
from bs4 import BeautifulSoup as bs

class DownloadProgressBar(tqdm):
    def update_to(self, b = 1, bsize = 1, tsize = None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

# Constantes
mes = {'1': 'Janeiro', '2': 'Fevereiro', '3': 'Março', '4': 'Abril', '5': 'Maio', '6': 'janeiro',
'7': 'Julho', '8': 'Agosto', '9': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
URL_base = 'http://www.ans.gov.br'
t3 = 'Padrão TISS - Versão'
t6 = 'Componente Organizacional'

## Passos 1 e 2
URL = URL_base + '/prestadores/tiss-troca-de-informacao-de-saude-suplementar'
page = requests.get(URL)
soup = bs(page.content, 'lxml') # parser recomendado pela velocidade

## Passos 3 e 4
header = soup.find('h2', string = lambda text: t3)
# print(header)
elem = header.next_sibling.next_sibling
# print('Elem is:', elem)
suffix = elem.find('a', class_ = 'alert-link')['href']
URL = URL_base + suffix
# print(URL)
page = requests.get(URL)
soup = bs(page.content, 'lxml')

## Passo 5
table = soup.find('div', class_ = 'table-responsive').tbody
# print(table.prettify())

## Passos 6 a 8
for tr in table.find_all('tr'):
    if tr.find('td').text == t6:
        # print(tr.prettify())
        cols = tr.find_all('td')
        vers = cols[1].text
        print('Versão do documento: {} de {}'.format(mes[vers[-2:]], vers[:4]))
        suffix = cols[2].a['href']
        URL = URL_base + suffix
        break

## Passo 9
filename = 'Componente Organizacional {}.{}.pdf'.format(vers[-2:], vers[:4])
try:
    os.listdir().index(filename)
    inp = input('Arquivo já existe. Substituir? Y/N\n').lower()
    if inp == 'n':
        print('Download cancelado.')
        print('Encerrando programa.')
        sys.exit()
    elif inp == 'y':
        pass
    else:
        print('Comando desconhecido.')
        print('Encerrando programa.')
        sys.exit()
except ValueError:
    pass

print('Iniciando download...')
page = requests.get(URL, allow_redirects = True)
with DownloadProgressBar(unit = 'B', unit_scale = True, miniters = 1,
    desc = URL.split('/')[-1]) as t:
    urllib.request.urlretrieve(URL, filename, reporthook = t.update_to)
print('Download realizado com sucesso!')
