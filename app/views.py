from flask import render_template
from app import app
from .request import get_movies

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     # Getting popular headlines
    biashara = get_news('business')
    michezo = get_news('sports')

    print(biashara)
    print(michezo)

    title = 'PATAPATA NEWS AND STORIES'
    return render_template('index.html', title = title, biashara = biashara, michezo = michezo)
