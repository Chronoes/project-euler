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
primes = [2]
suitables = []
for i in range( 3, 1000000, 2 ):
    if is_prime( i ):
        if i > 1000:
            for j in range( len( primes )):
                prime_sum = []
                for prime in primes[ j: ]:
                    prime_sum.append( prime )
                    if sum( prime_sum ) == i:
                        suitables.append(( len( prime_sum ), i ))
                        break
                    elif sum( prime_sum ) > i:
                        break
                    
        primes.append( i )
        