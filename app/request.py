import urllib.request,json
from .models import Source, Article



api_key = None
base_url = None
article_base_url = None

def configure_request(app):
    global api_key,base_url,article_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_API_BASE_URL']
    article_base_url = app.config['NEWS_ARTICLE_BASE_URL']
    






def get_sources(category):

    """
    Function that gets the json response to our url request
    """

    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:

        get_sources_data = url.read()
        get_source_response = json.loads(get_sources_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results


def process_results(source_list):
    '''
    Function that processes the source results and transform to a list of Objects
    Args:
        source_list:A list of dictionaries that contains source details

    Returns:
        source_results: A list of source objects    
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get("id")
        name = source_item.get("name")
        description = source_item.get("description")
        url = source_item.get("url")
        category = source_item.get("category")
        language = source_item.get("language")
        country = source_item.get("country")

        if name:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results

def get_articles(category):
    '''
    Function that gets json response to our url request
    '''
    get_articles_url = article_base_url.format(category)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_article_results(articles_results_list)

    return articles_results

def process_article_results(article_list):
    '''
    Function that processes the article result and transforms them to a list of Objects
    '''
    articles_results = []
    for articles_item in article_list:
        id = articles_item.get("id")
        name = articles_item.get("name")
        author = articles_item.get("author")
        title = articles_item.get("title")
        description = articles_item.get("description")
        url = articles_item.get("url")
        urlToImage = articles_item.get("urlToImage")
        publishedAt = articles_item.get("publishedAt")
        content = articles_item.get("content")

        if urlToImage:
            article_object = Article(id,name,author,title,description,url,urlToImage,publishedAt,content)

            articles_results.append(article_object)

    return articles_results

