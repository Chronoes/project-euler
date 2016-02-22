# -*- coding:utf-8 -*-
i = 1
array = list( range( 2, 20 ) )
while True:
    arv = 20 * i
    leitud = True
    for jagatav in array:
        if arv % jagatav != 0:
            leitud = False
            break
    if leitud:
        break
    i += 1
print( arv )