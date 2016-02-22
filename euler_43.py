# -*- coding:utf-8 -*-
from itertools import permutations


digits = "0123456789"
divisors = ( 2, 3, 5, 7, 11, 13, 17 )
sum = 0
for combo in permutations( digits, len( digits ) ):
    n = "".join( combo )
    correct = True
    for i in range( len( divisors ) ):
        if int( n[ 1 + i:4 + i ] ) % divisors[ i ] != 0:
            correct = False
            break
    if correct:
        sum += int( n )
        
print( sum )