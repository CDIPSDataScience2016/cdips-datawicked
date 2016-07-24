from flask import render_template
from app import app
from .utils import bcolors
import plotly
import json


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mike'}
    posts = [{'author': 'Yaning',
              'body': 'Hello!'},
             {'author': 'Bethan',
              'body': 'Goodbye!'}]
    return render_template('index.html',
                           title='CDIPS Data Wicked',
                           user=user,
                           posts=posts)


@app.route('/samsung')
def samsung():
    fi = open('app/static/Samsung_chromebook_sentiment.json', 'r')
    graph = json.loads(fi.read())
    print(bcolors.green, 'Pre', graph, bcolors.endc)
    graph = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
    print(bcolors.blue, 'Post', graph, bcolors.endc)
    return render_template('plots.html',
                           ids=['Samsung'],
                           graphJSON=[graph])


@app.route('/product/<int:product_id>')
def product():
    return '404'
