#Essa linha chama a biblioteca que se conecta com o servidor através de url's
from urllib.request import urlopen

#Essa linha passa o arquivo 'page1.html' para a variável 'html'
html = urlopen('http://pythonscraping.com/pages/page1.html')

#Essa linha printa na tela o conteúdo do arquivo
print(html.read())