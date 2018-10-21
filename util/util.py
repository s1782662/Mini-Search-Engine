from os import path


def _get_location(_fName):
    return path.realpath('./')+'/Output/'+_fName+'.txt'


def _save_boolean_to_file(_fName,_data):

    _fName = _get_location(_fName)

    _enumerated_docs = enumerate(_data)

    with open(_fName,'wb') as f:
        for i,docs in _enumerated_docs:
            for idx in docs:
                f.write('\n{0} {1} {2} {3} {4} {5}'.format(i+1,0,idx,0,1,0))

def _save_ranked_to_file(_fName,_data):

    _fName = _get_location(_fName)

    _enumerated_docs = enumerate(_data)

    with open(_fName,'w') as f:
        for query_idx,docs in _enumerated_docs:
            for doc in docs:
                f.write('\n{0} {1} {2} {3} {4} {5}'.format(query_idx+1,0,doc[0],0,doc[1],0))




def _build_positional_output(_data,_fName):

    _fName = _get_location(_fName)

    _space = ' '*3

    with open(_fName,'wb') as f:

	for eRow in _data:
	    f.write(eRow['WORD']+_space+'(df:'+str(len(eRow['INFO'].keys()))+'):')
	    for eDoc,ePos in eRow['INFO'].iteritems():
                f.write('\n\t'+eDoc+':'+_space+'(tf:'+str(len(ePos))+')'+','.join(map(str,map(int,ePos))))
            f.write('\n')

def _pretty_print(_data):

    print('\n Term \n \t'+_data['WORD'][0]+'\n')
    for (doc,positions) in _data['INFO'][0].iteritems():
        _positions = ','.join(map(str,map(int,positions)))
	print ('\tDocument #%s - %s'%(doc,_positions))











