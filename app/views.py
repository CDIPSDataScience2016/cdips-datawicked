from flask import render_template, request
from app import app
from .utils import bcolors
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import json

plotly.tools.set_credentials_file(username='mike-a-yen', api_key='7ijqoy41kr')


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


@app.route('/product')
def product():
    #TODO Use bethans function to change parameters
    # and return json of plotly
    #plot_json = bethans_function(product,sentiment)
    fi = open('app/static/Samsung_chromebook_sentiment.json', 'r')
    graph = json.loads(fi.read())
    data = graph['data']
    link = py.iplot(data,filename).embed_code
    return render_template('product_views.html',post=link)

@app.route('/samsung')
def samsung():
    fi = open('app/static/Samsung_chromebook_sentiment.json', 'r')
    graph = json.loads(fi.read())
    print(bcolors.green, 'Pre', graph, bcolors.endc)
    print(bcolors.blue, 'Post', graph, bcolors.endc)
    return render_template('plots.html',
                           ids=['Samsung'],
                           graphJSON=[graph])


@app.route('/product/<int:product_id>')
def product():
    return '404'
