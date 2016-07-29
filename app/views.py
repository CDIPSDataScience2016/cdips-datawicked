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

def product_html_plot(lst):
    product_html = ''
    if lst:
        product_json = json.loads(make_all_review_plot_json(lst))
        print('Product JSON', product_json)
        product_html = plotly_json_to_html(product_json,
                                           filename='number')
    return product_html

def sentiment_html_plot(lst):
    sentiment_html = ''
    if lst:
        sentiment_json = json.loads(make_sentiment_plot_json(lst))
        print('Sentiment JSON', sentiment_json)
        sentiment_html = plotly_json_to_html(sentiment_json,
                                             filename='sentiment')
    return sentiment_html


def product_list(lst):
    return '|'.join(lst).rstrip('|')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/product', methods=['GET', 'POST'])
def product():
    product_select = request.form.getlist('product_select',None)

    print(bcolors.blue,'Product Selection:',product_select,bcolors.endc)
    product_html = product_html_plot(product_select)
    sentiment_html = sentiment_html_plot(product_select)
    if not product_select:
        pass
        #make_word_cloud(product_select,'all')
    positive_cloud = '/static/img/pos_wordcloud.png'
    negative_cloud = '/static/img/neg_wordcloud.png'
        
    print(bcolors.green,product_html,bcolors.endc)
    print(bcolors.blue,sentiment_html,bcolors.endc)
    post = {'product_name': product_list(product_select),
            'sentiment_html': sentiment_html,
            'number_html': product_html,
            'positive_cloud':positive_cloud,
            'negative_cloud':negative_cloud}
    return render_template('dashboard.html', post=post)

@app.route('/ml_models')
def ml_models():
    accuracy_json = json.load(open('app/static/accuracy_plotly.json','r'))
    auc_json = json.load(open('app/static/auc_plotly.json','r'))
    f1_json = json.load(open('app/static/f1_plotly.json','r'))
    accuracy_html = plotly_json_to_html(accuracy_json, filename='accuracy')
    auc_html = plotly_json_to_html(auc_json, filename='auc')
    f1_html = plotly_json_to_html(f1_json, filename='f1')
    post={'accuracy':accuracy_html,
          'auc':auc_html,
          'f1':f1_html}
    return render_template('ml_models.html',post=post)

@app.route('/topic_models')
def topic_models():
    return render_template('topic_models.html',post={})
    
