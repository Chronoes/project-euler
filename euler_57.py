# -*- coding:utf-8 -*-
from fractions import Fraction
from sys import setrecursionlimit


setrecursionlimit( 1100 )
def squarert_exp( root, exp ):
    if exp == 1:
        return 1 + 1/root
    else:
        return 1 + 1/( 1 + squarert_exp( root, exp - 1 ) )

count = 0
for i in range( 1, 1001 ):
    rational = str( Fraction( squarert_exp( 2, i ) )).split( "/" )
    print( rational )
    if len( rational[ 0 ] ) > len( rational[ 1 ] ): count += 1