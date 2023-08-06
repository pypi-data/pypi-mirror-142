from nltk import download

from ffast.tokeniser import Tokeniser

def load() -> Tokeniser:
    download('stopwords')
    download('wordnet')
    return Tokeniser()