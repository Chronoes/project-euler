# -*- coding:utf-8 -*-
sum = 0
for n in range( 1, 1000000 ):
    n_bin = bin( n )[ 2: ]
    n = str( n )
    if n == "".join( reversed( n ) ) and n_bin == "".join( reversed( n_bin ) ):
        sum += int( n )