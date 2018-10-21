from query import Query
from boperator import Operator
from os import path

class QueryExecuter(Query):

    def __init__(self,fName,domain):
        super(QueryExecuter,self).__init__()
        self._fName = fName
        self._domain = domain
        self._query = None

    def _identify_query(self,term):

        term = term.strip(' ')
        if term[0] == '"' :
            return 'PH'
        elif term[0] == '#' :
            return 'PX'
        else:
            return 'WD'


    def _parse_queries(self,wCollection=None,ofName='firstOutput'):

        self._query = super(QueryExecuter,self)._parse(self._fName)

        _save_to_file = []

        while not self._query.isEmpty():
            _query_dict =self._query.dequeue()
            print '\n Query -\t',_query_dict

            if len(_query_dict.keys()) == 1:
                _type = self._identify_query(_query_dict['lterm'])
                _save_to_file.append(sorted(self._execute_query(_query_dict['lterm'],_type)))
            else:
                lterm = _query_dict['lterm']
                rterm = _query_dict['rterm']

                _ltresults = self._execute_query(lterm,self._identify_query(lterm))
                _rtresults = self._execute_query(rterm,self._identify_query(rterm))

                _ltresults = self._execute_not(list(wCollection),_ltresults,_query_dict['lflag'])
                _rtresults = self._execute_not(list(wCollection),_rtresults,_query_dict['rflag'])
                _save_to_file.append(sorted(self._execute_operator(_query_dict['operator'],_ltresults,_rtresults)))
        return _save_to_file


    def _get_queries(self):
        return self._query._print_queries()

    def _execute_query(self,term,qtype,distance=1):

        return self._domain._doc_search(term,qtype,distance)

    def _execute_not(self,wCollection,tCollection,flag):

        op = Operator()

        if flag:
            return op._parse(wCollection,tCollection,'NOT')

        return tCollection

    def _execute_operator(self,operator,ltresults,rtresults):

        op = Operator()
        return op._parse(ltresults,rtresults,operator)









