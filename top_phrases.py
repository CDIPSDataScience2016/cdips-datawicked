
# coding: utf-8

# Read in data for products and assign product names (this should be automated from meta data in the future

# In[2]:

import pandas as pd
all_reviews = pd.read_csv("./data/top_10_electronics_reviews.csv", sep='\t')


# Work out number of product reviews for each product. Maybe this will be useful at some point

# In[14]:

number_product_reviews = all_reviews.groupby([all_reviews.product_name]).overall.count()

number_product_reviews.head(10)


# In[3]:

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


# In[4]:

#This function returns top five negative and positive words for a given product

def get_top_five_phrases(products,sentiment):
    if type(products) == str:
        reviews = all_reviews[all_reviews["product_name"] == products]
        
        blobs = product_to_blobs(reviews)
        positive_phrases, negative_phrases = sort_sentiment_phrases(blobs)
        freq_pos = get_word_freq(positive_phrases)
        freq_neg = get_word_freq(negative_phrases)
        
        top_five_pos = freq_pos.head(5)
        top_five_neg = freq_neg.head(5)
        
        if sentiment == "positive":
            return top_five_pos
        elif sentiment == "negative":
            return top_five_neg
        elif sentiment == "all":
            return top_five_pos, top_five_neg
        else:
            print("Error: Incorrect sentiment type, try positive, negative or all")


# In[19]:

pos, neg = get_top_five_phrases("Sony PlayStation 5", "all")


# In[21]:

pos


# In[ ]:



