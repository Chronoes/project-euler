# -*- coding:utf-8 -*-
from itertools import permutations


def is_prime( n ):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        else:
            f += 6
    return True
digits = "987654321"
for i in range( 9, 3, -1 ):
    for combo in permutations( digits, i ):
        n = "".join( combo )
        if is_prime( int( n ) ) and "".join( reversed( sorted( n ))) == digits[ 9 - i: ]:
            print( n )
            break
            