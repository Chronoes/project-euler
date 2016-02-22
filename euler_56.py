# -*- coding:utf-8 -*-
a = 99
max_sum = 0
for b in range( 10, 99 ):
    digit_sum = sum( int( n ) for n in str( a**b ) )
    if digit_sum > max_sum: max_sum = digit_sum