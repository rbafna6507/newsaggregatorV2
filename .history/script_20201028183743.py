import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re
import time
import pymongo
import dns

class article():
    def __init__(self):
        self.headline = ""
        self.byline = ""
        self.link = ""