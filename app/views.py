from flask import render_template, request, redirect, url_for
from app import app
from .utils import bcolors
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import json
from IPython import embed

plotly.tools.set_credentials_file(username='mike-a-yen', api_key='7ijqoy41kr')


def json_to_link(fi):
    fo = open(fi)
    graph = json.loads(fo.read())
    link = py.iplot(graph['data'], filename=fi)
    return link.embed_code


def bethans_function(name):
    if name == 'Samsung Chromebook':
        return '<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~mike-a-yen/0.embed" height="525px" width="100%"></iframe>'
    else:
        return '<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~mike-a-yen/5.embed" height="525px" width="100%"></iframe>'


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


@app.route('/product', methods=['GET', 'POST'])
def product():
    print(bcolors.green, request, bcolors.endc)
    link = bethans_function(request.form.get('Product', ''))
    print(link)
    print(request.form.get('Product', ''))

    post = {'product_name': request.form.get('Product', ''),
            'kind': 'Time Series',
            'plotly_html': link}
    return render_template('dashboard.html', post=post)


@app.route('/submit_product', methods=['GET', 'POST'])
def submit_product():
    print(bcolors.red, request.form, bcolors.endc)
    print(bcolors.blue, request.form.keys(), bcolors.endc)
    for item in request.form.items():
        print(bcolors.green, item, bcolors.endc)
    print(url_for('product'))
    embed()
    return redirect(url_for('product/%s' % request.form['Product']))
