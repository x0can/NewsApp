from flask import render_template
from app import app
from .request import get_sources


@app.route("/")
def index():
    """
    View root function that returns the index page and its data
    """
    popular_news = get_sources("popular")
    title = "Welcome to the best news outlet"
    return render_template("index.html",title = title,popular = popular_news) 


@app.route("/sources/<int:sources_id>")
def sources(sources_id):
    '''
    View news page function that returns the movie details page and its data
    '''
    return render_template("news.html",id = sources_id)

