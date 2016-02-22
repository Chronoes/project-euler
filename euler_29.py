# -*- coding:utf-8 -*-
combos = []
for a in range( 2, 101 ):
    for b in range( 2, 101 ):
        number = a**b
        if number not in combos:
            combos.append( number )
print( len( combos ) )