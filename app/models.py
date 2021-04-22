class News:
    '''
    News class to define news Objects
    '''

    def __init__(self,id,name ,description,url,category,language,counrty):
        self.id =id
        self.name = name
        self.description= description
        self.category = category
        self.url = url
        self.language  = language
        self.country = counrty
       

class Articles:

    articles_list = []

    def __init__(self, news_id,author, title,description,urlToImage, url ,publishedAt):
        self.news_id = news_id
        self.urlToImage = urlToImage
        self.url = url
        self.author = author
        self.description = description
        self.title = title
        self.publishedAt = publishedAt
    
      


  
    
        
   