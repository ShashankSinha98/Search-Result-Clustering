# https://towardsdatascience.com/elegant-text-pre-processing-with-nltk-in-sklearn-pipeline-d6fe18b91eb8
import string
import re
import contractions

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

from bs4 import BeautifulSoup
from textblob import TextBlob
from unidecode import unidecode
import pandas as pd
import numpy as np


# Lemmatize sentences according to part of speech of individual words.
def lemmatize_pos_tagged_text(text, lemmatizer, pos_tag_dict):
  sentences = nltk.sent_tokenize(text)
  new_sentences = []

  for sentence in sentences:
    sentence = sentence.lower()
    new_sentence_words = []
    #one pos_tuple for sentence
    pos_tuples = nltk.pos_tag(nltk.word_tokenize(sentence)) 

    for word_idx, word in enumerate(nltk.word_tokenize(sentence)):
      nltk_word_pos = pos_tuples[word_idx][1]
      wordnet_word_pos = pos_tag_dict.get(nltk_word_pos[0].upper(), None)
      if wordnet_word_pos is not None:
        new_word = lemmatizer.lemmatize(word, wordnet_word_pos)
      else:
        new_word = lemmatizer.lemmatize(word)

      new_sentence_words.append(new_word)

    new_sentence = " ".join(new_sentence_words)
    new_sentences.append(new_sentence)

  return " ".join(new_sentences)


# Download resouce if not existing in workspace
def download_if_non_existent(res_path, res_name):
  try:
    nltk.data.find(res_path)
  except LookupError:
    print(f'resource {res_path} not found. Downloading now...')
    nltk.download(res_name)


class NltkPreprocessingSteps:
  
    def __init__(self, dataFrame: pd.core.frame.DataFrame):
        self.X = dataFrame

        # Download necessary resources (if not available in workspace)
        download_if_non_existent('corpora/stopwords', 'stopwords')
        download_if_non_existent('tokenizers/punkt', 'punkt')
        download_if_non_existent('taggers/averaged_perceptron_tagger','averaged_perceptron_tagger')
        download_if_non_existent('corpora/wordnet', 'wordnet')
        download_if_non_existent('corpora/omw-1.4', 'omw-1.4')

        # stopwords setup
        self.sw_nltk = stopwords.words('english')
        # new_stopwords = ['<*>'] # custom new stopwords
        # self.sw_nltk.extend(new_stopwords) # Add custom new stopwords
        # self.sw_nltk.remove('not') # Remove any stopwords

        self.pos_tag_dict = {"J": wordnet.ADJ,
                        "N": wordnet.NOUN,
                        "V": wordnet.VERB,
                        "R": wordnet.ADV}
        
        # '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~' 32 punctuations in python
        # we dont want to replace . first time around
        self.remove_punctuations = string.punctuation.replace('.','')


    def remove_html_tags(self):
        self.X = self.X.apply(lambda x: BeautifulSoup(x, 'html.parser').get_text())
        return self
    
    def replace_diacritics(self):
        self.X = self.X.apply(
                lambda x: unidecode(x, errors="preserve"))
        return self
    
    def to_lower(self):
        self.X = np.apply_along_axis(lambda x: x.lower(), self.X)
        return self
    
    def expand_contractions(self):
        self.X = self.X.apply(lambda x: " ".join([contractions.fix(expanded_word) 
                            for expanded_word in x.split()]))
        return self
    
    def remove_numbers(self):
        self.X = self.X.apply(lambda x: re.sub(r'\d+', '', x))
        return self
    
    def replace_dots_with_spaces(self):
        self.X = self.X.apply(lambda x: re.sub("[.]", " ", x))
        return self
    
    def remove_punctuations_except_periods(self):
        self.X = self.X.apply(lambda x: re.sub('[%s]' %
                    re.escape(self.remove_punctuations), '' , x))
        return self
    
    def remove_all_punctuations(self):
        self.X = self.X.apply(lambda x: re.sub('[%s]' %
                            re.escape(string.punctuation), '' , x))
        return self
    
    def remove_double_spaces(self):
        self.X = self.X.apply(lambda x: re.sub(' +', ' ', x))
        return self

    def fix_typos(self):
        self.X = self.X.apply(lambda x: str(TextBlob(x).correct()))
        return self

    def remove_stopwords(self):
        # remove stop words from token list in each column
        self.X = self.X.apply(
            lambda x: " ".join([ word for word in x.split() 
                        if word not in self.sw_nltk]) )
        return self

    def lemmatize(self):
        lemmatizer = WordNetLemmatizer()
        self.X = self.X.apply(lambda x: lemmatize_pos_tagged_text(
                                x, lemmatizer, self.pos_tag_dict))
        return self

    def get_processed_text(self):
        return self.X