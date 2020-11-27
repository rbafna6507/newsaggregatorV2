from flask import Flask
from script import Source, Article

app = Flask(__name__)

def parse_sources():
    sources = ['http://www.nytimes.com'] # maybe change these to urls instead idk
    for source in sources:
        source = Source(source)
        list_articles = source.articles
        for x in list_articles:
            x = Article(x, source)
            print(x.headline + '\n' + x.summary)

parse_sources()

@app.route('/')
def say_hello():
    return "hello its working"


@app.route("/parse-sources", methods=['GET', 'POST'])
def parse_sources_runner():
    # create thread
    # start thread
    return "blah"