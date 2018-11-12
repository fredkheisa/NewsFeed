from flask import render_template, request
from app import app
from .request import get_sources, get_articles	
from .models import source

# Views
@app.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	sources = get_sources('Business')
	sports_sources = get_sources('sports')
		# for x in sports_sources:
		# 	print(x.name)
	technology_sources = get_sources('technology')
	entertainment_sources = get_sources('entertainment')
	title = "News Highlighter"

	return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@app.route('/source/<int:source_id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)



