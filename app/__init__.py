from flask import Flask
import pandas as pd
import os

home = os.getcwd()
all_reviews = pd.read_csv(os.path.join(home,"data/top_10_electronics_reviews.csv"), sep='\t')
all_phrases = pd.read_pickle(os.path.join(home,"app/static/product_sentiment_phrases.pkl"))

df_review = pd.read_csv(os.path.join(home,"data/review-topic.csv"))
df_topic = pd.read_csv(os.path.join(home,"data/topic-words-reviews.csv"))

app = Flask(__name__)
# app.config.from_object('config')

from app import views
