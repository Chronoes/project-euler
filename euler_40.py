# -*- coding:utf-8 -*-
c = "."
for i in range( 1, 1000001 ):
    c += str( i )
prd = 1
for index in [ 1, 10, 100, 1000, 10000, 100000, 1000000 ]:
    prd *= int( c[ index ] )
    print( c[ index ], end = " " )
print()
print( prd )