from flask import render_template,request,redirect,url_for
from .import main
from ..request import get_sources,get_articles,search_news


from ..models import Source


@main.route("/")
def index():
    """
    View root function that returns the index page and its data
    """
    popular_news = get_sources("popular")
    title = "Welcome to the best news outlet"

    search_news = request.args.get("article_query")

    if search_news:
        return redirect(url_for('main.search',news_feed = search_news))

    else:

        
        return render_template("index.html",title = title,popular = popular_news) 


@main.route("/sources/<sources_id>")
def sources(sources_id):
    '''
    View news page function that returns the movie details page and its data
    '''

    news_source = get_articles(sources_id)
    title = f"{sources_id} | All Articles"
    return render_template("news.html",name = sources_id,title = title,news = news_source)

@main.route("/search/<news_feed>")
def search(news_feed):
    '''
    View function to display the search results
    '''

    news_name_list = news_feed.split(" ")
    news_name_format = "+".join(news_name_list)
    
    searched_news = search_news(news_name_format)
    title = "News results"
    #search_news = request.args.get('article_query')

    return render_template("search.html",article = searched_news)

    


       

  

    

            