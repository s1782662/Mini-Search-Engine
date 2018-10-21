from preprocessing import Preprocessing
from service import Service
from collections import defaultdict
from search import Search

class Domain(object):

    def __init__(self):

        self._service = Service()
        self._pre_processing = Preprocessing()
        self._cache_term = defaultdict(dict)
        self._search = None

    def _update_term(self,index,term,docId):

        if self._cache_term.get(term,False):
	        if self._cache_term[term].get(docId,False):
	            self._cache_term[term][docId].update([index])
	        else:
    		    self._cache_term[term][docId] = set([index])
        else:
	        self._cache_term[term][docId] = set([index])

    def _add_documents_to_gl(self,docs):

        self._service._insert_records(docs)
        return self

    def _add_terms_to_gl(self,terms):

        terms = {'WORD':terms.keys(),'INFO':terms.values()}
        self._service._insert_records(terms)
        return self

    def _apply_preprocessing(self,column_name,fn):

        return self._service._apply_operation(column_name,fn)

    def _combine_SArray(self,larr,rarr):

        return zip(larr,rarr)

    def _fetch_details_by_word(self,word):

        return self._service._fetch_record_by_word(word)

    def _build_index(self):

        fn = lambda row: row['HEADLINE']+' '+row['TEXT']

        _combined_cols = self._apply_preprocessing(['HEADLINE','TEXT'],fn)

        self._service._add_column('RAW_TEXT',_combined_cols)

        fn = lambda row:self._pre_processing._action(row)

        docs_tokenized = self._apply_preprocessing('RAW_TEXT',fn)

        doc_ids = self._service._fetch_column('DOCID')

        _cache = self._combine_SArray(doc_ids,docs_tokenized)

        fn = lambda term: self._update_term(term[0],term[1],docId)

        for docId,eWord in _cache:
            map(fn,list(enumerate(eWord)))

    	return self._cache_term

    def _build_positional_inverted_term(self):

        return self._service._get_sFrame_data()

    def _fetch_column(self,colName):
        return self._service._fetch_column(colName)

    def _fetch_records(self,filters,col_name):
        return self._service._fetch_records(filters,col_name)

    def _doc_search(self,term,search_type,distance):

    	if self._search ==  None:
	        service = self._service._get_service()
	        self._search = Search(service)
    	return self._search._parse(term,search_type,distance)



    def _doc_details(self,_doc_id):

	    return self._service._fetch_record_by_docid(str(_doc_id))
