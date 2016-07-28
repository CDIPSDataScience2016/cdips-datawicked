
# The code take an input of a single product name and the sentiment (which can be positive, negative or all) and saves a word cloud of the most positive or negative noun phrases as a .png file.

# Read in data for products with product names assigned

import pandas as pd
all_reviews = pd.read_csv("./data/top_10_electronics_reviews.csv", sep='\t')

import datetime
import json
import nltk.data
from textblob import TextBlob
import re
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
import numpy as np
import re
import nltk
import string

from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.corpus import stopwords

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

#Converts individual review text to text blobs. Each part of blobs list in a sentence
def review_to_blobs( review, tokenizer ):
    blobs = []

    if type(review) != str:
        print(type(review))
    sentences = tokenizer.tokenize(review.strip())
    for sentence in sentences:
        if len(sentence) > 0:
            sentence = re.sub("[^a-zA-Z]", " ", sentence)
            blobs.append(TextBlob(sentence))
    return blobs

#Makes list of text blobs (each part of list is a review).
def product_to_blobs(popular_product):
    blobs = []

    print("Parsing sentences from training set")
    icount = 1
    for review in popular_product["reviewText"]:
        icount += 1
        if icount%1000 == 0:
            print("Cleaning and tokenizing review", icount, "of", len(popular_product))
        if type(review) == str:
            blobs += review_to_blobs(review, tokenizer)

    return blobs

#Sort review sentences into positive and negative and find noun phrases
def sort_sentiment_phrases(blobs):
    positive_sentences = []
    negative_sentences = []

    positive_noun_phrases = []
    negative_noun_phrases = []
    for blob in blobs:
        if blob.polarity > 0.3:
            positive_sentences.append(blob)
            positive_noun_phrases.append(blob.noun_phrases)
        elif blob.polarity < -0.3:
            negative_sentences.append(blob)
            negative_noun_phrases.append(blob.noun_phrases)

    negative_phrases = []
    for noun_phrases in negative_noun_phrases:
        for noun_phrase in noun_phrases:
            negative_phrases.append(noun_phrase)

    positive_phrases = []
    for noun_phrases in positive_noun_phrases:
        for noun_phrase in noun_phrases:
            positive_phrases.append(noun_phrase)

    return positive_phrases, negative_phrases

#Find frequency of the noun phrases
def get_word_freq(words):
    vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, max_features = 1000, ngram_range=(2,3))

    word_features = vectorizer.fit_transform(words)
    word_features = word_features.toarray()

    vocab = vectorizer.get_feature_names()

    dist = np.sum(word_features, axis=0)

    word_freq = {'count': dist, 'vocab': vocab}
    word_freq = pd.DataFrame(word_freq)
    word_freq = word_freq.sort_values(by="count",ascending=False)
    return word_freq

#This function returns top five negative and positive words for a given product

def get_top_five_phrases(products,sentiment):
    if type(products) == str:
        reviews = all_reviews[all_reviews["product_name"] == products]

        blobs = product_to_blobs(reviews)
        positive_phrases, negative_phrases = sort_sentiment_phrases(blobs)
        freq_pos = get_word_freq(positive_phrases)
        freq_neg = get_word_freq(negative_phrases)

        top_five_pos = freq_pos.head(10)
        top_five_neg = freq_neg.head(10)

        if sentiment == "positive":
            return top_five_pos
        elif sentiment == "negative":
            return top_five_neg
        elif sentiment == "all":
            return top_five_pos, top_five_neg
        else:
            print("Error: Incorrect sentiment type, try positive, negative or all")


# Generate wordcloud using wordcloud library
#https://github.com/amueller/word_cloud
#Formatting help from https://github.com/minimaxir/stylistic-word-clouds

import numpy as np
import csv
import random
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from palettable.colorbrewer.sequential import Reds_9
from palettable.colorbrewer.sequential import Greens_9

def pos_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Greens_9.colors[random.randint(2,8)])
def neg_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Reds_9.colors[random.randint(2,8)])

def make_word_cloud(product, sentiment):
    if sentiment == "all":
        pos, neg = get_top_five_phrases(product,sentiment)

        pos.index = range(0,len(pos))
        neg.index = range(0,len(neg))

        pos_words_array = []
        neg_words_array = []
        for i in range(0,len(pos)):
            pos_words_array.append((pos["vocab"][i].upper(), float(pos["count"][i])))

        for i in range(0,len(neg)):
            neg_words_array.append((neg["vocab"][i].upper(), float(neg["count"][i])))

        wc = WordCloud(background_color="white", max_words=2000,
               max_font_size=300, random_state=42)

        # generate word cloud for positive
        wc.generate_from_frequencies(pos_words_array)
        wc.recolor(color_func=pos_color_func, random_state=3)
        wc.to_file("pos_wordcloud.png")

        # generate word cloud for negative
        wc.generate_from_frequencies(neg_words_array)
        wc.recolor(color_func=neg_color_func, random_state=3)
        wc.to_file("neg_wordcloud.png")

#make_word_cloud("Sony PlayStation 5", "all")
