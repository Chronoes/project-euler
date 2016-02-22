# -*- coding:utf-8 -*-
i = 286
while True:
    for j in range( 166, i ):
        for k in range( 144, j ):
            if i*( i + 1 )/2 == j*( 3*j - 1 )/2 == k*( 2*k - 1 ):
                print( i )
                break
    i += 1