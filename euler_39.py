# -*- coding:utf-8 -*-
triangles = []
for p in range( 12, 1001 ):
    solutions = []
    for a in range( 3, int( p / 3 ) ):
        for b in range( 4, p - a ):
            c = p - a - b
            if a <= b < c:
                if a**2 + b**2 == c**2:
                    solutions.append(( a, b, c ))
    if len( solutions ) > 0:
        triangles.append(( len( solutions ), p, tuple( solutions ) ))