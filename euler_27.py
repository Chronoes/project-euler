# -*- coding:utf-8 -*-
sum = 1
for i, scale in enumerate( range( 3, 1001 + 1, 2 ) ):
    prevscale = scale - 2
    for n in range( prevscale**2, scale**2 + 1 ):
        if n % 2**(i + 1) == 1:
            sum += n