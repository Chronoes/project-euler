# -*- coding:utf-8 -*-
algarvud = [2]
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
    
for jagaja in range( 3, 2000000, 2 ):
    if is_prime( jagaja ):
        algarvud.append( jagaja )
        
print( sum( algarvud ) )