def plotly_topic_frequency_bar(product_id, sentiment):

    asin_dic = {'B0074BW614': 'Kindle Fire',
            'B00DR0PDNE': 'Google Chromecast',
            'B007WTAJTO': 'SanDisk Memory Card',
            'B006GWO5WK': 'Kindle Powerfast Charger',
            'B007R5YDYA': 'Kindle Paperwhite Case',
            'B00622AG6S': 'Powergen Car Charger',
            'B008OHNZI0': 'Privacy Screen for IPhone 5',
            'B009SYZ8OC': 'USB to Lightning Cable',
            'B00BGA9WK2': 'Sony PlayStation 4',
            'B004QK7HI8': 'Mohu Leaf 30 TV Antenna'}

    import json
    import pandas as pd
    import numpy as np
    import plotly
    import plotly.plotly as py
    import plotly.graph_objs as go

    py.sign_in('naddata', '6eos5rv0q4')

    nshow = 50
    threshold = 0.5

    df_review = pd.read_csv('../data/review-topic.csv')
    df_topic = pd.read_csv('../data/topic-words-reviews.csv')

    # product_id = 'B0074BW614'

    if sentiment == 'positive':
        df = df_topic[df_topic['Sentiment'] == 1]
    elif sentiment == 'negative':
        df = df_topic[df_topic['Sentiment'] == 0]
    # elif sentiment == 'all':
    #     df = df_topic

    TID = df.Topic_ID.tolist()
    TID_label = ['Topic ' + str(i) for i in TID]
    rev_prob = [eval(rev) for rev in df.Reviews.tolist()]
    rev_prob = [[freq for freq in freq1 if freq[1] > threshold]
                for freq1 in rev_prob]
    frequency = [len(freq) for freq in rev_prob]
    sort_idx = np.argsort(np.array(frequency))
    frequency_sorted = list(np.array(frequency)[sort_idx])
    TID_label_sorted = list(np.array(TID_label)[sort_idx])

    layout = go.Layout(title='Frequency of reviews related to each topic '
                       'for product ' + product_id,
                       xaxis=dict(
                           title='Review frequency'
                       ),
                       yaxis=dict(
                           title='Topics'
                       ),
                       showlegend=True,
                       height=800)

    data = [go.Bar(x=frequency_sorted[-nshow:],
                   y=TID_label_sorted[-nshow:],
                   orientation='h')]

    fig = go.Figure(data=data, layout=layout)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return fig_json

    # with open('topic_freq.json', 'w') as fh:
    #    fh.write(fig_js)
