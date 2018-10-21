#from document import Document
from xml.etree.ElementTree import parse as xmlParse
from os import path


class XmlDocument(object):

    def __init__(self):
        self._fileName = None
	self._docids = []
	self._doctexts = []
	self._docHeadLines = []

    def _throwErrIfNotFileExist(self,fName):

        try:

            fileName = self._getfLocation(fName)
            if(not path.isfile(fileName) or not path.exists(fileName)):
                raise IOError('### PLEASE PROVIDE A VALID FILE NAME')
	    
	    self._fileName = fileName

            return True

        except Exception as err:

            print('### ERROR - %s.' % (err))
            return
    
    def _getfLocation(self,fName):
	return path.realpath('./')+'/Input/'+fName

    def parse(self,fName):

        if(self._throwErrIfNotFileExist(fName)):
	   
            # Read the content from the file 
	    with open(self._fileName,'rb') as f, open(self._getfLocation('parsed.xml'),'wb') as g:
		g.write('<ROOT>\n{}\n</ROOT>'.format(f.read())) 
     
	    root = xmlParse(self._getfLocation('parsed.xml')).getroot()
	    
	    for page in list(root):
		self._docids.append(page.find('DOCNO').text)
		self._doctexts.append(page.find('TEXT').text)
		self._docHeadLines.append(page.find('HEADLINE').text)
	   
	return {'DOCID':self._docids,'TEXT':self._doctexts,'HEADLINE':self._docHeadLines}
		
		



