from app import app
from .config import Config as config
import urllib.request,json
from .models import source

# Source = source.Source

# Getting api key
api_key = app.config["NEWS_API_KEY"]

# #Getting the articles base url
# base_url = app.config["NEWS_API_BASE_URL"]
sources = app.config['SOURCES_URL']

def get_sources(category):
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = category.format(category, api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)

		sources_results = None

		if get_sources_response['category']:
			sources_results_list = get_sources_response['category']
			sources_results = process_sources(sources_results_list)
	
	return sources_results

def process_sources(sources_list):
	'''
	Function that processes the news category results and turns them into a list of objects
	Args:
		sources_list: A list of dictionaries that contain category details
	Returns:
		sources_results: A list of category objects
	'''
	sources_results = []

	for source_item in sources_list:
		id = source_item.get('id') 
		name = source_item.get('name')
		description = source_item.get('description')
		url = source_item.get('url')
		category = source_item.get('category')
		language = source_item.get('language')
		country = source_item.get('country')


		sources_object = category(id,name,description,url,category,country,language)
		sources_results.append(sources_object)

	
	return sources_results

def get_articles(id):
	'''
	Function that processes the articles and returns a list of articles objects
	'''
	get_articles_url = articles_url.format(id,api_key)

	with urllib.request.urlopen(get_articles_url) as url:
		articles_results = json.loads(url.read())


		articles_object = None
		if articles_results['articles']:
			articles_object = process_articles(articles_results['articles'])

	return articles_object
