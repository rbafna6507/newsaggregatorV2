from flask import Flask
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re
import time
import pymongo
import dns
from paneer import parse_sources

app = Flask(__name__)

@app.route('/parse')
def say_hello():
    parse_sources()
    return "done"

executor = ThreadPoolExecutor (max_workers=None)

@app.route("/", methods=['GET', 'POST'])
def parse_sources_runner():
    # from threading import Thread
    # heavy_thread = Thread(
    #     target=parse_sources,
    # )
    # heavy_thread.daemon = True
    # heavy_thread.start()

    # with ThreadPoolExecutor (max_workers=None) as executor:
    #     executor.map(parse_sources)
    executor.submit(parse_sources)

    return "blah"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)