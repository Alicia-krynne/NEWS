import urllib.request,json
from .models import News,Articles
#import urllib.parse

#query = '/'
#urllib.parse.quote('/',safe='')

# Getting api key
api_key = None

# Getting the news base url
base_url = None
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url =app.config ['ARTICLES_BASE_URL']


def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_data)

        news_results = None

        if get_news_source_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

    #import pdb; pdb.set_trace() #python  debugger

    return news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []  
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description= news_item.get('description')
        category = news_item.get('category')
        url = news_item.get('url')
        language  = news_item.get('language')
        country = news_item.get('country')
    
        if urlToImage:

            news_object = News(
                author,
                title,
                description,
                urlToImage,
                publishedAt,
                publishedTime,
                name,
                
            )
            news_results.append(news_object)
    return news_results



def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        #if get_articles:
            #news_id = news_id.get('news_id')
            #urlToImage = urlToImage.get('urlToImage')
            #url = url.get('url')
            #author = author.get('author')
            #description = description.get('description')
            #title = title.get('title')
        if get_articles_response["articles"]:
           articles_results_list = get_articles_response["articles"]

           articles_results = process_results(articles_results_list)


    return articles_results
def process_results(articles_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    articles_results= []
    for articles_item in articles_list:
        id = articles_item.get('id')
        urlToImage = articles_item.get('urlToImage')
        url = articles_item.get('url')
        author = articles_item.get('author')
        description = articles_item.get('description')
        title = articles_item.get('title')
        publishedAt= articles_item.get('publishedAt')

        if urlToImage:
            articles_object = Articles(id,author,title,description,urlToImage, url,publishedAt)
            articles_results.append(articles_object)
            
            
    return articles_results
