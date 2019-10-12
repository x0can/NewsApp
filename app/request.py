from app import app
import urllib.request,json
from models import news

News = news.News



api_key = app.config["NEWS_API_KEY"]
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(articles):
    """
    Function that gets the json response to our url request
    """
    get_news_url = base_url.format(articles,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

       

        if get_news_response["articles"]:
            news_results_list = get_news_response["articles"]
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    """
    Function that processes the news result and transforms them to a list of objects

    Returns:
        news_results: A list of news objects
    """
    news_results = []

    for news_item in news_list:
        id = news_item.get("id")
        name = news_item.get("name")
        author = news_item.get("author")
        title = news_item.get("title")
        description = news_item.get("description")
        url = news_item.get("url")
        urlToImage = news_item.get("urlToImage")
        publishedAt = news_item.get("publishedAt")
        content = news_item.get("content")

        if description:
            news_object = News(id,name,author,title,description,url,urlToImage,publishedAt,content)
            news_results.append(news_object)

    return news_results
        