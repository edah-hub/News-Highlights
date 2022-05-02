class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,title,description,publishedAt,content,url,img_url):
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.img_url = img_url