# -*- coding:utf-8 -*-
fact = 1
for i in range ( 1, 101 ):
    fact *= i
sum = 0
for nr in str( fact ):
    sum += int( nr )
print( sum )