# -*- coding:utf-8 -*-

d = {}
def tee( r, v ):
    if r == 0 or v == 0:
        return 1
    elif ( r, v ) in d:
        return d[( r, v )]
    else:
        d[( r, v )] = tee( r - 1, v ) + tee( r, v - 1 )
        return d[( r, v )]

print( tee( 20, 20 ) )