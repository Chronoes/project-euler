# -*- coding:utf-8 -*-
def is_prime( n ):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    r = int( n**0.5 )
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        else:
            f += 6
    return True
    
primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 ]
i = 33
is_goldbach = True
while is_goldbach:
    i += 2
    if is_prime( i ):
        primes.append( i )
    else:
        is_goldbach = False
        for prime in primes:
            if ( ( i - prime ) / 2 )**0.5 in range( 1, i - prime ):
                is_goldbach = True
                break
        