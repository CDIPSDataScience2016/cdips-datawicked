#Read in data (this can be done at start of the app)
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from palettable.colorbrewer.sequential import Reds_9
from palettable.colorbrewer.sequential import Greens_9

all_phrases = pd.read_pickle("../app/static/product_sentiment_phrases.pkl")

#Get positive and negative noun phrases for a specific product
def get_phrases(product):
    pos_phrases =[]
    neg_phrases = []
    product_phrases = all_phrases[all_phrases["product_name"] == product]
    positive_phrases = product_phrases["positive_phrases"].tolist()
    negative_phrases = product_phrases["negative_phrases"].tolist()
    return positive_phrases[0], negative_phrases[0]

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


# Colour functions for positive and negative word clouds

def pos_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Greens_9.colors[random.randint(2,8)])
def neg_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Reds_9.colors[random.randint(2,8)])

# Make word clouds from product string or list of product strings
def make_word_cloud(products):
    if type(products) == str:
        new_pos_phrases, new_neg_phrases = get_phrases(products)
        freq_pos = get_word_freq(new_pos_phrases)
        freq_neg = get_word_freq(new_neg_phrases)

        pos = freq_pos.head(10)
        neg = freq_neg.head(10)

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

    elif type(products) == list:
        list_pos = []
        list_neg = []
        for product in products:
            new_pos_phrases, new_neg_phrases = get_phrases(product)
            freq_pos = get_word_freq(new_pos_phrases)
            freq_neg = get_word_freq(new_neg_phrases)

            pos = freq_pos.head(10)
            neg = freq_neg.head(10)

            list_pos.append(pos)
            list_neg.append(neg)

        all_pos = pd.concat(list_pos)
        all_neg = pd.concat(list_neg)

        all_pos.index = range(0,len(all_pos))
        all_neg.index = range(0,len(all_neg))

        pos_words_array = []
        neg_words_array = []
        for i in range(0,len(all_pos)):
            pos_words_array.append((all_pos["vocab"][i].upper(), float(all_pos["count"][i])))

        for i in range(0,len(all_neg)):
            neg_words_array.append((all_neg["vocab"][i].upper(), float(all_neg["count"][i])))

        wc = WordCloud(background_color="white", max_words=2000,
               max_font_size=300, random_state=42)

        # generate word cloud for positive
        positive_name = '../app/static/img/pos_wordcloud.png'
        wc.generate_from_frequencies(pos_words_array)
        wc.recolor(color_func=pos_color_func, random_state=3)
        wc.to_file(positive_name)

        # generate word cloud for negative
        negative_name = '../app/static/img/neg_wordcloud.png'
        wc.generate_from_frequencies(neg_words_array)
        wc.recolor(color_func=neg_color_func, random_state=3)
        wc.to_file(negative_name)        
