# -*- coding:utf-8 -*-

for a in range( 999 ):
    for b in range( 999 ):
        if a + b > 1000:
            break
        for c in range( 999 ):
            if a + b + c > 1000:
                break
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print( a * b * c )
                break
                