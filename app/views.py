from flask import render_template
from app import app
from .requests import get_sources,get_links

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting popular headlines
    biashara = get_sources('bbc-news')

    print(biashara[0].title)

    title = 'PATAPATA NEWS AND STORIES'
    return render_template('index.html', title = title, business = biashara)

@app.route('/link/<int:id>')
def link(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    link = get_links(id)
    title = f'{link.title}'

    return render_template('movie.html',title = title,link = link)