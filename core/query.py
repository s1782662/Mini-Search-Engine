from nltk.stem import PorterStemmer as ps
from os import path
import shlex
import re

class Query(object):

    def __init__(self):
        self._stack = []

    def isEmpty(self):
        return (self._stack == [])

    def enqueue(self,item):
        self._stack.insert(0,item)

    def dequeue(self):
        return self._stack.pop()

    def size(self):
        return len(self._stack)

    def _print_queries(self):
        return self._stack

    def _get_location(self,fName):

        return path.realpath('./')+'/Input/'+fName+'.txt'

    def _throwErrIfNotFileExist(self,fName):

        try:

            fileName = self._get_location(fName)
            if(not path.isfile(fileName) or not path.exists(fileName)):
                raise IOError('### PLEASE PROVIDE A VALID FILE NAME')
            return True
        except Exception as err:
            print('### ERROR - %s.' % (err))
            return


    def _parse(self,fName):

        if(self._throwErrIfNotFileExist(fName)):

            _fName = self._get_location(fName)

            _queries = None

            with open(_fName,'r') as f:
                _queries = [line[2:] for line in f]

            self._process_query(_queries)

            return self


    def _process_query(self,queries):

        _queries = []

        if queries is not None:
            _queries = map(lambda x:x.rstrip('\r\n').strip(' '),queries)

        for query in _queries:
            self._make_query(query)

    def _find_not_in_term(self,term):

        _proximity_query = re.compile(r'(.?)\s?#\s?(\d+)\s?\(\s?([a-z]+)\s?,\s?([a-z]+)\s?\)\s?$')

        if _proximity_query.match(term):

            _tmp = _proximity_query.search(term).groups()
            _text = '#'+_tmp[1]+'('+_tmp[2]+','+_tmp[3]+')'
            _w_string = _tmp[0]+' '+_text

            if 'NOT' in shlex.split(_w_string):
                return (_text,True)
            return(_text,False)
        else:
            _flag = True if term.find('"') is not -1 else False

            _w_string = shlex.split(term)

            _quotes = '"'
            if 'NOT' in _w_string:
                return (_quotes+_w_string[1]+_quotes if _flag else _w_string[1],True)
            else:
                return (_quotes+_w_string[0]+_quotes if _flag else _w_string[0],False)



    def _make_query(self,query):

        _ps = ps()
        sub_queries = shlex.split(query)

        _and_query =  re.compile(r'(.+)(\bAND\b|\bOR\b)(.+)')
        _hash_query = re.compile(r'\s?#\s?(\d+)\s?\(\s?([a-z]+)\s?,\s?([a-z]+)\s?\)\s?$')

        if _and_query.match(query):

            _result = _and_query.search(query).groups()

            _lterm,lflag = self._find_not_in_term(_result[0])

            _rterm,rflag = self._find_not_in_term(_result[2])

            self.enqueue({'lterm' :_lterm.lower(),'operator':_result[1],'rterm' :_rterm.lower(),'lflag':lflag,'rflag':rflag})

        elif _hash_query.match(query):

            _result =  _hash_query.search(query).groups()
            term = '#'+_result[0]+'('+_result[1].lower()+','+_result[2].lower()+')'
            self.enqueue({'lterm' :term})
        elif len(sub_queries) == 1:
            fn = lambda word:word.lower()
            sub_queries = map(fn,sub_queries)
            _quotes = '"'
            if len(sub_queries[0].split(' ')) > 1:
                self.enqueue({'lterm' :_quotes+sub_queries[0]+_quotes})
            else:
                self.enqueue({'lterm':sub_queries[0]})

