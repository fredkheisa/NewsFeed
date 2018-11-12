from app import app
import urllib.request,json
from .models import source

Source = source.Source


# Getting api key
api_key = app.config['SOURCE_API_KEY']

# Getting the movie base url
base_url = app.config["SOURCE_API_BASE_URL"]


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['articles']:
            source_results_list = get_sources_response['articles']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    """
    Function that processes api results and transforms them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns:
        headlines_results: A list of headlines objects
    """
    source_results = []
    for source_item in source_list:
        source = source_item.get('source')
        author = source_item.get('author')
        title = source_item.get('title')
        description = source_item.get('description')
        url = source_item.get('url')
        image_url = source_item.get('urlToImage')
        publish_time = source_item.get('publishedAt')
        print(title)
        source_object = Source(source, author, title, description, url, image_url, publish_time)
        source_results.append(source_object)

    return source_results