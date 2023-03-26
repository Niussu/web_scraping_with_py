#Essa linha chama a biblioteca que se conecta com o servidor através de url's
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#Essa linha passa o arquivo 'page1.html' para a variável 'html'
html = urlopen('https://pt.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html.read(), 'html.parser') #-> O segundo parâmetro utilizado nessa linha é
#passado para podermos dizer qual o método escolhido

for link in bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('(/wiki/)((?!:).)*$')):
  if 'href' in link.attrs:
    print(link.attrs['href'])