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

def make_prime(start=2, end=float('inf')):
    if start < 11:
        yield 2
        yield 3
        yield 5
        yield 7
    f = 11
    while f < end:
        if is_prime(f):
            yield f
        if is_prime(f+2):
            yield f+2
        f += 6

def product(iterable):
    total = 1
    for el in iterable: total *= el
    return total

def divver(nr, div, times=0):
    if nr % div == 0:
        return divver(nr//div, div, times + 1)
    return nr, times


def main():
    triangle = 1
    nr = 2
    divisors = {}
    for p in results: data += p.get()
    while product(map(lambda v: v+1, divisors.values())) < 500:
        prime = make_prime()
        triangle += nr
        nr += 1
        p = next(prime)
        divisors = {}
        while p < triangle:
            div_triangle, ppow = divver(triangle, p)
            if ppow:
                divisors[p] = ppow
            if div_triangle == 1:
                break
            p = next(prime)
    print(triangle)
        
def arvutus( triangle, count = 2 ):
    step = 1 if triangle % 2 == 0 else 2
    for i in range( 2 + int( step / 2 ), int( triangle / 2 ) + 1, step ):
        if triangle % i == 0: count += 1
    return count

def old():
    triangle = 1
    n = 2
    divisors = 0
    while arvutus( triangle ) < 500:
        triangle += n
        n += 1
    print( triangle )
    
if __name__ == '__main__':
    main()