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
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    """
    Function that processes api results and transforms them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns:
        headlines_results: A list of headlines objects
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

def get_new(id):
    get_new_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_new_details_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads(new_details_data)

        new_object = None

        if new_details_response:
            id = new_details_response.get('id')
            title = new_details_response.get('original_title')
            overview = new_details_response.get('overview')
            poster = new_details_response.get('poster_path')
            vote_average = new_details_response.get('vote_average')
            vote_count = new_details_response.get('vote_count')

            new_object = News(id,title,overview,poster,vote_average,vote_count)

    return new_object