from app import app
import urllib.request,json
from .models import news
News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    """ 
    function that gets the headlines on request 
    """

    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    """
    Function that processes api results and transforms them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns:
        headlines_results: A lsist of headlines objects
    """
    news_results = []
    for news in news_list:
        source = news.get('source')
        author = news.get('author')
        title = news.get('title')
        description = new.get('description')
        url = news.get('url')
        image_url = news.get('urlToImage')
        publish_time = news.get('publishedAt')

        news_object = News(source, author, title, description, url, image_url, publish_time)
        news_results.append(news_object)

    return news_results
