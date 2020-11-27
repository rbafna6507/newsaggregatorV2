import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re
import time
import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')
class Source:
    def __init__(self, source_url):
        # change source_url dependent on actual source
        self.source_url = source_url
        self.articles = []
        self.summarize_source()


    def get_article_urls_from_source(self):
        # do something with beautiful soup to return list of urls for article
        return ['blah.com', 'blah.com']

    def summarize_source(self):
        # get a list of the urls for the articles
        article_urls = self.get_article_urls_from_source()

        # create articles
        for article_url in article_urls:
            article = Article(article_url)
            self.articles.append(article)


class Article:
    def __init__(self, url):
        self.url = url
        self.parse_article()

    def parse_article(self):
        # use beautiful soup to parse actual article
        self.headline = "blah"
        self.byline = "blah"
        self.summary = "blah"