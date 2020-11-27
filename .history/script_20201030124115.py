import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re
import time
import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')
class Queue():
    def __init__(self, list):
        self.list = list
    def enqueue(self, new_element):
        self.list.append(new_element)
    def dequeue(self):
        return self.list.pop(0)
    def peek(self):
        return self.list[0]
class article():
    def __init__(self):
        self.headline = ""
        self.byline = ""
        self.link = ""
    def set_props(self, website, scrape1, scrape2, scrape3, head1, head2, head3, by1, by2, by3, link1, link2, link3, add_web):
        scrape_at = index
        response = requests.get(website)
        doc = BeautifulSoup(response.text, 'html.parser')
        story = doc.find_all(scrape1,{scrape2:scrape3})
        for story in story[:scrape_at]:
            self.headline = story.find(head1, {head2:head3}).text
            if self.headline is None:
                self.headline = "No Headline"
            self.byline = story.find(by1, {by2:by3})
            if self.byline is None:
                self.byline = "No Byline"
            else:
                self.byline = self.byline.text
            self.link = story.find(link1)
            self.link = add_web + self.link['href']
holder = [article() for x in range(1, 15)]
def nytimes():
    for obj in holder:
        global index
        index = holder.index(obj)
        obj.set_props()