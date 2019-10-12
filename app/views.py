from flask import render_template
from app import app
from .request import get_news


@app.route('/')
def index():

    """
    view root function that returns the index page and its data
    """
    popular_news = get_news("popular")
    upcoming_news = get_news("upcoming")
    now_trending = get_news("trending")
    title = "Home - Welcome to The best News website Online"
    return render_template("index.html",title = title, popular = popular_news,upcoming = upcoming_news,trending = now_trending)

@app.route("/news/<int:news_id>")
def news(news_id):
    """
    View news function that returns the news details page and its data
    """    
    return render_template("news.html",id = news_id)