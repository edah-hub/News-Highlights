import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_HIGHLIGHTS_BASE_URL = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
    NEWS_SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_ENTERTAINMENT_BASE_URL = 'https://newsapi.org/v2/top-headlines?category={}&apiKey={}'
    TOP_HEADLINES_BASE_URL = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
    EVERYTHING_BASE_URL = "https://newsapi.org/v2/everything?domains=wsj.com&apikey={}"
    BUSINESS_TOP_HEADLINES_BASE_URL = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={}"


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