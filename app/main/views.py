from flask import render_template,redirect,url_for
from . import main
from ..requests import get_news,get_articles
from ..models import Articles 
from ..models import News


# Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   
    business = get_articles('business')
    sports = get_articles('sports')
    science = get_articles('science')
    entertainment = get_articles('entertainment')
    
    

    return render_template('index.html' ,business = business,sports =sports,science = science,entertainment= entertainment)

@main.route('/articles')
def articles(id):

    '''
    View news page function that returns the  news    articles
    '''
    articles = get_articles(id)
    title = f'{id}'
    
    return render_template('news.html', title = title,articles =articles) 

# Static blueprint module usage
#@html.route('/<re(".*"):file_name>')





