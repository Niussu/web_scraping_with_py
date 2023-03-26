from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
#random.seed(datetime.datetime.now())

#Obtem uma lista de todos os links internos de uma página

def getInternalLinks(bs, includeURL):
    includeURL = '{}://{}'.format(urlparse(includeURL).scheme, urlparse(includeURL).netloc)
    internalLinks = []
    #Encontra todos os links que começam com /
    for link in bs.find_all('a', href = re.compile('^(/|.*'+includeURL+')')):
        if link.attrs['href'] is not None:
            if link['href'] not in internalLinks:
                if(link['href'].startswith('/')):
                    internalLinks.append(includeURL+link['href'])
                else:
                    internalLinks.append(link['href'])
    return internalLinks

#Obtem uma lista de todos os links internos de uma página

def getExternalLinks(bs, excludeURL):
    externalLinks = []
    #Encontra todos os links que começam com http
    for link in bs.find_all('a', href = re.compile('^(http|www)((?!'+excludeURL+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

# O resto do código não foi feito pois precisa achar um jeito de usar o random