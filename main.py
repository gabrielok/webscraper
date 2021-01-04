import requests
from bs4 import BeautifulSoup as bs

URL_base = 'http://www.ans.gov.br'
URL = URL_base + '/prestadores/tiss-troca-de-informacao-de-saude-suplementar'
page = requests.get(URL)

soup = bs(page.content, 'lxml')

header = soup.find('h2', string = lambda text: 'Padrão TISS - Versão')
print(header)
elem = header.next_sibling.next_sibling
print('Elem is:', elem)
suffix = elem.find('a', class_ = 'alert-link')['href']
URL = URL_base + suffix
print(URL)
