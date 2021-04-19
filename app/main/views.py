from flask import render_template,redirect,url_for
from . import main
from ..requests import get_news,search_news,get_articles
from ..models import Articles 
from ..models import News


# Views

@main.route('/')
def news():

    '''
    View root page function that returns the index page and its data
    '''
    id = get_news ('id')
    business = get_news('business')
    sports = get_news('sports')
    science = get_news('science')
    entertainment =get_news('entertainment')

    return render_template('index.html', id = id ,business = business,sports =sports,science = science,entertainment= entertainment)

@main.route('/articles/<news:id>')
def articles(news_id):

    '''
    View news page function that returns the  news    articles
    '''
    articles = get_articles(id)
    title = f'{news.id}'
    
    return render_template('news.html',id = id,news =news) 


@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_list = news_name.split(" ")
    news_name_format = "+".join(news_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)




