from storage_layer import Storage

class Service(object):

    def __init__(self):
        self._gl = Storage()._get_graphlab()
    
    def _insert_records(self,records):
        
        self._gl = self._gl.append(Storage()._set_graphlab(records))
        return self

    def _fetch_record_by_word(self,word):
        return self._gl[self._gl['WORD'] == word]

    def _fetch_record_by_docid(self,docid):
        return self._gl[self._gl['DOCID'] == docid]

    def _fetch_records(self,filters,column_name):
        return self._gl.filter_by(filters,column_name)
    
    def _fetch_column(self,column_name):
	    return self._gl[column_name] 
	
    def _apply_operation(self,column_name,fn):
        return self._gl[column_name].apply(fn)
    
    def _update_gl(self,gl):
	    self._gl = gl

    def _get_sFrame_data(self):
	    return self._gl if self._gl is not None else None
    
    def _add_column(self,column_name,data):
	    self._gl.add_column(data,name=column_name) 
    
    def _filter_custom_sframe(self,sframe,filters,column_name):
        return sframe.filter_by(filters,column_name)

    def _get_service(self):
	    return self
