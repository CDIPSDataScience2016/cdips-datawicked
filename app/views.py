from flask import render_template, request, redirect, url_for
from app import app
from .utils import bcolors
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import json

py.sign_in('naddata','6eos5rv0q4')

def json_to_link(fi):
    fo = open(fi)
    graph = json.loads(fo.read())
    link = py.iplot(graph, filename=fi)
    return link.embed_code


def bethans_function(name):
    if name == 'Samsung Chromebook':
        #return '<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~mike-a-yen/0.embed" height="525px" width="100%"></iframe>'
        return json_to_link('app/static/Samsung_chromebook_sentiment.json')
    else:
        #return '<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~mike-a-yen/5.embed" height="525px" width="100%"></iframe>'
        return json_to_link('app/static/Ipad_and_Kindle_sentiment.json')


@app.route('/')
def index():
    return redirect(url_for('product'))


@app.route('/product', methods=['GET', 'POST'])
def product():
    print(bcolors.green, request, bcolors.endc)
    print(bcolors.green,list(request.form.keys()),bcolors.endc)
    print(request.form.get('product', ''))
    print(request.form.get('sentiment', ''))
    link = bethans_function(request.form.get('product', ''))
    print(link)
    print(request.form.get('product', ''))

    post = {'product_name': request.form.get('product', ''),
            'kind': 'Time Series',
            'plotly_html': link}
    return render_template('dashboard.html', post=post)
