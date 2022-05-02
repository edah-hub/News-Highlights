from app import app
import datetime
import urllib.request,json
from .models import news,sources,entertainment

News = news.News
Sources = sources.Sources
Entertainment = entertainment.Entertainment

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
news_base_url = app.config["NEWS_HIGHLIGHTS_BASE_URL"]

# Getting the sources base url
sources_base_url = app.config["NEWS_SOURCE_BASE_URL"]

# Getting the entertainment news base url
entertainment_base_url = app.config["NEWS_ENTERTAINMENT_BASE_URL"]


def get_news(country):
	'''
	Function that gets the json response to our url request
	'''
	get_news_url = news_base_url.format(country,api_key)

	with urllib.request.urlopen(get_news_url) as url:
		get_news_data = url.read()
		get_news_response = json.loads(get_news_data)

		news_results = None

		if get_news_response['articles']:
			news_result_list = get_news_response['articles']
			news_results = process_newsResults(news_result_list)


	return news_results