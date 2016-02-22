# -*- coding:utf-8 -*-
from itertools import permutations, combinations


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
unsuitables = []
for i in range( 1001, 10000, 2 ):
    if i in unsuitables:
        continue
    if is_prime( i ):
        numbers = []
        for combo in permutations( str( i ), 4 ):
            combo = int( "".join( combo ) )
            if is_prime( combo ) and combo not in numbers:
                numbers.append( combo )
            else:
                unsuitables.append( combo )
                
        numbers = sorted( numbers )
        for nrs in combinations( numbers, 3 ):
            first = nrs[ 0 ]
            second = nrs[ 1 ]
            third = nrs[ 2 ]
            if third - second == second - first:
                print( first, second, third )
        