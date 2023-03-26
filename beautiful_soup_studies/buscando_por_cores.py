#Essa linha chama a biblioteca que se conecta com o servidor através de url's
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Essa linha passa o arquivo 'page1.html' para a variável 'html'
html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser') #-> O segundo parâmetro utilizado nessa linha é
#passado para podermos dizer qual o método escolhido

namelist = bs.find_all('span', {'class':'green'})#Utiliza o método find_all para buscar as tags
# com algum atributo
for name in namelist:
    print(name.get_text())# -> Apresenta o que tem dentro dessas tags