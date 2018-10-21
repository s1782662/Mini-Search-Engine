from document.Document import Document as Doc
from core.storage import Storage
from util.stopwords import Stopwords
from collections import defaultdict
from core.preprocessing import Preprocessing
import string
import re

stopWords = Stopwords()._parse()._get_stopwords()
_db = defaultdict(dict)

def _update_db(index,term,docid):
    if _db.get(term,False):
        if _db[term].get(docid,False):
            _db[term][docid].update([index])
        else:
            _db[term][docid] = set([index])
    else:
	_db[term][docid] = set([index])

if __name__== '__main__':

    processing = Preprocessing()
    print('Hurray !!! Program Started')
    data = Doc()._registerInstances()._getInstance('XML').parse('data.xml')
    glData = Storage()._transformData(data)._get_transformed_version()

    glData['tokens']=glData['TEXT'].apply(lambda row:processing._action(row))
    print 'tokens',glData['tokens']

    result = zip(glData['DOCID'],glData['tokens'])
	
    print 'result',result

    for docid,etW in result:
        map(lambda term : _update_db(term[0],term[1],docid),list(enumerate(etW)))

    p_in_idx = Storage()._set_data_positional_data_frame(_db.keys(),_db.values())._get_positional_data_frame()

    print p_in_idx[(p_in_idx['Word'] == 'pink') | (p_in_idx['Word'] == 'wink') | (p_in_idx['Word'] == 'drink')]
