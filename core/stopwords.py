from os import path

class Stopwords(object):

     def __init__(self):
         self._stopWords = None

     def _throwErrIfNotFileExist(self,fName):

         try:

             fileName = self._getfLocation(fName)
             
             if(not path.isfile(fileName) or not path.exists(fileName)):
		        raise IOError('### PLEASE PROVIDE A VALID FILE FOR STOP WORDS')
	     
             return True

     	 except Exception as err:

             print ('#### ERROR -%s.' %(err))
             return


     def _getfLocation(self,fName):

         return path.realpath('./')+'/Input/'+fName

     def _parse(self,fName='englishST.txt'):
     
         if(self._throwErrIfNotFileExist(fName)):
             
             words = None
             
             with open(self._getfLocation(fName),'rb') as f:
                 words = f.readlines()

    	     self._stopWords = [word.rstrip('\r\n') for word in words]
             
             return self
         return


     def _get_stopwords(self):
         return list(self._stopWords) if self._stopWords is not None else []



