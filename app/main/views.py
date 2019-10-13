from flask import render_template,request,redirect,url_for
from .import main
from ..request import get_sources,get_articles

from ..models import Source


@main.route("/")
def index():
    """
    View root function that returns the index page and its data
    """
    popular_news = get_sources("popular")
    title = "Welcome to the best news outlet"
    return render_template("index.html",title = title,popular = popular_news) 


@main.route("/sources/<int:sources_id>")
def sources(sources_id):
    '''
    View news page function that returns the movie details page and its data
    '''
    news_source = get_articles(category)
    title = "Worlds best articles"
    return render_template("news.html",id = sources_id,title = title,news = news_source)

