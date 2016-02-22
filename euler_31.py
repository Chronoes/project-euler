# -*- coding:utf-8 -*-
from itertools import combinations_with_replacement


pence = [200, 100, 50, 20, 10, 5, 2, 1]
ways = 0
for i in range( 1, 201 ):
    for pence_sum in combinations_with_replacement( pence, i ):
        pence_sum = sum( pence_sum )
        if pence_sum == 200:
            ways += 1
            