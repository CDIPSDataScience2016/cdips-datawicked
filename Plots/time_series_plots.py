#The functions make_all_review_plot_json and make_sentiment_plot_json take a single product or list of products as parameters and return the plotly plot as a json file. 

# Read in data for products and assign product names (this should be automated from meta data in the future
import pandas as pd
all_reviews = pd.read_csv("data/top_10_electronics_reviews.csv", sep='\t')


# Everything before this point can be done when the web page is initially loaded, everything after this point will update when parameters are given. Currently only parameter is product, although multiple products can be given as a list (they will all be plotted on the same graph). 

import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import json

#Converts time to datetime and returns pandas dataframe with date and number of reviews for one product
def organize_product_reviews(product):
    #Convert data to correct type
    product['unixReviewTime'] = pd.to_datetime(product['unixReviewTime'],unit='s')
    product["overall"] = product["overall"].astype(int)
    
    #
    time_dist=product.groupby([product.unixReviewTime.dt.year,product.unixReviewTime.dt.month]).overall.count()

    df_time = time_dist.to_frame()
    df_time["date"] = pd.to_datetime( time_dist.index, format='(%Y, %m)')
    
    return df_time

#returns a pandas dataframs of time and %positive reviews for a single product
def sentiment_reviews(product):
    #Convert data to correct type
    product['unixReviewTime'] = pd.to_datetime(product['unixReviewTime'],unit='s')
    product["overall"] = product["overall"].astype(int)
    
    product = product[product["overall"] != 3]
    product["sentiment"] = product["overall"] >= 4
    
    pos_product = product[product["sentiment"] == True]
    neg_product = product[product["sentiment"] == False]
    #
    time_dist=product.groupby([product.unixReviewTime.dt.year,product.unixReviewTime.dt.month]).overall.count()
    pos_dist = pos_product.groupby([pos_product.unixReviewTime.dt.year,pos_product.unixReviewTime.dt.month]).sentiment.count()
    neg_dist = neg_product.groupby([neg_product.unixReviewTime.dt.year,neg_product.unixReviewTime.dt.month]).summary.count()


    result = pd.concat([time_dist, pos_dist,neg_dist], axis=1, join_axes=[time_dist.index])
    result["date"] = pd.to_datetime( result.index, format='(%Y, %m)')
    
    result["sentiment_score"] = result["sentiment"]*100/result["overall"][result["overall"] > 2]
    
    return result

#Generates plotly plot of all reviews vs time for a single product or list of products
def make_all_review_plot_json(products):
    print('In make_all_reiview_plot_json')
    data = []
    
    if type(products) == str:
        reviews = all_reviews[all_reviews["product_name"] == products]
        product_time = organize_product_reviews(reviews)
    
        trace = go.Scatter(
            x=product_time["date"][product_time["overall"] > 1],
            y=product_time["overall"][product_time["overall"] > 1],
            name=products
        )
        data = [trace]
    elif type(products) == list:
    
        for product in products:
            reviews = all_reviews[all_reviews["product_name"] == product]
            product_time = organize_product_reviews(reviews)
    
            trace = go.Scatter(
                x=product_time["date"][product_time["overall"] > 1],
                y=product_time["overall"][product_time["overall"] > 1],
                name=product
            )
            data.append(trace)
    else:
        print("Error: incorrect type for products. Try string or list.")


    layout = go.Layout(
        title='Reviews vs time',
        xaxis=dict(
            title='Date',
        ),
        yaxis=dict(
            title='Number of reviews',
        ),
        showlegend=True
    )

    fig = go.Figure(data=data, layout=layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#    with open('Ipad_and_Kindle.json', 'w') as outfile:
#        return json.dump(fig, outfile, cls=plotly.utils.PlotlyJSONEncoder)

#Generates plotly plot of % positive reviews vs time for single product or list of products
def make_sentiment_plot_json(products):
    data = []
    
    if type(products) == str:
        reviews = all_reviews[all_reviews["product_name"] == products]
        sent_product = sentiment_reviews(reviews)
    
        trace = go.Scatter(
            x=sent_product["date"][sent_product["overall"] > 1],
            y=sent_product["sentiment_score"][sent_product["overall"] > 1],
            name=products
        )
        data = [trace]
    elif type(products) == list:
    
        for product in products:
            reviews = all_reviews[all_reviews["product_name"] == product]
            sent_product = sentiment_reviews(reviews)
    
            trace = go.Scatter(
                x=sent_product["date"][sent_product["overall"] > 1],
                y=sent_product["sentiment_score"][sent_product["overall"] > 1],
                name=product
            )
            data.append(trace)
    else:
        print("Error: incorrect type for products. Try string or list.")


    layout = go.Layout(
        title='Sentiment vs time',
        xaxis=dict(
            title='Date',
        ),
        yaxis=dict(
            title='% of positive reviews',
        ),
        showlegend=True
    )

    fig = go.Figure(data=data, layout=layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#    with open('Ipad_and_Kindle_sentiment.json', 'w') as outfile:
#        return json.dump(fig, outfile, cls=plotly.utils.PlotlyJSONEncoder)

