from flask import render_template, request, redirect, url_for
from app import app, home, accuracy_json, auc_json, f1_json
from .utils import bcolors
from Plots.time_series_plots import make_all_review_plot_json, make_sentiment_plot_json
from Plots.word_cloud import make_word_cloud
from Plots.plotly_topic_modeling import plotly_topic_frequency_bar
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import json
import base64
import pdb

py.sign_in('naddata','6eos5rv0q4')

def plotly_json_to_url(js,filename='product'):
    link = py.plot(js, filename=filename, auto_open=False)
    print(bcolors.red,link,bcolors.endc)
    return link

def plotly_json_to_html(js,filename='product', width="1000 px", height="500 px"):
    link = plotly_json_to_url(js,filename)
    iframe = '<iframe width="%s" height="%s" frameborder="0" scrolling="no" src="%s"></iframe>'
    return iframe%(width,height,link)

def wordcloud_html(src):
    try:
        print('try in wordcloud_html')
        pngdata = base64.b64encode(open(src,'rb').read())
        print(str(pngdata))
        #pdb.set_trace()
        print('All good here')
        return '<img src="data:image/png;base64,' + pngdata.decode('utf-8') + '">'
    except:
        print('Except in wordcloud_html')
        return '<img>'

def product_html_plot(lst):
    product_html = ''
    if lst:
        product_json = json.loads(make_all_review_plot_json(lst))
        product_html = plotly_json_to_html(product_json,
                                           filename='number')
    return product_html

def sentiment_html_plot(lst):
    sentiment_html = ''
    if lst:
        sentiment_json = json.loads(make_sentiment_plot_json(lst))
        sentiment_html = plotly_json_to_html(sentiment_json,
                                             filename='sentiment')
    return sentiment_html


def bar_html_plot(product,sentiment,width="800 px",height="500 px"):
    bar_html = ''
    if product and sentiment:
        bar_json = json.loads(plotly_topic_frequency_bar(product,sentiment))
        bar_html = plotly_json_to_html(bar_json, filename='bar', width=width, height=height)
    return bar_html

def product_list(lst):
    return ' | '.join(lst).rstrip(' | ')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/product', methods=['GET', 'POST'])
def product():
    product_select = request.form.getlist('product_select')

    
    print(bcolors.blue,'Product Selection:',product_select,bcolors.endc)
    product_html = product_html_plot(product_select)
    sentiment_html = sentiment_html_plot(product_select)
    positive_cloud = '<img>'
    negative_cloud = '<img>'
    if product_select != []:
        print('New word clouds!')
        positive_cloud, negative_cloud = make_word_cloud(product_select)
        positive_cloud = wordcloud_html(positive_cloud)
        negative_cloud = wordcloud_html(negative_cloud)
    
    print(bcolors.red, positive_cloud, bcolors.endc)
    print(bcolors.blue, negative_cloud, bcolors.endc)
    print(bcolors.green, product_html, bcolors.endc)
    print(bcolors.blue, sentiment_html, bcolors.endc)

    post = {'product_name': product_list(product_select),
            'sentiment_html': sentiment_html,
            'number_html': product_html,
            'positive_cloud':positive_cloud,
            'negative_cloud':negative_cloud}

    return render_template('dashboard.html', post=post)

@app.route('/ml_models')
def ml_models():
    accuracy_html = plotly_json_to_html(accuracy_json, filename='accuracy')
    auc_html = plotly_json_to_html(auc_json, filename='auc')
    f1_html = plotly_json_to_html(f1_json, filename='f1')
    post={'accuracy':accuracy_html,
          'auc':auc_html,
          'f1':f1_html}
    return render_template('ml_models.html',post=post)

@app.route('/topic_models',methods=['GET','POST'])
def topic_models():
    product = request.form.get('product')
    sentiment = request.form.get('sentiment')

    print(bcolors.red, product, bcolors.endc)
    print(bcolors.blue, sentiment, bcolors.endc)
        
    bar_html = bar_html_plot(product,sentiment, width="900 px", height="500 px")
    print(bcolors.green, bar_html, bcolors.endc)
    post = {'bar_html':bar_html}
    print(post)
    return render_template('topic_models.html',post=post)
    
