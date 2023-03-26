from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set ()
def getLinks(pageURL):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageURL))
    bs = BeautifulSoup(html, 'html.parser')

    try:
        print(bs.h1.get_text())
        print(bs.find(id = 'mw-contente-text').find_all('p')[0])
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except:
        print("This page is missing, continuing")
    
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #Encontramos outra página
                newPage = link.attrs['href']
                print('*'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('/wiki/Kevin_Bacon')