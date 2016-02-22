# -*- coding:utf-8 -*-
from itertools import permutations


i = 3
unsuitable = []
while True:
    suitable = []
    if i in unsuitable: continue
    cube = str( i**3 )
    for perm in permutations( cube, len( cube ) ):
        n = int( "".join( perm ) )**(1/3)
        rounded_n = round( n )
        if abs( rounded_n - n ) < 0.0000001:
            suitable.append( rounded_n )
        else:
            unsuitable.append( rounded_n )
    if len( suitable ) == 5: break    
    i += 1
    
print( i )