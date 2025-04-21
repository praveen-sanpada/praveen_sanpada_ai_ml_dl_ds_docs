import spacy
import nltk
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import logging

nltk.download('punkt')
nltk.download('stopwords')

# Load pre-trained Word2Vec model (if applicable)
# Example: model = Word2Vec.load('word2vec_model.bin')

nlp = spacy.load("en_core_web_sm")  # Using spaCy for lemmatization

def load_nlp_model():
    """Load the Word2Vec or other NLP models here."""
    # Example: Load pre-trained Word2Vec model
    model = Word2Vec.load('word2vec_model.bin')
    pass

def process_query(query):
    """
    This function will process the incoming query and return the response.
    """
    # Step 1: Tokenize the query
    words = word_tokenize(query.lower())

    # Step 2: Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    # Step 3: Lemmatization (or Stemming if preferred)
    lemmatized_words = [nlp(word)[0].lemma_ for word in filtered_words]

    # Step 4: Process the query using word embeddings or keyword matching
    response = handle_query_with_embeddings(lemmatized_words)
    
    return response

def handle_query_with_embeddings(words):
    """
    Handle query processing using word embeddings (e.g., Word2Vec, GloVe).
    """
    # Example: Searching for a response in a predefined dataset
    venue_keywords = ["narendra modi stadium", "MA chidambaram stadium", "Eden gardens"]
    
    for keyword in venue_keywords:
        if any(word in keyword for word in words):
            return f"Information related to {keyword}"

    return "Sorry, I couldn't find an answer to your query."
