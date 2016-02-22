# -*- coding:utf-8 -*-
from itertools import permutations
from string import digits


print( list( permutations( digits ) )[1000000 - 1] )
        
