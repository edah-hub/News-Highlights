import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SOURCES_BASE_API_URL = "https://newsapi.org/v2/sources?apiKey={}"
    EVERYTHING_BASE_API_URL = "https://newsapi.org/v2/everything?domains=wsj.com&apikey={}"
    TOP_HEADLINES_BASE_API_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    BUSINESS_TOP_HEADLINES = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={}"


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True # debug mode
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}