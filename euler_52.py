# -*- coding:utf-8 -*-
i = 10
while True:
    if i % 11 != 0:
        multiples = [ str( i ) ]
        for x in [ 2, 3, 4, 5, 6 ]:
            i_string = str( i * x )
            if sorted( multiples[ 0 ] ) != sorted( i_string ):
                break
            multiples.append( i_string )
    if len( multiples ) == 6:
        print( i )
        break
    i += 1