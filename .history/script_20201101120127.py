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

    def get_article_urls_from_source(self, find_tag1, find_tag2, find_tag3, link1, link2, link3):
        # do something with beautiful soup to return list of urls for article
        response = requests.get(self.source_url)
        doc = BeautifulSoup(response.text, 'html.parser')
        story = doc.find_all(find_tag1, {find_tag2: find_tag3})
        for story in story[:15]:
            article = story.find(link1, {link2: link3})
            article = self.source_url + article['href']
            self.articles.append(article)
            article = Article(article)


class Article:
    def __init__(self, url):
        self.url = url
        self.parse_article()

    def parse_article(self):
        # use beautiful soup to parse actual article
        self.headline = "blah"
        self.byline = "blah"
        self.summary = "blah"

bruh = Source("https://www.reuters.com")
bruh.get_article_urls_from_source('div', 'class', 'story-content', 'a', None, None)
print(bruh.articles)