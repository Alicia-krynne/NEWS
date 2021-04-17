from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news_source,get_news,search_news
from ..models import Articles


# Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    # Getting  news sources 
  news_sources = get_news_source('sources')
    

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('.search',news_sources=search_news))
    else:
        return render_template('index.html', id = id ,author= author ,title= title,description = description,publishedAt= publishedAt,content= content,urlToImage= urlToImage )

@main.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the  news   sources 
    '''
    news = get_news_source(id)
    title = f'{news.title}'
    
    return render_template('news.html',title = title,news = movie) 


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




