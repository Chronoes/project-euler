# -*- coding:utf-8 -*-

def collatz( n, nr = 1 ):
    if n == 1:
        return nr
    elif n % 2 == 0:
        return collatz( n / 2, nr + 1 )
    else:
        return collatz( 3 * n + 1, nr + 1 )

nrs = []
for i in range( 1, 1000000, 2 ):
    nrs.append( collatz( i ) )

print( nrs.count( max( nrs ) ), nrs.index( max( nrs ) ) - 1 )