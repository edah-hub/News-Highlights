class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,author, title, description, url, urlToImage, publishedAt):
        """
        This method allows us to instantiate an instance.
        """
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt