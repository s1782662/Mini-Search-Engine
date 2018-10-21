from itertools import product
from nltk.stem import PorterStemmer as ps
from collections import defaultdict
import shlex
import re

class Search(object):

    #WS -- Word Search
    #PS -- Phrase Search 
    #BS -- Boolean Search
    #PYS -- Proximity Search  

    def __init__(self,service):
    	self._service = service
        self.stemmer = ps()
        self._operators = {'AND' :True,'OR' :True}
    
    def _parse(self,term,search_type,distance):
        
        if search_type == 'WD' :
            return self._word_search(term)        
        elif search_type == 'PH' :
            return self._phrase_search(term,1)
        elif search_type == 'PX' :
            _term = re.compile(r'\s?#\s?(\d+)\s?\(\s?([a-z]+)\s?,\s?([a-z]+)\s?\)\s?$').search(term).groups()
            term = "'"+_term[0]+' '+_term[1]+"'"
            return self._phrase_search(term,_term[2])

    def _get_word(self,term):

        try:
            return self._service._fetch_record_by_word(term)
        except Exception as err:
            return False
    
    def _word_search(self,term):
        
        _term = self._preprocess_search(term)
        record = self._get_word(_term)
    	
        if not record:
    	   print('No documents on this term %s'%(term))
           return
        return list(record[0]['INFO'])
    
    def _phrase_search(self,phrase,distance):
        
        fn = map(str,map(lambda x:x.strip('\"\''),phrase.split(' ')))                    

        _split = filter(re.compile(r'\w+').search,fn)
                  
        _split = self._preprocess_search(_split)  
        _records = self._service._fetch_records(_split,'WORD') 
        
        if len(_records) == 2:
            return self._is_doc_with_phrase(_records[0],_records[1],distance) 
        return None    
   
    def _is_doc_with_phrase(self,lrecord,rrecord,distance):
        
       _ldocs = lrecord['INFO']
       _rdocs = rrecord['INFO']

       _rsult_docs =  self._common_documents(_ldocs,_rdocs) 
       _rsult_phrase = []

       for _docIdx in _rsult_docs:
           _rsult_phrase.append(self._neighbor_terms(_ldocs[_docIdx],_rdocs[_docIdx],_docIdx,distance))          
       _phrase_rslt = map(lambda x: x[1],filter(lambda _match: _match[0] == True,_rsult_phrase))
        
       # returns documents 
       return _phrase_rslt
    
    def _neighbor_terms(self,llist,rlist,docIdx,distance):
        
        _combinations = product(llist,rlist)

        _result = filter(lambda term: abs(term[0] - term[1]) <= distance, _combinations)

        return (True if len(_result) > 0 else False,docIdx)  
    
    def _preprocess_search(self,term):     
        
        if type(term) is str:
            return str(self.stemmer.stem(term.strip(' ')))
        elif type(term) is list:
            fn = lambda word : str(self.stemmer.stem(word.strip(' ')))
            return map(fn,term)            
            
    def _common_documents(self,ldocs,rdocs):

        if type(ldocs) is dict and type(rdocs) is dict:
            _lterm = ldocs.keys()
            _rterm = rdocs.keys()
        elif type(ldocs) is list and type(rdocs) is dict:
            _lterm = ldocs
            _rterm = rdocs.keys()
        elif type(ldocs) is dict and type(rdocs) is list:
            _lterm = ldocs.keys()
            _rterm = rdocs
        else:
            _lterm = ldocs
            _rterm = rdocs
        return set(_lterm).intersection(set(_rterm))

