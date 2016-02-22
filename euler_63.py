# -*- coding:utf-8 -*-
suitable = [ 1 ]
    
for c in range( 1, 22 ):
    for a in range( 2, 10 ):
        nr = a**c
        if len( str( nr )) == c: suitable.append( nr )