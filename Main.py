from util.util import _build_positional_output,_pretty_print,_save_boolean_to_file,_save_ranked_to_file
from core.queryexecuter import QueryExecuter
from document.Document  import Document
from core.rankexecuter import RankExecuter
from core.domain import Domain
import argparse

def _execute_xml_db(fName):

    print '\n\t\t\t Loading Input file\t'+fName+'into GraphLab'
    doc = Document()
    main = Domain()
    docs =  doc._registerInstances()._getInstance('XML').parse('trec.5000.xml')
    mService =  main._add_documents_to_gl(docs)
    return docs,mService

def _building_index(docs,mService,invertedIndexFName):
    print '\n\t\t\tBuilding Index file'

    posInvertIdxDm = Domain()

    _db = mService._build_index()
    posInvertIdxDm._add_terms_to_gl(_db)

    termInverted = posInvertIdxDm._build_positional_inverted_term()
    _build_positional_output(termInverted,invertedIndexFName)

    return mService,posInvertIdxDm

def _execute_rank_boolean_queries(mService,pInvertIdx,rfName,bfName,oBQuery,oRQuery):
    print'\n\t\t Executing Boolean Queries And Rank Queries'

    wCollection = mService._fetch_column('DOCID')

    qExecutor = QueryExecuter(bfName,pInvertIdx)
    rExecutor = RankExecuter(pInvertIdx)

    bResults = qExecutor._parse_queries(wCollection)
    rResults = rExecutor._parse(rfName)

    _save_boolean_to_file(oBQuery,bResults)
    _save_ranked_to_file(oRQuery,rResults)


if __name__== '__main__':

    parser = argparse.ArgumentParser(description='\t\t\tMini Search Engine\t\t')
    parser.add_argument('--db',default='trec.5000.xml',help='Please provide xml data ')
    parser.add_argument('--query',default='queries.boolean',help='Please provide file name to execute boolean queries')
    parser.add_argument('--rank',default='queries.ranked',help='Please provide file name to execute rank queries')
    parser.add_argument('--invertedIdx',default='index',help='Please provide an output file for Positional Inverted Index')
    parser.add_argument('--oBQuery',default='results.boolean',help='Please provide an output file for Boolean queries')
    parser.add_argument('--oRQuery',default='results.ranked',help='Please provice an output file for Rank queries')

    args = parser.parse_args()

    #Transferring xml data into GraphLab
    docs,mService = _execute_xml_db(args.db)
    mService,pInvertIdx = _building_index(docs,mService,args.invertedIdx)
    _execute_rank_boolean_queries(mService,pInvertIdx,args.rank,args.query,args.oBQuery,args.oRQuery)
    print('Exiting From Program')











