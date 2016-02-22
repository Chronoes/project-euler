# -*- coding:utf-8 -*-

tulemus = []
for arv in range( 100, 1000 ):
    for arv2 in range( 100, 1000 ):
        korrutis = arv * arv2
        v6rdlus = list( str( korrutis ) )
        if v6rdlus == list( reversed( v6rdlus ) ):
            tulemus.append( korrutis )
print( max( tulemus ) )