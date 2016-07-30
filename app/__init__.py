from flask import Flask
import pandas as pd
import os

home = os.getcwd()


all_reviews = pd.read_csv("/home/ubuntu/cdips-datawicked/data/top_10_electronics_reviews.csv", sep='\t')
all_phrases = pd.read_pickle("/home/ubuntu/cdips-datawicked/app/static/product_sentiment_phrases.pkl")

df_review = pd.read_csv("/home/ubuntu/cdips-datawicked/data/review-topic.csv")
df_topic = pd.read_csv("/home/ubuntu/cdips-datawicked/data/topic-words-reviews.csv")

app = Flask(__name__)
# app.config.from_object('config')

from app import views
