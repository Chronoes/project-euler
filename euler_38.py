# -*- coding:utf-8 -*-
digits = "123456789"
pandigitals = []
for i in range( 1, 10000 ):
    n = 2
    n_str = str( i )
    n_list = [ 1 ]
    while int( n_str ) < 987654321 and len( n_str ) < 9:
        n_str += str( i * n )
        n_list += [ n ]
        n += 1
    if "".join( sorted( n_str ) ) == digits:
        pandigitals.append(( int( n_str ), i, tuple( n_list ) ))