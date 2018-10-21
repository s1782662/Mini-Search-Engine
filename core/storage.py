import graphlab as gl


class Storage(object):

    def __init__(self,glab = gl):
	   self._gl = glab
       self._pos_gl = glab
       self._data = None

    def _getGraphLab(self):
	return self._gl

    def _transformData(self,data):
	self._data = self._gl.SFrame(data)
        return self

    def _get_transformed_version(self):
	return self._data

    def _get_positional_data_frame(self):
        return self._pos_gl

    def _set_data_positional_data_frame(self,word,docs):
        self._pos_gl = self._pos_gl.SFrame({'Word':word,'Docs':docs})
        return self


    def _reset_all_instances(self):
        print '#### FACTORY RESET... DO YOU WISH TO CONTINUE (Y/N)..'



