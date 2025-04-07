import nltk
nltk.download('punkt')
nltk.download('stopwords')

import spacy
try:
    nlp = spacy.load("en_core_web_sm")
except:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")
from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
