from flask import Flask
from script import Source, Article

app = Flask(__name__)

def parse_sources():
    sources = ['http://www.nytimes.com'] # maybe change these to urls instead idk
    for source in sources:
        source = Source(source)
    print(source)

parse_sources

@app.route('/')
def say_hello():
    return "hello its working"


@app.route("/parse-sources", methods=['GET', 'POST'])
def parse_sources_runner():
    # create thread
    # start thread
    return "blah"