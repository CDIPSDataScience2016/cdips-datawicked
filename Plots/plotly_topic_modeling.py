import json
import pandas as pd
import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from app import df_review, df_topic

py.sign_in('naddata', '6eos5rv0q4')

#df_review = pd.read_csv('../data/review-topic.csv')
#df_topic = pd.read_csv('../data/topic-words-reviews.csv')


asin_dic = {'B0074BW614': 'Kindle Fire',
            'B00DR0PDNE': 'Google Chromecast',
            'B007WTAJTO': 'SanDisk memory card',
            'B006GWO5WK': 'Kindle Powerfast Charger',
            'B007R5YDYA': 'Kindle Paperwhite Case',
            'B00622AG6S': 'Powergen Car Charger',
            'B008OHNZI0': 'Privacy Screen for iPhone 5',
            'B009SYZ8OC': 'USB to lightning charger',
            'B00BGA9WK2': 'Sony PlayStation 4',
            'B004QK7HI8': 'Mohu Leaf 30 TV Antenna'}

inv_asin_dic = {k: v for v, k in asin_dic.items()}


def plotly_topic_frequency_bar(product_id, sentiment):

    nshow = 50
    threshold = 0.5

   # product_id = 'B0074BW614'

    if sentiment == 'positive':
        df = df_topic[df_topic['Sentiment'] == 1]
    elif sentiment == 'negative':
        df = df_topic[df_topic['Sentiment'] == 0]

    TID = df.Topic_ID.tolist()
    TID_label = ['Topic ' + str(i) for i in TID]
    rev_prob = [eval(rev) for rev in df.Reviews.tolist()]
    rev_prob = [[freq for freq in freq1 if freq[1] > threshold
                 and df_review.loc[freq[0], 'ProductID'] ==
                 inv_asin_dic[product_id]]
                for freq1 in rev_prob]
    frequency = [len(freq) for freq in rev_prob]
    sort_idx = np.argsort(np.array(frequency))
    frequency_sorted = list(np.array(frequency)[sort_idx])
    TID_label_sorted = list(np.array(TID_label)[sort_idx])
    TID_sorted = list(np.array(TID)[sort_idx])

    if sentiment == 'positive':
        ylabel = [', '.join([pair[0] for pair in
                             eval(df_topic.loc[TID, 'Words_and_Weights'])[:5]])
                  for TID in TID_sorted]
    elif sentiment == 'negative':
        ylabel = [', '.join([pair[0] for pair in
                             eval(df_topic.loc[TID+200, 'Words_and_Weights'])[:5]])
                  for TID in TID_sorted]

    layout = go.Layout(title='Frequency of reviews related to each topic '
                       'for product ' + product_id,
                       xaxis=dict(
                           title='Review frequency'
                       ),
                       # yaxis=dict(
                       #     title='Topics'
                       # ),
                       showlegend=False,
                       margin=go.Margin(l=400),
                       height=800)

    data = [go.Bar(x=frequency_sorted[-nshow:],
                   # y=TID_label_sorted[-nshow:],
                   y=ylabel[-nshow:],
                   orientation='h')]

    fig = go.Figure(data=data, layout=layout)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return fig_json

    # with open('topic_freq.json', 'w') as fh:
    #    fh.write(fig_js)
