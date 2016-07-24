from flask import render_template
from app import app
import plotly


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mike'}
    posts = [{'author': 'Yaning',
              'body': 'Hello!'},
             {'author': 'Bethan',
              'body': 'Goodbye!'}]
    return render_template('plots.html',
                           title='CDIPS Data Wicked',
                           user=user,
                           posts=posts)
