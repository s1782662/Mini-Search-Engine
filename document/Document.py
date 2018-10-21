from xmlDocument import XmlDocument

class Document(object):

    def __init__(self):
        self._instances = None
        

    def _registerInstances(self):
        self._instances = dict(XML = XmlDocument())
	return self

    def _getInstance(self,key):

	if key in self._instances:   
  	     return self._instances[key]
	else:
	     print('OOPS !!! #####  PLEASE REGISTER INSTANCES OF DOCUMENT')




