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
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        else:
            f += 6
    return True

max_tot_n = 0, 0
divisors = {}
for n in range( 2, 1000001 ):
    totient = []
    if is_prime( n ):
        phi = n / ( n - 1 )
    else:
        for i in range( int( n / 2 ), 1, -1 ):
            if i in totient     : continue
            elif i in divisors  : totient += divisors[ i ]
            elif n % i != 0     : totient.append( i )
        divisors[ n ] = totient
        phi = n / (len( totient ) + 1)
            
    if max_tot_n[ 1 ] < phi: max_tot_n = n, phi
    