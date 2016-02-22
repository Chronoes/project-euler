# -*- coding:utf-8 -*-

d = {}
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        if n - 2 not in d:
            d[ n - 2 ] = fib( n - 2 )
        if n - 1 in d:
            return d[ n - 1 ] + d[ n - 2 ]
        else:
            return fib( n - 1 ) + d[ n - 2 ]

fibo = ""
i = 4000
while len( fibo ) < 1000:
    i += 1
    fibo = str( fib( i ) )
