from flask import render_template, request, redirect, url_for
from app import app
from .utils import bcolors
from Plots.time_series_plots import make_all_review_plot_json, make_sentiment_plot_json
from Plots.phrase_word_cloud import make_word_cloud
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import json


py.sign_in('naddata','6eos5rv0q4')

def plotly_json_to_html(js,filename='product'):
    link = py.iplot(js, filename=filename)
    return link.embed_code


def bethans_function(name):
    if name == 'Samsung Chromebook':
        return json_to_link('app/static/Samsung_chromebook_sentiment.json')
    else:
        return json_to_link('app/static/Ipad_and_Kindle_sentiment.json')

def product_list(lst):
    return '<br>'.join(lst).rstrip('<br>')

@app.route('/')
def index():
    return redirect(url_for('product'))


def product_html_plot(lst):
    product_html = '<iframe></iframe>'
    plot_type = ''
    if lst:
        product_json = json.loads(make_all_review_plot_json(lst))
        print('Product JSON', product_json)
        plot_type = product_json.get('type','')
        product_html = plotly_json_to_html(product_json)
    return product_html,plot_type

def sentiment_html_plot(lst):
    sentiment_html = '<iframe></iframe>'
    plot_type = ''
    if lst:
        sentiment_json = json.loads(make_sentiment_plot_json(lst))
        print('Sentiment JSON', sentiment_json)
        sentiment_type = sentiment_json.get('type','')
        sentiment_html = plotly_json_to_html(sentiment_json)
    return sentiment_html, plot_type

@app.route('/product', methods=['GET', 'POST'])
def product():
    product_select = request.form.getlist('product_select',None)
    sentiment = request.form.get('sentiment')

    print('Sentiment',sentiment)
    print(bcolors.green,product,bcolors.endc)
    print(bcolors.blue,product_select,bcolors.endc)
    product_html, product_type = product_html_plot(product_select)
    sentiment_html, sentiment_type = sentiment_html_plot(product_select)
    if sentiment:
        word_cloud_json = make_word_cloud(product_select,sentiment)
    
        
    print('Sentiment', sentiment)
    print(bcolors.green,product,bcolors.endc)
    print(bcolors.blue,product_select,bcolors.endc)
    post = {'product_name': product_list(product_select),
            'kind': product_type,
            'sentiment_type': sentiment,
            'plotly_html': product_html}
    return render_template('dashboard.html', post=post)
