#Essa linha chama a biblioteca que se conecta com o servidor através de url's
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Essa linha passa o arquivo 'page1.html' para a variável 'html'
html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser') #-> O segundo parâmetro utilizado nessa linha é
#passado para podermos dizer qual o método escolhido

#Essa linha printa na tela o conteúdo do arquivo
print(bs.h1)