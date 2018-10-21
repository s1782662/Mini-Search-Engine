import graphlab as gl

class Operator(object):


    def __init__(self):
        self._lcollection = None
        self._rcollection = None

    def _parse(self,lcollection,rcollection,operator):
       
        _gl_type = gl.data_structures.sframe.SFrame


        if type(lcollection) is list and type(rcollection) is _gl_type:
            
            self._lcollection = lcollection
            self._rcollection = rcollection[0]['INFO'].keys()

            print 'self._rcollection',self._rcollection

        elif type(lcollection) is _gl_type and type(rcollection) is list:

           self._lcollection = lcollection[0]['INFO'].keys()
           self._rcollection = rcollection
            
        elif type(lcollection) is list and type(rcollection) is list:

            self._lcollection = lcollection
            self._rcollection = rcollection
        
        elif type(lcollection) is _gl_type and type(lcollection) is _gl_type:
            
            self._lcollection = lcollection[0]['INFO'].keys()
            self._rcollection = rcollection[0]['INFO'].keys()
    
          

        if operator == 'AND':
            return list(set(self._lcollection).intersection(set(self._rcollection)))
        elif operator == 'OR':
            return list(set(self._lcollection) | set(self._rcollection))
        elif operator == 'NOT':
            return  list(set(self._lcollection) - set(self._rcollection))
        else:
            return None










