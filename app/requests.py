import urllib.request,json
from .models import News

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


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(id,api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_data)

        news_results = None

        if get_news_source_response['results']:
            news_results_list = get_news_source_response['results']
            news_results = process_results(news_source_results_list)


    return news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []  #  add  the  categories
    for news_item in news_list:
        id = news_item.get('id')
        sports= news_item.get('sports')
        science = news_item.get('science')
        business = news_item.get('business')
        entertainment = news_item.get('entertainment')

        if poster:
            news_object = news(id,name,author,description,publishedAt,urlToImage,content)
            news_results.append(news_object)

    return news_results


 
def search_news(news_name):
    

    search_news_url = 'https://newsapi.org/v2/sources?apiKey={}'.format(api_key,news)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)


    return search_news_results


def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles:
            news_id = news_id.get('id')
            urlToImage = urlToImage.get('urlToImage')
            url = url.get('url')
            author = author.get('author')
            description = description.get('description')
            title = title.get('title')

        articles_object = Articles(source,news_id,author, title,descripton,urlToImage, url)


    return articles_results
def process_results(articles_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    articles_list= []
    for articles_item in articles_list:
        news_id = news_id.get('id')
        urlToImage = urlToImage.get('urlToImage')
        url = url.get('url')
        source = source.get('source')
        author = author.get('author')
        description = description.get('description')
        title = title.get('title')

        articles_object = Articles(source,news_id,author, title,descripton,urlToImage, url)

        if poster:
            news_object =   News(id,name,author,description,publishedAt,urlToImage,content)
            news_results.append(news_object)

    return articles_results
