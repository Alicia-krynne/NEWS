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

    articles_list = []

    def __init__(self, source,news_id,author, title,descripton,urlToImage, url):
        self.news_id = news_id
        self.urlToImage = urlToImage
        self.url = url
        self.source = source
        self.author = author
        self.description = description
        self.title = title
    
    @classmethod
    def get_articles (cls,id):
        reponse[]

        for articles in cls.articles_list:
            if articles.news_id==id:
                response.append(articles)
        return response
        


  
    
        
    