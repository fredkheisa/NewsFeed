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
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['articles']:
            new_results_list = get_news_response['articles']
            new_results = process_results(new_results_list)

    return new_results

def process_results(new_list):
    """
    Function that processes api results and transforms them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns:
        headlines_results: A lsist of headlines objects
    """
    new_results = []

    for new in news_list:
        source = new.get('source')
        author = new.get('author')
        title = new.get('title')
        description = new.get('description')
        url = new.get('url')
        image_url = new.get('urlToImage')
        publish_time = new.get('publishedAt')

        new_object = News(source, author, title, description, url, image_url, publish_time)
        new_results.append(new_object)

    return new_results
