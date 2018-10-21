import graphlab as gl

class Storage(object):

    def __init__(self):
        print('')

    def _get_graphlab(self):
        return gl.SFrame()

    def _set_graphlab(self,data):
        return gl.SFrame(data)






