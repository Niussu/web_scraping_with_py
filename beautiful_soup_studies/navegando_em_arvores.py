#Essa linha chama a biblioteca que se conecta com o servidor através de url's
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Essa linha passa o arquivo 'page1.html' para a variável 'html'
html = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

images = bs.find('img')
teste = images.attrs['src']
print(teste)