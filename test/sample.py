

import graphlab as gl


s = gl.SFrame({'Name':['cilic','Text'],'value':[{'cilic':[{'james':[2,3,4]},{'johnson':[4,5,6]} ]},{'Text':[{'TTDS':[1,2,3]}]}]}  )


try:
    print s['James']
except Exception as err:
    print 'Thrown an exception'







