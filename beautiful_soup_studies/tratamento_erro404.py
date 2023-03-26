from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:#-> Página não encotrada
    print(e)
except URLError as e:#-> Sem conexão com servidor
    print(e)
else:
    print("ok")
#Dessa maneira o programa acusará um erro, e ao invés de simplesmente quebrar irá 
#fazer oq vc planejou