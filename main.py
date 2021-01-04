import requests
from bs4 import BeautifulSoup as bs

# Constantes
mes = {'1': 'Janeiro', '2': 'Fevereiro', '3': 'Março', '4': 'Abril', '5': 'Maio', '6': 'janeiro',
'7': 'Julho', '8': 'Agosto', '9': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}

## Passos 1 e 2
URL_base = 'http://www.ans.gov.br'
URL = URL_base + '/prestadores/tiss-troca-de-informacao-de-saude-suplementar'
page = requests.get(URL)
soup = bs(page.content, 'lxml') # parser recomendado pela velocidade

## Passos 3 e 4
header = soup.find('h2', string = lambda text: 'Padrão TISS - Versão')
# print(header)
elem = header.next_sibling.next_sibling
# print('Elem is:', elem)
suffix = elem.find('a', class_ = 'alert-link')['href']
URL = URL_base + suffix
# print(URL)
page = requests.get(URL)
soup = bs(page.content, 'lxml')

# Passo 5
table = soup.find('div', class_ = 'table-responsive').tbody
# print(table.prettify())

# Passos 6 a 8
for tr in table.find_all('tr'):
    if tr.find('td').text == 'Componente Organizacional':
        # print(tr.prettify())
        cols = tr.find_all('td')
        vers = cols[1].text
        print('Versão do documento: {} de {}'.format(mes[vers[-2:]], vers[:4]))
        suffix = cols[2].a['href']
        URL = URL_base + suffix
        break

# Passo 9
pdf = requests.get(URL, allow_redirects = True)
print('Iniciando download...')
open('Componente Organizacional {}.{}.pdf'.format(vers[-2:], vers[:4]), 'wb').write(pdf.content)
print('Encerrado com sucesso')
