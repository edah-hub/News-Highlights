class Business:
    """
    This class helps to design Business object
    """
    
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
