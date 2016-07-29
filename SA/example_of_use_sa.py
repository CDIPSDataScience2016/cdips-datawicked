import pickle
# Load the sentiment analysis classifier 
sa = pickle.load(open('sa.p', 'rb'))
# Vectorizing a new review, the review has to be cleaned and each review is a list of words
tf = sa.NLP_model_predict(['bad', 'bad', 'bad', 'bad', 'bad', 'bad' 'bad'])
# Predict the sentiment
pr = sa.predict_ML_model(tf)
