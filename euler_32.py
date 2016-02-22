# -*- coding:utf-8 -*-
digits = "123456789"
mult_len = 0
prd_sum = []
for i in range( 1, 9876 ):
    for j in range( 1, 9876 ):
        prd = i * j
        prd_string = str( i ) + str( j ) + str( prd )
        mult_len = len( prd_string )
        if mult_len == len( digits ) and sorted( prd_string ) == list( digits ) and prd not in prd_sum:
            print( i, j, prd )
            prd_sum.append( prd )
        elif mult_len > 9:
            break
print( sum( prd_sum ) )