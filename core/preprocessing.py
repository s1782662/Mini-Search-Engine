from stopwords import Stopwords as sW
from nltk.stem import PorterStemmer
import re


class Preprocessing(object):

    def __init__(self,pStemmer = PorterStemmer()):
        self._stopWords = sW()._parse()._get_stopwords()
        self.pStemmer = PorterStemmer()

    def _action(self,row):
        _tokens = self._tokenize(row)
        _pruned_tokens = map(lambda word: word.lower(),_tokens)
        _stemmed_tokens = self._stemming(_pruned_tokens)
        return self._rmove_stopWords(_stemmed_tokens)

    def _stemming(self,row):
        return map(lambda word: self.pStemmer.stem(word),row)

    def _tokenize(self,row):
        return filter(lambda word:re.match("^[\w]+$",word),[word for word in re.split("[\W+]",row)])

    def _rmove_stopWords(self,row):
        return [word for word in row if word not in self._stopWords ]

