import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find("h1")
    lines = bs.find_all("p", {"class":"css-1cy1v93"})
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)

def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find("h1").text
    body = bs.find("div", {"class":"post-body"}).text
    return Content(url, title, body)

url = 'https://www.brookings.edu/research/power-play-how-the-us-benefits-if-china-greens-the-global-south/'

content = scrapeBrookings(url)

print('Title: {}'.format(content.title))
print('URL: {}'.format(content.url))
print(content.body)

url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'

content = scrapeNYTimes(url)

print('Title: {}'.format(content.title))
print('URL: {}'.format(content.url))
print(content.body)