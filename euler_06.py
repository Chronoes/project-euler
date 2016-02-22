# -*- coding:utf-8 -*-
sum, sum2 = 0, 0
for i in range( 1, 101 ):
    sum += i * i
    sum2 += i
sum2 *= sum2
print( sum2 - sum )