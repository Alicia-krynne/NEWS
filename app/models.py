class News:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,name,author,description,publishedAt,content,urlToImage):
        self.id =id
        self.name= name
        self.author = author
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.urlToImage = "https://s.yimg.com/os/creatr-uploaded"+image

class Articles:

    all_articles = []

    def __init__(self,news_id,name,urlToImage, url):
        self.news_id = news_id
        self.name = name
        self.urlToImage = urlToImage
        self.url = url

  
    
        
    