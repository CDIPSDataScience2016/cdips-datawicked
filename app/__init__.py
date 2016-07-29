from flask import Flask
import pandas as pd

all_reviews = pd.read_csv("data/top_10_electronics_reviews.csv", sep='\t')
app = Flask(__name__)
# app.config.from_object('config')

from app import views
