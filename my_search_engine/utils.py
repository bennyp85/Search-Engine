import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def tokenize(text):
    """Tokenize text using spaces and punctuation as delimiters. 
    Convert to lower case, remove stop words, and perform stemming."""
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    tokens = re.split('\W+', text.lower())
    tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
    return tokens