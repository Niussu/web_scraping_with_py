import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body
    
    def print(self):
        print("New article found for topic: {}".format(self.topic))
        print("Title: {}".format(self.title))
        print("Body \n{}".format(self.body))
        print("URL: {}".format(self.url))

class Website:
    def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyyTag = bodyTag

#---------------------> Tem que fazer a classe crawler da pág. 79 <----------------------
#Revisa o código todo antes!!!