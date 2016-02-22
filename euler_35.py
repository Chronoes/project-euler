# -*- coding:utf-8 -*-
import time


algarvud = [2]
for jagaja in range( 3, 1000000, 2 ):
    on_algarv = True
    for algarv in algarvud:
        if jagaja % algarv == 0:
            on_algarv = False
            break   
    if on_algarv:
        algarvud.append( jagaja )
        
count = 0
for algarv in algarvud:
    sobiv = True
    algarv_str = str( algarv )
    for _ in range( len( algarv_str ) ):
        algarv_str = algarv_str[ 1:len( algarv_str ) ] + algarv_str[ :1 ]
        if int( algarv_str ) not in algarvud:
            sobiv = False
            break
    if sobiv:
        count += 1
