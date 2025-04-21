from gensim.models import Word2Vec
import nltk
from nltk.tokenize import word_tokenize
import logging

nltk.download('punkt')

# Sample text data for training
corpus = [
    "Narendra Modi Stadium is located in Ahmedabad.",
    "MA Chidambaram Stadium is one of the oldest stadiums in India.",
    "Eden Gardens is the iconic cricket ground in Kolkata.",
    "The Narendra Modi Stadium is famous for hosting large crowds."
]

# Tokenize the text data
sentences = [word_tokenize(sentence.lower()) for sentence in corpus]

# Train the Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# Save the trained model
model.save("models/word2vec_model.bin")

# You can load the model later with: model = Word2Vec.load('models/word2vec_model.bin')
