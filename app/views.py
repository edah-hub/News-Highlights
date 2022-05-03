from flask import render_template
from app import app
from .request import get_news,get_sources,getEntertainment
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - News Highlight'
    country_news = get_news('us')
    news_source = get_sources()
    entertainment_news = getEntertainment('entertainment')
   
    return render_template('index.html', title = title, country = country_news, sources = news_source, entertainment = entertainment_news)
    
   